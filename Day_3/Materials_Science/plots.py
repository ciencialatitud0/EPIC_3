import matplotlib.pyplot as plt
from pandas import read_csv

class PlotResults:

    def __init__(self, output):
        self.output = read_csv(output)

    def plot_position(self):
        plt.plot(self.output.time,self.output.crd, label = 'x(t)')
        for i in range(self.output.shape[0]-1):
            if self.output.state[i] != self.output.state[i+1]:
                plt.axvline(x=self.output.time[i+1],label='Hop. at %i'%self.output.time[i+1],\
                            linestyle='--', c = 'purple')
        plt.xlabel('Time (arb.u.)', fontweight = 'bold', fontsize = 16)
        plt.ylabel('$\mathbf{X(a0)}$', fontsize = 16)
        plt.legend()
        plt.savefig("position.pdf", bbox_inches='tight')
        plt.close()

    def plot_velocity(self):
        plt.plot(self.output.time,self.output.vel, label = 'x(t)')
        for i in range(self.output.shape[0]-1):
            if self.output.state[i] != self.output.state[i+1]:
                plt.axvline(x=self.output.time[i+1],label='Hop. at %i'%self.output.time[i+1],\
                            linestyle='--', c = 'purple')
        plt.xlabel('Time (arb.u.)', fontweight = 'bold', fontsize = 16)
        plt.ylabel('$\mathbf{V(a0/arb.u.)}$', fontsize = 16)
        plt.legend()
        plt.savefig("velocity.pdf", bbox_inches='tight')
        plt.close()

    def plot_total_energies(self):
        plt.plot(self.output.time,self.output.etotal, label = '$E_0$')
        for i in range(self.output.shape[0]-1):
            if self.output.state[i] != self.output.state[i+1]:
                plt.axvline(x=self.output.time[i+1],label='Hop. at %i'%self.output.time[i+1],\
                            linestyle='--', c = 'purple')
        plt.xlabel('Time (arb.u.)', fontweight = 'bold', fontsize = 16)
        plt.ylabel('$\mathbf{Energy(a.u.)}$', fontsize = 16)
        plt.legend()
        plt.savefig("total_energies.pdf", bbox_inches='tight')
        plt.close()

    def plot_energies(self):
        plt.plot(self.output.time,self.output.ene_0, label = '$E_0$')
        plt.plot(self.output.time,self.output.ene_1, label = '$E_1$')
        for i in range(self.output.shape[0]-1):
            if self.output.state[i] != self.output.state[i+1]:
                plt.axvline(x=self.output.time[i+1],label='Hop. at %i'%self.output.time[i+1],\
                            linestyle='--', c = 'purple')
        plt.xlabel('Time (arb.u.)', fontweight = 'bold', fontsize = 16)
        plt.ylabel('$\mathbf{Energy(a.u.)}$', fontsize = 16)
        plt.legend()
        plt.savefig("energies.pdf", bbox_inches='tight')
        plt.close()

    def plot_population(self):
        plt.plot(self.output.time,self.output.coff_0, label = '$|C_0(t)|^2$')
        plt.plot(self.output.time,self.output.coff_1, label = '$|C_1(t)|^2$')
        for i in range(self.output.shape[0]-1):
            if self.output.state[i] != self.output.state[i+1]:
                plt.axvline(x=self.output.time[i+1],label='Hop. at %i'%self.output.time[i+1],\
                            linestyle='--', c = 'purple')
        plt.xlabel('Time (arb.u.)', fontweight = 'bold', fontsize = 16)
        plt.ylabel('$\mathbf{Population}$', fontsize = 16)
        plt.legend()
        plt.savefig("population.pdf", bbox_inches='tight')
        plt.close()

if __name__=="__main__":

    output = "results.out"
    picture = PlotResults(output)
    picture.plot_population()
    picture.plot_total_energies()
    picture.plot_energies()
    picture.plot_velocity()
    picture.plot_position()
