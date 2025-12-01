import sys

class dataShape:
    def __init__(self,width,height):
        self.width = width
        self.height = height


if len(sys.argv) > 2:
    temp_width = sys.argv[1]
    temp_height = sys.argv[2]
else:
    temp_width = input('Image width to be analyzed: ')
    temp_height = input('Image height to be analyzed: ')

dimImg = dataShape(int(temp_width), int(temp_height))