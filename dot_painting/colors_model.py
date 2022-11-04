# import colorgram
import random

colors = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234),
          (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68)]


class Colors:
    def __init__(self):
        self.num_colors = 10
        self.color_list = colors

    def get_random_color(self):
        random_color = random.choice(self.color_list)
        return random_color

    # use to generate rgb color tuples from the image
    # def get_colors(self):
    #     image = "image.jpg"
    #     colors = colorgram.extract(self.image, self.num_colors)

    #     colors_list = []

    #     for color in colors:
    #         current = color.rgb
    #         r = current.r
    #         g = current.g
    #         b = current.b
    #         color_tuple = (r, g, b)
    #         colors_list.append(color_tuple)

    #     return colors_list
