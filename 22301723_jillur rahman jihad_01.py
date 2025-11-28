#######################TASK1#############################

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

rains = 400
flag = 0
sc = 0

j, k, l = 0.529, 0.808, 0.922
def skyControl(key,x,y):
    global sc
    if key == b'c':
        if sc == 0:
            sc = 1
        else:
            sc = 0
def rainControl(key,x,y):
    global flag
    if flag>25 or flag<-25:
        flag = 0
    if key==GLUT_KEY_LEFT:
        flag+=1
    if key==GLUT_KEY_RIGHT:
        flag-=1
    glutPostRedisplay()

def rainDropBlue():
    global flag, rains
    rain_coords= []
    for i in range(rains):
        rain_coords.append([random.randint(-1500, 1500), random.randint(-1500, 1500)])
    glColor3f(0.6, 0.8, 1.0)
    glLineWidth(1.5)
    glBegin(GL_LINES)
    for i in range(rains):
        x1 = rain_coords[i][0]
        y1 = rain_coords[i][1]
        x2 = x1 - flag
        y2 = y1 - 20
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

    glEnd()
    glutPostRedisplay()



def Fence():
    glColor3f(0.50, 0.23, 0.09)
    # fence boxes
    for i in range(-1000, 750, 50):
        glBegin(GL_QUADS)
        glVertex2f(i, 0)             # bottom left
        glVertex2f(i + 20, 0)  # bottom right
        glVertex2f(i + 20, 100)  # top right
        glVertex2f(i, 100)         # top left
        glEnd()
# fence lines
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(-750, 30)
    glVertex2f(750, 30)
    glVertex2f(-750, 50)
    glVertex2f(750, 50)
    glVertex2f(-750, 70)
    glVertex2f(750, 70)
    glVertex2f(-750, 90)
    glVertex2f(750, 90)
    glEnd()
def rainDropGray():
    global flag, rains
    rain_coords= []
    for i in range(rains):
        rain_coords.append([random.randint(-1500, 1500), random.randint(-1500, 1500)])
    glColor3f(0.4, 0.4, 0.4)
    glLineWidth(1.5)
    glBegin(GL_LINES)
    for i in range(rains):
        x1 = rain_coords[i][0]
        y1 = rain_coords[i][1]
        x2 = x1 - flag
        y2 = y1 - 20
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)

    glEnd()
    glutPostRedisplay()

def windows():
    
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2d(-90, -30)  # Top vertex
    glVertex2d(-90, -60)  # Bottom left vertex
    glVertex2d(-60, -30)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(-60, -30)  # Top vertex
    glVertex2d(-90, -60)  # Bottom left vertex
    glVertex2d(-60, -60)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(90, -30)  # Top vertex
    glVertex2d(90, -60)  # Bottom left vertex
    glVertex2d(60, -30)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(60, -30)  # Top vertex
    glVertex2d(90, -60)  # Bottom left vertex
    glVertex2d(60, -60)  # Bottom right vertex
    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(-75, -30)
    glVertex2d(-75, -60)
    glVertex2d(-90, -45)
    glVertex2d(-60, -45)
    glVertex2d(75, -30)
    glVertex2d(75, -60)
    glVertex2d(90, -45)
    glVertex2d(60, -45)
    glEnd()
def sky(x,y,z):


    glColor3f(x,y,z)

    glBegin(GL_TRIANGLES)
    glVertex2d(1500, 0)  # Top vertex
    glVertex2d(-1500, 1500)  # Bottom left vertex
    glVertex2d(-1500, 60)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(1500, 0)  # Top vertex
    glVertex2d(-1500, 60)  # Bottom left vertex
    glVertex2d(-1500, 0)  # Bottom right vertex
    glEnd()
    
def field():
    glColor3f(0.255, 0.392, 0.133)
    glBegin(GL_TRIANGLES)
    glVertex2d(1500, 60)  # Top vertex
    glVertex2d(-1500, 60)  # Bottom left vertex
    glVertex2d(-1500, -1500)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(1500, 60)  # Top vertex
    glVertex2d(-1500, -1500)  # Bottom left vertex
    glVertex2d(-1500, -1500)  # Bottom right vertex
    glEnd()
    
