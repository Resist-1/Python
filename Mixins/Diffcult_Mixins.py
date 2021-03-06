#Python Code
class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False
    def toggle(self):
        self.status = not self.status

class LimitSizeMixin:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        size_x = min(size_x, 500)
        size_y = min(size_y, 400)
        super().__init__(pos_x, pos_y, size_x, size_y)

class LimitSizeButton(LimitSizeMixin, Button):
    pass

b = LimitSizeButton(10, 20, 2000, 1000)
print(b.size_x)
print(b.size_y)