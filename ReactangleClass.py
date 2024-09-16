class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
       
        self._attributes = [{'length': self.length}, {'width': self.width}]
        self._index = 0 
    
    def __iter__(self):
       
        self._index = 0 
        return self
    
    def __next__(self):
       
        if self._index < len(self._attributes):
            result = self._attributes[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration  

# Example usage:
rect = Rectangle(10, 20)

for attr in rect:
    print(attr)
