#import colorgram
import random
import turtle as t # Can use import * to import all modules, not recommended to use though
#import heroes
#print(heroes.gen())
# import turtle as t gives a name shortcut for it
# tim = t.Turtle() to use the shortcut
# import heroes wouldn't work because it's not a built-in module (find in pypi)
#tim = t.Turtle()
#t.colormode(255)
#
#def random_color_f():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    random_color = (r, g, b)
#    return random_color
#tim.shape("turtle")
#tim.color("coral")

#for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

#for _ in range(10):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()



#def draw_shape(num_sides):
#    angle = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(angle)
#
#for i in range (3, 11):
#    tim.color(random.choice(colors))
#    draw_shape(i)

#directions = [0, 90, 180, 270]
#tim.width(10)
#tim.speed(500)
#while True:
#    tim.forward(20)
#    tim.setheading(random.choice(directions))
#    tim.color(random_color_f())

#extent_number = 10
#tim.speed("fastest")
#while True:
#    tim.color(random_color_f())
#    tim.circle(100, 360)
#    tim.right(5)


# You can use tuples to basically have immutable lists
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
# After acquiring the colors using colorgram, you put them in color_list

t.colormode(255)
tim = t.Turtle()
color_list = [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (108, 68, 84), (113, 161, 175), (40, 37, 35), (23, 122, 173), (64, 153, 139), (77, 40, 48), (90, 142, 53), (9, 67, 47), (180, 97, 80), (131, 39, 41), (211, 202, 152), (140, 172, 157), (176, 152, 158), (178, 201, 186), (218, 181, 171), (169, 200, 209), (205, 183, 188), (41, 75, 61), (148, 116, 122), (39, 72, 81), (97, 138, 153)]

tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(25, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


