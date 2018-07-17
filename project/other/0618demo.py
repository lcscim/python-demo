class Rectangle:
    def __init__(self,width = 0,height = 0):
        self.width = width
        self.height = height

    def __setattr__(self,nam,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(name,value)

    def getArea(self):
        return self.width * self.height
