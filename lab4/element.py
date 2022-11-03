class element:

    def __init__(self, name, y, peak):
        self.name = name
        self.y = y
        self.peak = peak

    def axis(self):
        maxi = max(self.y)
        self.loc = self.y.index(maxi)
        self.scale = self.peak/self.loc
        self.x = []
        for i in range(len(self.y)):
            self.x.append(i*self.scale)
            #self.x.append(i)

    def compton(self, start, stop, start2, stop2):
        topAvg = sum(self.y[start:stop])/(stop-start)
        botAvg = sum(self.y[start2:stop2])/(stop2-start2)
        avg = (topAvg+botAvg)/2
        mini_dist = 999999999999898898989898989898
        final_pos = 0
        for i in range(start, stop2+1):
            if abs(avg - self.y[i]) < mini_dist:
                mini_dist = abs(avg - self.y[i])
                final_pos = i

        self.comp = final_pos * self.scale

    def compton2(self, start, stop, start2, stop2):
        topAvg = sum(self.y[start:stop])/(stop-start)
        botAvg = sum(self.y[start2:stop2])/(stop2-start2)
        avg = (topAvg+botAvg)/2
        mini_dist = 999999999999898898989898989898
        final_pos = 0
        for i in range(start, stop2+1):
            if abs(avg - self.y[i]) < mini_dist:
                mini_dist = abs(avg - self.y[i])
                final_pos = i

        self.comp2 = final_pos * self.scale

    def rela(self, e):
        k = self.comp * 1.6022e-16
        m = 9.1093837e-31
        c = 299792458
        e *= 1.6022e-16
        p = 2*(e)/c - k/c
        return (p**2)/(2*m)
