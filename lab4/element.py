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
            # self.x.append(i)

    def compton(self, start, stop, start2, stop2):
        self.uncertainty(start, stop, start2, stop2)
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
        self.x_positive_uncertainty = abs(
            self.comp - self.x_positive_uncertainty)
        self.x_negative_uncertainty = abs(
            self.comp - self.x_negative_uncertainty)
        if self.x_positive_uncertainty == 0:
            self.x_positive_uncertainty = self.scale
        if self.x_negative_uncertainty == 0:
            self.x_negative_uncertainty = self.scale
        print(
            f"{self.name} {self.comp} + {self.x_positive_uncertainty} - {self.x_negative_uncertainty}")

    def compton2(self, start, stop, start2, stop2):
        self.uncertainty(start, stop, start2, stop2)
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
        self.x_positive_uncertainty = abs(
            self.comp2 - self.x_positive_uncertainty)
        if self.x_positive_uncertainty == 0:
            self.x_positive_uncertainty = self.scale
        self.x_negative_uncertainty = abs(
            self.comp2 - self.x_negative_uncertainty)
        if self.x_negative_uncertainty == 0:
            self.x_negative_uncertainty = self.scale
        print(
            f"{self.name} {self.comp2} + {self.x_positive_uncertainty} - {self.x_negative_uncertainty}")

    def rela(self, e):
        k = self.comp * 1.6022e-16
        m = 9.1093837e-31
        c = 299792458
        e *= 1.6022e-16
        p = 2*(e)/c - k/c
        return (p**2)/(2*m)

    def uncertainty(self, start, stop, start2, stop2):
        avg = sum([i * i**(1/2) for i in self.y[start:stop]]) / \
                  sum([i**(1/2) for i in self.y[start:stop]])
        avg2 = sum([i * i**(1/2) for i in self.y[start2:stop2]]) / \
                  sum([i**(1/2) for i in self.y[start2:stop2]])

        uncer = 1/(sum([(1/i**(1/2))**2 for i in self.y[start:stop]]))**(1/2)
        uncer2 = 1 / \
            (sum([(1/i**(1/2))**2 for i in self.y[start2:stop2]]))**(1/2)

        total_uncer = 1/2 * (uncer**2 + uncer2**2)**(1/2)
        total = (avg+avg2)/2
        self.t1 = total
        mini_dist = 999999999999898898989898989898
        final_pos = 0
        for i in range(stop, start2+1):
            if abs(total - total_uncer - self.y[i]) < mini_dist:
                mini_dist = abs(total-total_uncer - self.y[i])
                final_pos = i
        self.x_positive_uncertainty = final_pos * self.scale
        mini_dist = 999999999999898898989898989898
        final_pos = 0
        for i in range(stop, start2+1):
            if abs(total + total_uncer - self.y[i]) < mini_dist:
                mini_dist = abs(total+total_uncer - self.y[i])
                final_pos = i
        self.x_negative_uncertainty = final_pos * self.scale
