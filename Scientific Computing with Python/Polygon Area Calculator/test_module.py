class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return (self.width * self.height)
  
  def get_perimeter(self):
    return (2*self.width + 2*self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    if(self.width>50 or self.height>50):
      return 'Too big for picture.'
    output = ''
    for line in range(self.height):
      output += '*'*self.width + '\n'
    return output
  
  def get_amount_inside(self, shape):
    if self.width < shape.width or self.height < shape.height :
      return 0
    else:
      outerArea = self.get_area()
      innerArea = shape.get_area()
      return int(outerArea/innerArea)
  
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)

  def set_side(self, side):
    self.height = side
    self.width = side
  
  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)

  def __str__(self):
    return f'Square(side={self.width})'