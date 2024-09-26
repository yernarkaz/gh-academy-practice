import random


class RandomizedSet:

    def __init__(self):
        # initialized the RandomizedSet object
        self.rset = dict()
        self.idx = list()

    def insert(self, val: int) -> bool:
        # Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        if val in self.rset:
            return False

        self.rset[val] = len(self.idx)
        self.idx.append(val)

        return True

    def remove(self, val: int) -> bool:
        # Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        if val not in self.rset:
            return False

        index = self.rset[val]
        self.idx[index], self.rset[self.idx[-1]] = self.idx[-1], index
        self.idx.pop()

        del self.rset[val]

        return True

    def getRandom(self) -> int:
        # Returns a random element from the current set of the elements (it's guaranteed that at least one element exists when this method is called). Each element must have them same probability of being returned.

        rindex = random.randint(0, len(self.idx) - 1)
        return self.idx[rindex]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.remove(3)
print(obj.getRandom())
