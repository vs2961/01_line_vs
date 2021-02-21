import math

AXIOM = 'F'
RULES = { 'F' : 'G+[[F]-F]-G[-GF]+F',
          'G' : 'GG',
          '[' : '[',
          ']' : ']',
          '+' : '+',
          '-' : '-' }
ITERATIONS = 6
ANGLE = 20*math.pi/180
LENGTH = 5
SIZE=800


def lsystem(start, rules):
    out = ''
    for c in start:
        s = rules[c]
        out += s

    return out

def draw(canvas):
    s = AXIOM
    for i in range(ITERATIONS):
        s = lsystem(s, RULES)

    turtle = Turtle(canvas)
    canvas.stroke(Color('darkgreen'))
    canvas.strokeWeight(2)
    turtle.moveTo(SIZE/4, SIZE-10)
    turtle.left(75*math.pi/180)
    for c in s:
        if c=='F':
            turtle.forward(LENGTH)
        if c=='G':
            turtle.forward(LENGTH)
        elif c=='[':
            turtle.push()
        elif c==']':
            turtle.pop()
        elif c=='+':
            turtle.left(ANGLE)
        elif c=='-':
            turtle.right(ANGLE)


makeSvg("lsystem-tree.svg", draw, pixelSize=(SIZE, SIZE))
