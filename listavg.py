class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = sum(lst)  # initialize total with the sum of the initial list
        self.length = len(lst)  # initialize length with the length of the initial list

    def add(self, num):
        self.lst.append(num)
        self.total += num  # update total with the added number
        self.length += 1  # update length

    def compute_avg(self):
        return self.total / self.length

    def compute_avg_faster(self):
        return self.total / self.length
