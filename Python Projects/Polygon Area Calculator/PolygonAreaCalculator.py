class Rectangle():
  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height

  #Print function
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, new_width):
    self.width = new_width

  def set_height(self, new_height):
    self.height = new_height

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    self.perimeter = (2 * self.width) + (2 * self.height)
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = ((self.width**2 + self.height**2)**.5)

    return self.diagonal

  def get_picture(self):
    if self.width <= 50 and self.height <= 50:
      return ("*" * self.width + "\n") * self.height
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    times_inside = round(
        round(self.width / shape.width) * round(self.height / shape.height))
    return times_inside


class Square(Rectangle):

  def __init__(self, width):
    self.width = width
    self.height = width

  def set_side(self, new_side):
    self.width = new_side
    self.height = new_side

  def __str__(self):
    return f"Square(side={self.width})"
