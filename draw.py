from display import *

def draw_line(x0, y0, x1, y1, screen, color):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    isSteep = abs(y1 - y0) > abs(x1 - x0)
    if isSteep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    pos = -1 if y0 > y1 else 1
    slope = 2 * (y1 - y0) * pos
    error = 0
    for x in range(x0, x1 + 1):
        if isSteep:
            screen[y0][x] = color[:]
        else:
            screen[x][y0] = color[:]
        error -= slope
        if error < 0:
            y0 += pos
            error += 2 * (x1 - x0)
    
    

