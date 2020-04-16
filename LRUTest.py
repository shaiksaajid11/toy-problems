import LRU
class LRUTest:

    def test(self, cache, size):
        '''test case 1'''
        if len(cache.get_cache()) == size:
            print("Test case 1 passed")
        else: 
            print("Test case 1 failed")
        if -1 == cache.get(1):
            print("Test case 2 passed")
        else:
            print("Test case 2 failed")
        if 1 == cache.get(6):
            print("Test case 3 passed") #if cache size is 3, fails for other size
        else:
            print("Test case 3 failed")




size = int(input("Enter the cache size\n"))
cache = LRU.LRU(size)
cache.put(1)
cache.put(2)
cache.put(3)
cache.put(4)
cache.put(5)
cache.put(6)
cache.put(7)
print("Index of 4 is ",end = ' ')
print(cache.get(4))
print(cache.get_cache())
test = LRUTest()
test.test(cache, size)