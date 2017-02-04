class Colour(object):

    def __init__(self, name, red, green, blue, clear=None):
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
        self.clear = clear

    def get_name(self):
        return self.name

    def get_red(self):
        return self.red

    def get_green(self):
        return self.green

    def get_blue(self):
        return self.blue

    def get_clear(self):
        return self.clear

    def calc_distance(self, cmp_colour):
        return (self.red-cmp_colour.red)**2 + (self.green-cmp_colour.green)**2 +(self.blue-cmp_colour.blue)**2
