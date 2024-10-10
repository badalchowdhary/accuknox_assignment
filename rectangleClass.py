class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        attributes = [{'length': self.length}, {'width': self.width}]
        return iter(attributes)

rect = Rectangle(10, 5)

for attribute in rect:
    print(attribute)


# Output
    # {'length': 10}
    # {'width': 5}