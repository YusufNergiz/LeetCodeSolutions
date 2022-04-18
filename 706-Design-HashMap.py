### Goals:
### add a new key + value when the function put() is used ---- replace the value of th given key if it exists
### remove the key from the hashmap
### get the value of the key if exists else return -1

class MyHashMap:

    def __init__(self):
        self.map = {}

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        if key in self.map:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.map:
            self.map.pop(key, None)

obj = MyHashMap()
obj.put(1, 10)
obj.put(2, 14)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))

