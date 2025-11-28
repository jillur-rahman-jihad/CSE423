from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import sys

bright_colors = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
    (1.0, 1.0, 0.0),
    (1.0, 0.0, 1.0),
    (0.0, 1.0, 1.0),
    (1.0, 0.5, 0.0),
    (0.5, 0.0, 1.0),
    (0.0, 0.5, 1.0),
    (1.0, 0.0, 0.5),
    (0.0, 1.0, 0.5),
    (0.5, 1.0, 0.0),
    (1.0, 0.25, 0.0),
    (0.25, 1.0, 0.0),
    (0.0, 0.25, 1.0),
    (0.75, 0.0, 1.0),
    (1.0, 0.75, 0.0),
    (0.0, 1.0, 0.75),
    (0.75, 0.0, 0.5),
    (0.5, 0.75, 0.0),
    (0.0, 0.75, 0.75),
    (0.75, 0.25, 0.25),
    (0.25, 0.75, 0.25),
    (0.25, 0.25, 0.75),
    (0.75, 0.25, 0.75),
    (0.75, 0.75, 0.25),
    (0.25, 0.75, 0.75),
    (0.75, 0.5, 0.25),
    (0.5, 0.75, 0.5),
    (0.5, 0.5, 0.75),
    (0.9, 0.1, 0.3),
    (0.3, 0.9, 0.1),
    (0.1, 0.3, 0.9),
    (0.9, 0.3, 0.1),
    (0.1, 0.9, 0.3),
    (0.3, 0.1, 0.9),
    (0.9, 0.1, 0.9),
    (0.1, 0.9, 0.9),
    (0.9, 0.9, 0.1),
    (0.5, 1.0, 1.0)
]
W_Width, W_Height = 500, 500
xd = 0
paussStatus = 0
Score = 0
DiamondInfo = None
Fall = False
DiamondX = random.randint(-235,235)
DiamondY = 200
DiamondSpeed = 1
GameOver = False
DiamondColor = bright_colors[random.randint(0,39)]
BarPosition = [-50+xd, 50+xd, -250, -240]
DiamondPosition = [DiamondX-15, DiamondX+15,DiamondY-30,DiamondY]
BS = 16
def ZoneDetect(x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    if dx>0 and dy>0:
        if abs(dx) > abs(dy):
            return 0
        else:
            return 1
    elif dx<0 and dy>0:
        if abs(dx) > abs(dy):
            return 3
        else:
            return 2
    elif dx<0 and dy<0:
        if abs(dx) > abs(dy):
            return 4
        else:
            return 5
    else:
        if abs(dx) > abs(dy):
            return 7
        else:
            return 6
            
def ToZero(x,y, zone):
    if zone == 1:
        xp = y
        yp = x
    elif zone == 2:
        xp = y
        yp = -x
    elif zone == 3:
        xp = -x
        yp = y
    elif zone == 4:
        xp = -x
        yp = -y
    elif zone == 5:
        xp = -y
        yp = -x
    elif zone == 6:
        xp = -y
        yp = x
    elif zone == 7:
        xp = x
        yp = -y
    return (xp,yp)
   
def BackToReal(xp,yp, zone):
    if zone == 1:
        y = xp
        x = yp
    elif zone == 2:
        y  = xp
        x = -yp
    elif zone == 3:
        x = -xp
        y = yp
    elif zone == 4:
        x = -xp
        y = -yp
    elif zone == 5:
        y = -xp
        x = -yp
    elif zone == 6:
        y = -xp
        x = yp
    elif zone == 7:
        x = xp
        y = -yp
    return (x,y)

def MPL8W(start, end):
    zone = ZoneDetect(start[0], start[1], end[0], end[1])

    if zone == 0:
        nps = start
        npe = end
    else:
        nps = ToZero(start[0], start[1], zone)
        npe = ToZero(end[0], end[1], zone)

    dx = npe[0] - nps[0]
    dy = npe[1] - nps[1]
    D = 2 * dy - dx
    NE = 2 * (dy - dx)
    E = 2 * dy
    pixels = []

    x = nps[0]
    y = nps[1]
    point = (x, y)
    pixels.append(BackToReal(x, y, zone))

    while point != npe:
        if D > 0:
            x += 1
            y += 1
            D += NE
        else:
            x += 1
            D += E
        point = (x, y)
        pixels.append(BackToReal(x, y, zone))
    return pixels

def moveBar(key,x,y):
    global xd, GameOver, paussStatus, BS
    if GameOver == True or paussStatus ==1:
        XD = 0
    else:
    
        if key==GLUT_KEY_LEFT:
            if xd < -198:
                xd+=0
            else:
                xd-= BS
        if key==GLUT_KEY_RIGHT:
            if xd > 198:
                xd+=0
            else:
                xd+= BS
    glutPostRedisplay()
    
def MPLine(pixels, color):
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(color[0],color[1],color[2])
    for x, y in pixels:
        glVertex2f(x, y)
    glEnd()
def mouseButton(button, state, dx, dy):
    global paussStatus, Score, Fall, DiamondX, DiamondY, xd, GameOver, DiamondColor
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = 500 - dy
        x = dx - W_Width // 2
        y = y - W_Height // 2

        if -230 <= x <= -190 and 215 <= y <= 235: # rESTART
            print("Starting Over...")
            GameOver  = False
            Score = 0
            Fall = False
            DiamondX = random.randint(-235, 235)
            DiamondY = 200
            DiamondColor = bright_colors[random.randint(0,39)]
            xd = 0
            glutPostRedisplay()

        elif 190 <= x <= 230 and 205 <= y <= 245:  #Cross

            print("Goodbye")
            #glutLeaveMainLoop()
            os._exit(0)

        elif -5 <= x <= 5 and 200 <= y <= 240:  #PAUSE
            paussStatus = 1 - paussStatus


        glutPostRedisplay()


def LineBar(color):
    global xd

    MPLine(MPL8W((-40 + xd, -250), (40 +xd, -250)),color)
    MPLine(MPL8W((-50 +xd, -240), (50+xd, -240)),color)
    MPLine(MPL8W((50 +xd , -240), (40+xd, -250)),color)
    MPLine(MPL8W((-50 +xd, -240),(-40+xd, -250)),color)
def Diamond():
    global DiamondX, DiamondY, DiamondColor
    MPLine(MPL8W((DiamondX, DiamondY), (DiamondX - 15, DiamondY - 15)),DiamondColor )
    MPLine(MPL8W((DiamondX - 15, DiamondY - 15), (DiamondX, DiamondY - 30)),DiamondColor )
    MPLine(MPL8W((DiamondX, DiamondY - 30), (DiamondX + 15, DiamondY - 15)),DiamondColor )
    MPLine(MPL8W((DiamondX + 15, DiamondY - 15), (DiamondX, DiamondY)),DiamondColor)

    
def Arrow():
    x, y = -230, 225
    MPLine(MPL8W((x, y), (x + 40, y)),(0.0, 1.0, 1.0))
    MPLine(MPL8W((x, y), (x + 10, y + 10)),(0.0, 1.0, 1.0))
    MPLine(MPL8W((x, y), (x + 10, y - 10)),(0.0, 1.0, 1.0))
def Cross():
    x, y = 210, 225
    MPLine(MPL8W((x - 20, y + 20), (x + 20, y - 20)),(1.0, 0.0, 0.0))
    MPLine(MPL8W((x - 20, y - 20), (x + 20, y + 20)),(1.0, 0.0, 0.0))
def pause():
    MPLine(MPL8W((-5, 240), (-5, 200)),(1.0, 0.65, 0.0))
    MPLine(MPL8W((5, 240), (5, 200)),(1.0, 0.65, 0.0))
def triangle():
    MPLine(MPL8W((10, 220), (-10, 240)),(1.0, 0.65, 0.0))
    MPLine(MPL8W((-10, 240), (-10, 200)),(1.0, 0.65, 0.0))
    MPLine(MPL8W((-10, 200), (10, 220)),(1.0, 0.65, 0.0))


    

def display():
    global DiamondX, DiamondY, DiamondSpeed, Fall, Score, paussStatus, GameOver, xd, DiamondColor, BS

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

    if GameOver == True:
        LineBar((1.0,0.0,0.0)) # GAMEOVER RED BAR
        Arrow()
        Cross()
        pause()
        glutSwapBuffers()
    else:
        LineBar((1.0,1.0,1.0))
        Arrow()
        Cross()
        if paussStatus == 1:
            triangle()
            Diamond()
        else:
            pause()
            Diamond()

        # UpdateD positions
            BarPosition = [-50 + xd, 50 + xd, -240, -250]
            DiamondPosition = [DiamondX - 15, DiamondX + 15, DiamondY, DiamondY - 30]
            DiamondY -= DiamondSpeed
            Fall = True

        # Game Over
            if DiamondY < -270:
                print("Game Over!")
                GameOver = True
                DiamondSpeed = 1
                DiamondY = 200
                DiamondX = random.randint(-235, 235)
                DiamondColor = bright_colors[random.randint(0,39)]
                Score = 0
                Fall = False


        # DIAMOND BAR CRASH HANDLING
            elif (BarPosition[1] >= DiamondPosition[0] and BarPosition[0] <= DiamondPosition[1]) and \
                (DiamondY - 30 <= -240 and DiamondY >= -250):
                Score += 1
                if Score>0 and Score%5 == 0:
                    DiamondSpeed+=1
                    BS+=4
                print("Score: ", Score)
                DiamondY = 200
                DiamondX = random.randint(-235, 235)
                DiamondColor = bright_colors[random.randint(0,39)]
                Fall = False

        glutSwapBuffers()
        glutPostRedisplay()


def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"OpenGL Coding Practice")

init()
glutDisplayFunc(display)

glutSpecialFunc(moveBar)
glutMouseFunc(mouseButton)
glutIdleFunc(display)

glutMainLoop()




