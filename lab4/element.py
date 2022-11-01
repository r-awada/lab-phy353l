class element:

    def __init__(self, name, y, peak):
        self.name = name
        self.y = y
        self.peak = peak

    def axis(self):
        maxi = max(self.y)
        self.loc = self.y.index(maxi)
        scale = self.peak/self.loc
        self.x = []
        for i in range(len(self.y)):
            self.x.append(i*scale)

    def compton(self):
        if self.loc - 150 < 0:
            loc = 0
        else:
            loc = self.loc - 150

        top = 0
        postop = 0
        bottom = 99999999999
        for i in range(loc, self.loc):
            if self.y[i] > top:
                top = self.y[i]
                postop = i
            if self.y[i] < self.y[i+1] and self.y[i+1] < self.y[i+2]:
                bottom = i

        self.comp = top +(bottom - top)/2
        print(self.comp)
