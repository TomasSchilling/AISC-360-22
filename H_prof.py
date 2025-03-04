from geom_prop import H

m=1
cm=0.01
mm=0.001


Hn1= H(200*mm,150*mm,8*mm,6*mm,1*mm)
class Calc_H:
    
    def __init__(self, E, Fy, Hn, Pr, Mx, My, Qx, Qy, Lx, Ly, Lz, kx, ky, kz, Cb,Met):
        self.E = E
        self.Fy = Fy
        self.Hn = Hn
        self.Pr = Pr
        self.Mx = Mx
        self.My = My
        self.Qx = Qx
        self.Qy = Qy
        self.Lx = Lx
        self.Ly = Ly
        self.Lz = Lz
        self.kx = kx
        self.ky = ky
        self.kz = kz
        self.Cb = Cb
        self.Met = Met


    def FU_traccion(self):
        
        if self.Met==1:
            
            return self.Pr/(self.Hn.A * self.Fy/1.67)
        elif self.Met ==2:
            
            return self.Pr/ (self.Hn.A * self.Fy*0.9)
        
    def FU_compresion(self):
        return None
    
    def FU_flexion_x(self):
        return None
    
    def FU_flexion_y(self):
        return None
    
    def FU_corte_x(self):
        return None
    
    def FU_corte_y(self):
        return None
    
    def FU_combinado(self):
        return None
    
    
    
a=Calc_H(200*10**9, 248*10*6, Hn1, 10000, 10, 10, 10, 10, 11, 20, 10, 1, 1, 1, 1, 1)
print(a.FU_traccion())
    