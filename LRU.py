class LRU:
    l = []
    size = 0
    def __init__(self, size):
        self.l = []
        self.size = int(size)


    def put(self, element):
        if len(self.l) >= self.size:
            self.l.pop(0)
            self.l.append(element)
        else:
            self.l.append(element)
        return True


    def get(self, element):
        if element not in self.l:
            return -1
        return self.l.index(element)


    def get_cache(self):
        return self.l
