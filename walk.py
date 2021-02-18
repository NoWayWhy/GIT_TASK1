class Walk(Transportation):
    def __init__(self, start, end, distance):
        Transportation.__init__(self, start, end, distance)

    def find_cost(self):
        return 0
