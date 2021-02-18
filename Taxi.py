class Taxi(Transportation):
    def __init__(self, start, end, distance):
        super().__init__(start, end, distance)
        self.rate = 40
        
    def find_cost(self):
        self.cost = super().getD() * self.rate
        return self.cost
