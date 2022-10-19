import math
class drop:

    def __init__(self, dist, fall, rise, temp, voltage=500):
        self.dist = dist
        self.fall = fall
        self.rise = rise
        self.temp = temp + 273
        self.density = 886 #kg/m^3
        self.V = voltage
        self.d = 7.5e-4


    def fall_vel(self):
        avg_fall = sum(self.fall)/len(self.fall)
        distance = (self.dist / 16.7) * 0.00001 #convert pixels to meters
        self.fall_vel = distance/avg_fall

    def rise_vel(self):
        avg_rise = sum(self.rise)/len(self.rise)
        distance = (self.dist / 16.7) * 0.00001 #convert pixels to meters
        self.rise_vel = distance/avg_rise

    def drag(self):
        self.n = 0.0001702*(1+0.00329*self.temp-0.0000070*self.temp**2)

    def radi(self):
        r = ((9*self.n*self.fall_vel)/(2*self.density*9.81))**(1/2)
        self.neff = self.n*(1/(1+((8.2e-3)/(101325*r))))
        self.r = r * (1/(1+(8.2e-3)/101325*r))**(1/2)
        self.r = ((9*self.neff*self.fall_vel)/(2*self.density*9.81))**(1/2)

    def charge(self):
        self.q = (4*self.d*math.pi*self.r**3 * self.density * 9.81 * (self.fall_vel + self.rise_vel))/(3*self.fall_vel*self.V)
        print(self.q/1.602e-19)

    def charge_per_mass(self):
        self.qpm = self.q/(self.density * 4/3 * math.pi * self.r**3)
