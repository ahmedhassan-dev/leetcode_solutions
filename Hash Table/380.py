class RandomizedSet(object):

    def __init__(self):
        self.data = []
        self.data_map = {}

    def insert(self, val):
        if val in self.data:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val):
        if not val in self.data_map:
            return False
        
        index_of_elem_to_remove = self.data_map[val]
        last_elem_in_list = self.data[-1]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

        

    def getRandom(self):
        idx = int(random.random() * len(self.data))
        return self.data[idx]
        # return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()