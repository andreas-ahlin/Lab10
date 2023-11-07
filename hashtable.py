class HashNode:
    def __init__(self, key="", data=None):
        self.key = key
        self.data = data
        self.next = None


# Fyll i kod här nedan för att initiera hashtabellen


class Hashtable:

    def __init__(self, size):
        self.size = size
        self.list = [None]*size

    def store(self, key, data):
        hashedKey = self.hashfunction(key)
        hashNode = HashNode(key, data)
        if self.list[hashedKey] == None:
            self.list[hashedKey] = hashNode
        else:
            tmp = self.list[hashedKey]
            self.list[hashedKey] = hashNode
            self.list[hashedKey].next = tmp

    def search(self, key):
        hashedKey = self.hashfunction(key)
        current = self.list[hashedKey]

        while current is not None:
            if current.key == key:
                return current.data
            current = current.next
        raise KeyError("Nyckel hittades inte i hashtabellen")

    def hashfunction(self, key):  # taget från föreläsning 11
        h = 0
        for c in key:
            h = h*32 + ord(c)
        return h % self.size
        # Fyll i kod här!
