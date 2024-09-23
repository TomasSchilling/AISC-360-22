#Calculate geometric properties
import numpy as np
class H:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        self.A  = (self.D-2*self.tf)*(self.tw) +2 *(self.bf)* (self.tf)
        self.Ix = 2*((self.bf)*(self.tf)*((self.D-self.tf)/2)**2)+2*(self.bf)*(self.tf)**3/12+(self.D-2*self.tf)**3*(self.tw)/12
        self.Iy =  (2*(self.tf)*self.bf**3 + (self.D-2*self.tf)*(self.tw)**3)/ 12
        self.rx = np.sqrt(self.Ix /self.A)
        self.ry = np.sqrt(self.Iy /self.A)
        self.Zx = self.bf*self.tf*(self.h+self.tf)+self.tw*self.h**2/4 
        self.Zy = self.tf*self.bf**2/2+self.h*self.tw**2/4
        self.J  = (2*self.bf*self.tf**3+(self.h+self.tf)*self.tw**3)/3 
        self.Cw = self.tf*self.bf**3*(self.h+self.tf)**2/24
        
        self.Sx = self.Ix / (self.D / 2)
        self.Sy = self.Iy / (self.bf / 2)  
        self.rt = np.sqrt(self.Ix / self.A)
        self.rts = np.sqrt(self.Cw / self.A)
        self.Aw = self.D * self.tw
        
        
class T:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta
        
class C_l:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta      

class C_p:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta   
  
        
class L_l:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta    
    
class L_p:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta  

class XL_p:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta  

class O:
    
    def __init__(self,D,t,e_c=0):
        self.D=D
        self.t= t-e_c
        
        ##### Falta  

class B:
    
    def __init__(self,D,bf,tf,tw,e_c=0):
        self.D=D
        self.bf=bf
        self.tf=tf-e_c
        self.tw=tw-e_c 
        self.h=(self.D-tf*2)
        
        ##### Falta  















m=1
cm=0.01
mm=0.001


Hn= H(200*mm,150*mm,8*mm,6*mm,1*mm)
print(Hn.A/cm**2)
print(Hn.rx/cm)
print(Hn.ry/cm)
print(Hn.Sx/cm**3,Hn.Sy/cm**3,sep="\n")
print(Hn.Zx/cm**3,Hn.Zy/cm**3,sep="\n")
print(Hn.J/cm**4,Hn.Cw/cm**6,sep="\n")
print(Hn.Ix/cm**4,Hn.Iy/cm**4)

print(Hn.rt/cm,Hn.rts/cm,Hn.Aw/cm**2)