def house():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(0, 120)  # Top vertex
    glVertex2d(-120, 0)  # Bottom left vertex
    glVertex2d(120, 0)  # Bottom right vertex
    glEnd()
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(-120, 0)  # Top vertex
    glVertex2d(-120, -120)  # Bottom left vertex
    glVertex2d(0, 0)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(0, 0)  # Top vertex
    glVertex2d(-120, -120)  # Bottom left vertex
    glVertex2d(0, -120)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(0, 0)  # Top vertex
    glVertex2d(0, -120)  # Bottom left vertex
    glVertex2d(120, 0)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(120, 0)  # Top vertex
    glVertex2d(0, -120)  # Bottom left vertex
    glVertex2d(120, -120)  # Bottom right vertex
    glEnd()
    # Doors
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2d(30, -3)  # Top vertex
    glVertex2d(-30, -3)  # Bottom left vertex
    glVertex2d(30, -60)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(30, -60)  # Top vertex
    glVertex2d(-30, -3)  # Bottom left vertex
    glVertex2d(-30, -114)  # Bottom right vertex
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2d(30, -60)  # Top vertex
    glVertex2d(-30, -114)  # Bottom left vertex
    glVertex2d(30, -114)  # Bottom right vertex
    glEnd()
    # door midddle line
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2d(0,-3)
    glVertex2d(0,-114)
    glEnd()
    # door corners
    glBegin(GL_TRIANGLES)
    glVertex2d(30, -3)  # Top vertex
    glVertex2d(-3, -3)  # Bottom left vertex
    glVertex2d(0, -7)  # Bottom right vertex
    glEnd()

def display():
    global j, k, l, sc
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,    0,0,0,    0,1,0)
    glMatrixMode(GL_MODELVIEW)
    sky(j,k,l)
    if sc == 0:
        if j < 0.529:
            j += 0.001
        if k < 0.808:
            k += 0.001
        if l < 0.922:
            l += 0.001
    
        j = min(j, 0.529)
        k = min(k, 0.808)
        l = min(l, 0.922)

    elif sc == 1:
        if j > 0:
            j -= 0.001
        if k > 0:
            k -= 0.001
        if l > 0:
            l -= 0.001
        j = max(j, 0)
        k = max(k, 0)
        l = max(l, 0)

    field()
    Fence()
    house()
    windows()
    rainDropBlue()
    rainDropGray()

    glutSwapBuffers()

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,    1,    1,    1000.0)



glutInit()
glutInitWindowSize(1500, 1500)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

window = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutSpecialFunc(rainControl)
glutKeyboardFunc(skyControl)

glutMainLoop()


############################### TASK 2 ##################################
"""
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
W_Width, W_Height = 500, 500
points = []
speed = 1
freeze = 0
prevblink = None
blink = False
blinkstatus = 0
blinkerf = False
prev = 1
def blinker(x):
    global blink
    glutTimerFunc(800, blinker, 0)
    blink = not blink
def point(x, y):
    value = (-1, 1)
    i = random.randint(0, 255) / 255
    j = random.randint(0, 255) / 255
    k = random.randint(0, 255) / 255
    points.append({
        "x": x,
        "y": y,
        "Point_Color": (i, j, k),
        "moveX": random.choice(value),
        "moveY": random.choice(value)
    })
    print(f"Point at:{x},{y}")
def speedControl(key,x,y):
    
    global speed
    if key==GLUT_KEY_UP:
        if freeze == 1:
            print("Screen freezed")
        else:
            speed *= 1.5
            print("Speed increase")
    if key== GLUT_KEY_DOWN:
        if freeze == 1:
            print("Screen freezed")
        else:
            speed /= 1.5
            print("Speed decrease")
def mouse(button, state, x, y):
    global blinkstatus, blinkerf, freeze
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        mx = x - 250
        my = (500 - y) - 250
        if freeze == 1:
            print("Screen freezed")
        else:
            point(mx, my)
            print("point created")
        
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and blinkstatus == 0:
        if freeze == 1:
            print("Screen freezed")
        else:
            blinkstatus = 1
            if blinkerf == False:
                blinker(x)
                print(blinkstatus)
                blinkerf = True
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and blinkstatus == 1:
        if freeze == 1:
            print("Screen freezed")
        else:
            blinkstatus = 0
            print(blinkstatus)
        
    glutPostRedisplay()
        
       
def pauseControl(key,x,y):
    global speed, freeze, prev, blinkstatus, prevblink
    if key == b' ' and freeze == 0:
        prev = speed
        speed = 0
        freeze = 1
        prevblink = blinkstatus
        blinkstatus = 0
    elif key == b' ' and freeze == 1:
        speed = prev
        freeze = 0
        blinkstatus = prevblink
    glutPostRedisplay()

def display():
    global speed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

    glPointSize(5)
    glBegin(GL_POINTS)
    for point in points:
        if point["x"] <= -250 or point["x"] >= 250:
            point["moveX"] *= -1
        if point["y"] <= -250 or point["y"] >= 250:
            point["moveY"] *= -1
        point["x"] += point["moveX"] * speed
        point["y"] += point["moveY"] * speed
        if blinkstatus == 1:
            if blink == False:
                glColor3f(point["Point_Color"][0],point["Point_Color"][1],point["Point_Color"][2])
            else:
                glColor3f(0.0, 0.0, 0.0)
        else:
            glColor3f(point["Point_Color"][0],point["Point_Color"][1],point["Point_Color"][2])
        glVertex2f(point["x"],point["y"])
    glEnd()

    glutSwapBuffers()

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
glutMouseFunc(mouse)
glutKeyboardFunc(pauseControl)
glutSpecialFunc(speedControl)
glutIdleFunc(display)


glutMainLoop()
"""
