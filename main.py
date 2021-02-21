from display import *
from draw import *
import math

s = new_screen()
RULES = { 'F' : '-[F]++[F][F]-[F][F]G+[-F]-G[-GF]+F',
        'G' : 'GG',
        '[' : '[',
        ']' : ']',
        '+' : '+',
        '-' : '-' }

def draw(x, y, angle, dist, screen, color):
    angle = math.radians(angle)
    newX = round(x + dist * math.sin(angle))
    newY = round(y + dist * math.cos(angle))
    draw_line(x, y, newX, newY, screen, color)
    return (newX, newY)

def init_tree(iters, start):
    for i in range(iters):
        new = ""
        for char in start:
            new += RULES[char]
        start = new
    return start

def draw_tree(x, y, inst, init_angle, angle, dist, screen):
    color = [79, 130, 66]
    curr_angle = init_angle
    stack = []
    for cmd in inst:
        if cmd == 'F':
            x, y = draw(x, y, curr_angle, dist, screen, color)
        elif cmd == 'G':
            x, y = draw(x, y, curr_angle, dist, screen, color)
        elif cmd == '+':
            curr_angle += angle
        elif cmd == '-':
            curr_angle -= angle
        elif cmd == '[':
            stack.append((x, y, curr_angle))
        elif cmd == ']':
            x, y, curr_angle = stack.pop()


for x in range(XRES):
    for y in range(YRES):
        s[y][x] = [ 0, 191, 255]


color = [31, 47, 26]
x = init_tree(7, "F")
draw_tree(XRES - 50, YRES / 2 + 30, x, 270, 35, 1.2, s)

for x in range(XRES):
    for y in range(YRES - 40, YRES):
        s[y][x] = [210,105,30]

"""
c = [ 0, 255, 0 ]

#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES / 2, s, c) 
draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

#octants 8 and 4
c[BLUE] = 255;
draw_line(0, YRES-1, XRES-1, 0, s, c);  
draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
draw_line(XRES-1, 0, 0, YRES/2, s, c);

#octants 2 and 6
c[RED] = 255;
c[GREEN] = 0;
c[BLUE] = 0;
draw_line(0, 0, XRES/2, YRES-1, s, c);
draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

#octants 7 and 3
c[BLUE] = 255;
draw_line(0, YRES-1, XRES/2, 0, s, c);
draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

#horizontal and vertical
c[BLUE] = 0;
c[GREEN] = 255;
draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);
"""

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
