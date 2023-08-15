import numpy as np
from colt import Colt


class Tully_1(Colt):

    _user_input = """ 
    # chosen parameters
    a = 0.01 :: float
    b = 1.6 :: float
    c = 0.005 :: float
    d = 1.0  :: float
    factor = 1.0  :: float
    """

    def __init__(self, a,b,c,d, factor):
        """ Tully model 1: Simple avoided crossing 

            Diabatic potential, parameters:
            ------------------------------
                a: float
                b: float
                c: float
                d: float
           factor: float
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.factor = factor

    def from_config(cls,config):
        return cls(config['a'], config['b'], config['c'], config['d'], config['factor'])

    def di_energy(self, x):
        """ returns the matrix of diabatic energies at position x """
        sign_a  = np.copysign(self.a,x)
        V_11 = sign_a*(1-np.exp(-self.b*np.abs(x)))
        V_22 = -V_11
        V_12 = self.c*np.exp(-self.d*(x**2))
        return np.array([ [V_11, V_12], [V_12, V_22] ])
    
 
    def di_gradient(self, x):
        """ returns the matrix of gradients of diabatic energies at position x """
        D_11 = self.a*self.b*np.exp(-self.b*np.abs(x))
        D_22 = -D_11
        D_12 = -self.d*(2*x)*self.c*np.exp(-self.d*(x**2))
        return np.array([ [D_11, D_12], [D_12, D_22] ])
    
    def energy(self, x):
        """ returns the matrix of adiabatic energies at position x """
        u_ij_di = self.di_energy(x)
        energies, coeff = np.linalg.eigh(u_ij_di)
        return energies
    
    def gradient(self, x): 
        """ returns the matrix of adiabatic energies at position x """
        u_ij_di = self.di_energy(x)
        DV = self.di_gradient(x)
        energies, coeff = np.linalg.eigh(u_ij_di)

        gradients= np.dot(coeff.T, np.dot(DV, coeff))
        grad = np.diag(gradients)
        return grad 

    
    def nac(self, x):
        """ returns the couplings at position x using np.linalg.eigh function. 

            In Tully's paper, the Hamiltonian is expressed in a diabatic basis. 
            If the diabatic basis is transformed into adiabatic basis, then 
            the Hellmann-Feynman theorem:
                
                <\phi_i|d/dx|\phi_j> = <\phi_i|dH/dx|\phi_j>/(e_j - e_i),
                
            can be used to compute the nonadiabatic coupling strength (since, 
            this theorem holds for the adiabatic basis). 
            
            The diabatic basis (\psi_j) is related to the adiabatic basis (\phi_k) by 
            the unitary tranformation:
                
                \psi_j = \sum_k \phi_k U_{k,j}
                
        """
        u_ij_di = self.di_energy(x)
        DV = self.di_gradient(x)
        energies, coeff = np.linalg.eigh(u_ij_di)

        dij= np.dot(coeff[:,0].T, np.dot(DV, coeff[:,1]))
        dE = energies[1] - energies[0]
        f = 50.0/self.factor
        return {(0,1): -dij/(f*dE), (1,0): dij/(f*dE)}

if __name__=="__main__":
    #HO = Tully_1(a = 0.01, b = 1.6, c = 0.005, d = 1.0, factor = 50)
    HO = Tully_1.from_questions(config = "model.inp")
    crd = 5
    print(HO.energy(crd))
    print(HO.gradient(crd))
    print(HO.nac(crd))
