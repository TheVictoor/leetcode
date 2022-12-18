
class Allocator:
    def __init__(self, n: int):
        self.memory = [None]*n

    def allocate(self, size: int, mID: int) -> int:
        space_empty = 0
        start_index=None

        # print('MID', mID)
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                # print('empty' , i)
                space_empty+=1
                if start_index is None:
                    start_index = i
            else:
                # print('not empty' , i)
                space_empty = 0
                start_index = None

            if space_empty == size:
                # print('found', start_index, size)
                for r in range(size):
                    # print('inserting ',start_index + r)
                    self.memory[start_index + r] = mID
                return start_index
        return -1

    def free(self, mID: int) -> int:
        f = 0
        for i in range(len(self.memory)):
            # print('memory', self.memory[i], mID)
            if self.memory[i] == mID:
                # print('removing', i)
                self.memory[i] = None
                f+=1
        return f


# Your Allocator object will be instantiated and called as such:
obj = Allocator(10)
print(obj.allocate(1,1))
# print(obj.memory)
print(obj.allocate(1,2))
# print(obj.memory)
print(obj.allocate(1,3))
# print(obj.memory)
print()
print(obj.free(2))
# print(obj.memory)
print(obj.allocate(3,4))
# print(obj.memory)
print(obj.allocate(1,1))
# print(obj.memory)
print()
print(obj.allocate(1,1))
# print(obj.memory)
print(obj.free(1))
# print(obj.memory)
print(obj.allocate(10,2))
# print(obj.memory)
print()
print(obj.free(7))
print(obj.memory)
