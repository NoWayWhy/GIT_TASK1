class Train(Transportation):
    def __init__(self, s_p, e_p, d, n_s):
        super().__init__(self, s_p, e_p)
        self.rate = 5
        self.n_s = n_s

    def find_cost(self):
        self._cost = self.n_s * self.rate
        return self._cost
