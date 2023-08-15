# Excited-state dynamics: Tully scheme implementation and models
This is an introductory lecture on nonadiabatic dynamics, focused on the trajectory surface hopping method based on the Tully scheme. The idea is to get the basis and some tools to excited-state dynamics.
## Settings and Requirements
To run the scripts locally, the following package must be installed:  
pip install pycolt
If you want to run the scripts in Google Colab, then run the following lines:

!git clone https://github.com/gatox/EPIC_3.git

pip install pycolt

%cd EPIC_3/Day3/Materials_Science/

!python vv_sh_tully.py

If you want to plot the results:
!python plots.py
## References
[1] [FSSH](https://github.com/gatox/SH_Tully.git) pluging
[2] Tully, J. C. Molecular dynamics with electronic transitions. J. Chem. Phys. 1990, 93,
1061–1071.
[3] Menger, M. F. S. J.; Ehrmaier, J.; Faraji, S. PySurf: A Framework for Database
Accelerated Direct Dynamics. J. Chem. Theory Comput. 2020, 16, 7681–7689.
