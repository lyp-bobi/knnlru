from cacheQueue import cacheQueue
class LRUCache(cacheQueue):
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value


