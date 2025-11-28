from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
timer2 = 0
cative= False
ctimer = 0
val = 10
regenrateTime = 15
timeHit = 0
timer = 120
slide_speed = 2
GameMode = 1
slide = 0
rightorleft = 1
newGame = 1
walls = {}
boulders = {}
bots = {}
nitro = {}
coins = {}
Fanhappy = 0
nitroON = 0
LapCounter = 0
nitroTime = 0
LapComplete = False
points = 0
nitrus = 0
health = 50
GameOver = 0
hitTimer = 2
hit  = False
key_states = {'w': False, 'a': False, 's': False, 'd': False}
px, pz = 0, -1880
angle = 0.0
step = 20
rstep = 5
track_tiles_x = 50
track_tiles_z = 50
track_width_in_tiles = 3
tile_size = 80
fd = []
hlsl = False
light_colors = [
    (0.67, 0.84, 0.90), # Light Blue
    (0.56, 0.93, 0.56), # Light Green
    (0.93, 0.93, 0.56), # Light Yellow
    (0.90, 0.67, 0.84), # Light Pink
    (0.80, 0.67, 0.90), # Lavender
    (0.94, 0.82, 0.70), # Peach
    (0.70, 0.94, 0.82), # Mint
    (0.95, 0.75, 0.75), # Light Coral
    (0.75, 0.95, 0.95), # Light Cyan
    (0.85, 0.85, 0.85), # Light Gray
    (0.90, 0.90, 0.80), # Beige
    (0.80, 0.90, 0.90), # Pale Turquoise
]
def draw_text(x, y, text):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
def strips():
    sw = 15.0
    sh = 1.0
    sl = 40


    def dsl(length, is_horizontal):
        n = int(length * 2 / sl)
        startp = -length
        is_red = True
        for i in range(n):
            if is_red:
                glColor3f(0.8, 0.0, 0.0)
            else:
                glColor3f(1.0, 1.0, 1.0)

            p1 = startp + i * sl
            p2 = p1 + sl

            glBegin(GL_QUADS)
            if is_horizontal:
                glVertex3f(p1, 0, -7.5)
                glVertex3f(p2, 0, -7.5)
                glVertex3f(p2, 0,  7.5)
                glVertex3f(p1, 0,  7.5)
            else:
                glVertex3f(-7.5, 0, p1)
                glVertex3f(-7.5, 0, p2)
                glVertex3f( 7.5, 0, p2)
                glVertex3f( 7.5, 0, p1)
            glEnd()
            is_red = not is_red

    # Outer Strips
    glPushMatrix()
    glTranslatef(0, 1.0, 1992.5)
    dsl(2000.0, True)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 1.0, -1992.5)
    dsl(2000.0, True)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1992.5, 1.0, 0)
    dsl(2000.0, False)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1992.5, 1.0, 0)
    dsl(2000.0, False)
    glPopMatrix()

    # Inner Strips
    glPushMatrix()
    glTranslatef(0, 1.0, 1767.5)
    dsl(1760.0, True)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 1.0, -1767.5)
    dsl(1760.0, True)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1767.5, 1.0, 0)
    dsl(1760.0, False)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1767.5, 1.0, 0)
    dsl(1760.0, False)
    glPopMatrix()
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
def stadium():
    glColor3f(0.6, 0.6, 0.65)
    glPushMatrix()
    glTranslatef(0, 5.0, -2125.0)
    glScalef(4250, 10, 50)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 5.0, 2125.0)
    glScalef(4250, 10, 50)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2125.0, 5.0, 0)
    glScalef(50, 10, 4250)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2125.0, 5.0, 0)
    glScalef(50, 10, 4250)
    glutSolidCube(1)
    glPopMatrix()



    glPushMatrix()
    glTranslatef(0, 10.0, -2200.0)
    glScalef(4400, 20, 100)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 10.0, 2200.0)
    glScalef(4400, 20, 100)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2200.0, 10.0, 0)
    glScalef(100, 20, 4400)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2200.0, 10.0, 0)
    glScalef(100, 20, 4400)
    glutSolidCube(1)
    glPopMatrix()


   
    glPushMatrix()
    glTranslatef(0, 15.0, -2275.0)
    glScalef(4550, 30, 150)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 15.0, 2275.0)
    glScalef(4550, 30, 150)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2275.0, 15.0, 0)
    glScalef(150, 30, 4550)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2275.0, 15.0, 0)
    glScalef(150, 30, 4550)
    glutSolidCube(1)
    glPopMatrix()



    glPushMatrix()
    glTranslatef(0, 20.0, -2350.0)
    glScalef(4700, 40, 200)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 20.0, 2350.0)
    glScalef(4700, 40, 200)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2350.0, 20.0, 0)
    glScalef(200, 40, 4700)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2350.0, 20.0, 0)
    glScalef(200, 40, 4700)
    glutSolidCube(1)
    glPopMatrix()


def fence(length):

    for xp in range(int(-length / 2), int(length / 2), 100):
        glPushMatrix()
        glTranslatef(xp, 25.0, 0)
        glScalef(5, 50, 5)
        glutSolidCube(1)
        glPopMatrix()

    # Draw the long horizontal rails
    glPushMatrix()
    glTranslatef(0, 45.0, 0)
    glScalef(length, 5, 5)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, 25.0, 0)
    glScalef(length, 5, 5)
    glutSolidCube(1)
    glPopMatrix()

def drawFence():

    glColor3f(0.5, 0.5, 0.5)

    glPushMatrix()
    glTranslatef(0, 0, 2050.0)
    fence(4000.0)
    glPopMatrix()
    
   
    glPushMatrix()
    glTranslatef(0, 0, -2050.0)
    fence(4000.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2050.0, 0, 0)
    glRotatef(90, 0, 1, 0)
    fence(4000.0)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-2050.0, 0, 0)
    glRotatef(90, 0, 1, 0)
    fence(4000.0)
    glPopMatrix()

def box(r, c, color):
    ox = 25
    oz = 25
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex3f((r - ox) * 80, 0, (c - oz) * 80)
    glVertex3f((r - ox) * 80 + 80, 0, (c - oz) * 80)
    glVertex3f((r - ox) * 80 + 80, 0, (c - oz) * 80 + 80)
    glVertex3f((r - ox) * 80, 0, (c - oz) * 80 + 80)
    glEnd()

def racetrack():
    for i in range(50):
        for j in range(50):
            is_track = (i < 3 or
                        i >= 47 or
                        j < 3 or
                        j >= 47)
            
            if is_track:
                color = (0.7, 0.7, 0.7)  # Gray color for the track
            else:
                color = (0.1, 0.6, 0.1)  # Green color for the infield
            
            box(i, j, color)

spin_angle = 0.0   # rotation angle


def drawCoin(ccx,ccz):
    coin_radius = 10
    coin_thickness = 0.2
    coin_color = (1.0, 0.84, 0.0)

    glPushMatrix()
    glTranslatef(ccx, 20, ccz)
    glRotatef(spin_angle, 0, 1, 0)
    glColor3f(*coin_color)

    glPushMatrix()
    glScalef(1.0, 1.0, 0.02)
    quad = gluNewQuadric()
    gluSphere(quad, coin_radius, 40, 40)
    glPopMatrix()
    glPopMatrix()





def drawNitro(nx, nz):
    nitro_color = (0.0, 0.5, 1.0)
    glPushMatrix()
    glTranslatef(nx, 20, nz)
    glRotatef(spin_angle, 0, 1, 0)
    glColor3f(*nitro_color)

    quad = gluNewQuadric()
    gluCylinder(quad, 6, 6, 20, 40, 40)
    glPushMatrix()
    glTranslatef(0, 0, 24)
    gluSphere(quad, 4, 40, 40)
    glPopMatrix()

    glPopMatrix()




tile_size = 80

def start():

    glPushMatrix()
    glTranslatef(0, 1.0, -2000)
    


    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 0.0)
    glVertex3f(0.0, 0, 0.0)
    glVertex3f(0.0, 0, 40.0)
    glVertex3f(-40.0, 0, 40.0)
    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 40.0)
    glVertex3f(0.0, 0, 40.0)
    glVertex3f(0.0, 0, 80.0)
    glVertex3f(-40.0, 0, 80.0)
    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 80.0)
    glVertex3f(0.0, 0, 80.0)
    glVertex3f(0.0, 0, 120.0)
    glVertex3f(-40.0, 0, 120.0)
    glEnd()
    
  
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 120.0)
    glVertex3f(0.0, 0, 120.0)
    glVertex3f(0.0, 0, 160.0)
    glVertex3f(-40.0, 0, 160.0)
    glEnd()

    
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 160.0)
    glVertex3f(0.0, 0, 160.0)
    glVertex3f(0.0, 0, 200.0)
    glVertex3f(-40.0, 0, 200.0)
    glEnd()


    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(-40.0, 0, 200.0)
    glVertex3f(0.0, 0, 200.0)
    glVertex3f(0.0, 0, 240.0)
    glVertex3f(-40.0, 0, 240.0)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 0.0)
    glVertex3f(40.0, 0, 0.0)
    glVertex3f(40.0, 0, 40.0)
    glVertex3f(0.0, 0, 40.0)
    glEnd()


    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 40.0)
    glVertex3f(40.0, 0, 40.0)
    glVertex3f(40.0, 0, 80.0)
    glVertex3f(0.0, 0, 80.0)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 80.0)
    glVertex3f(40.0, 0, 80.0)
    glVertex3f(40.0, 0, 120.0)
    glVertex3f(0.0, 0, 120.0)
    glEnd()

    
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 120.0)
    glVertex3f(40.0, 0, 120.0)
    glVertex3f(40.0, 0, 160.0)
    glVertex3f(0.0, 0, 160.0)
    glEnd()

    
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 160.0)
    glVertex3f(40.0, 0, 160.0)
    glVertex3f(40.0, 0, 200.0)
    glVertex3f(0.0, 0, 200.0)
    glEnd()

    
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 0, 200.0)
    glVertex3f(40.0, 0, 200.0)
    glVertex3f(40.0, 0, 240.0)
    glVertex3f(0.0, 0, 240.0)
    glEnd()

   
    glPopMatrix()
    

def Boulder(x, z, track_part):
    boulder_x, boulder_z = x, z
    if track_part == 1 or track_part == 3:
        boulder_z += slide
    elif track_part == 2 or track_part == 4:
        boulder_x += slide

    glPushMatrix()
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(boulder_x, 20, boulder_z)
    glScalef(0.5, 0.5, 0.5)
    glutSolidSphere(40, 100, 100)
    glPopMatrix()


def bot(x, z, boangle, track_part):
    bot_x, bot_z = x, z
    if track_part == 1 or track_part == 3:
        bot_z += slide
    elif track_part == 2 or track_part == 4:
        bot_x += slide
        
    glPushMatrix()
    glTranslatef(bot_x, 50, bot_z)
    glRotatef(boangle, 0, 1, 0)
    glScalef(0.5, 0.5, 0.5)
    
    # BODY
    glPushMatrix()
    glColor3f(0.5, 0.2, 0.1)
    glScalef(15, 12, 15)
    glutSolidCube(4)
    glPopMatrix()

    # HEAD
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(0, 45, 0)
    glutSolidSphere(20, 32, 32)
    glPopMatrix()

    # hand1
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(-30, 20, 0)
    glRotatef(180, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 10, 5, 50, 10, 10)
    glPopMatrix()

    # hand2
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(30, 20, 0)
    glRotatef(180, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 10, 5, 50, 10, 10)
    glPopMatrix()

    # LEG1
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(-15, -15, 0)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 15, 5, 80, 10, 10)
    glPopMatrix()

    # leg2
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(15, -15, 0)
    glRotatef(90, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 15, 5, 80, 10, 10)
    glPopMatrix()
    glPopMatrix()

def wall(x,z,angle):
    glPushMatrix()
    glColor3f(0.463, 0.275, 0.196)
    glTranslatef(x, 20, z)
    glRotatef(angle,0,1,0)
    glScalef(100, 50, 20)
    glutSolidCube(1)
    glPopMatrix()
    

def fans():
    global fd
    for x_pos in range(-2100, 2100, 20):
        fd.append({'x': x_pos, 'y': 10, 'z': 2125.0, 'color': random.choice(light_colors)})
        fd.append({'x': x_pos, 'y': 10, 'z': -2125.0, 'color': random.choice(light_colors)})
    for z_pos in range(-2100, 2100, 20):
        fd.append({'x': 2125.0, 'y': 10, 'z': z_pos, 'color': random.choice(light_colors)})
        fd.append({'x': -2125.0, 'y': 10, 'z': z_pos, 'color': random.choice(light_colors)})
    for x_pos in range(-2150, 2150, 20):
        fd.append({'x': x_pos, 'y': 20, 'z': 2175.0, 'color': random.choice(light_colors)})
        fd.append({'x': x_pos, 'y': 20, 'z': -2175.0, 'color': random.choice(light_colors)})
    for z_pos in range(-2150, 2150, 20):
        fd.append({'x': 2175.0, 'y': 20, 'z': z_pos, 'color': random.choice(light_colors)})
        fd.append({'x': -2175.0, 'y': 20, 'z': z_pos, 'color': random.choice(light_colors)})
    for x_pos in range(-2200, 2200, 20):
        fd.append({'x': x_pos, 'y': 30, 'z': 2225.0, 'color': random.choice(light_colors)})
        fd.append({'x': x_pos, 'y': 30, 'z': -2225.0, 'color': random.choice(light_colors)})
    for z_pos in range(-2200, 2200, 20):
        fd.append({'x': 2225.0, 'y': 30, 'z': z_pos, 'color': random.choice(light_colors)})
        fd.append({'x': -2225.0, 'y': 30, 'z': z_pos, 'color': random.choice(light_colors)})
    for x_pos in range(-2250, 2250, 20):
        fd.append({'x': x_pos, 'y': 40, 'z': 2275.0, 'color': random.choice(light_colors)})
        fd.append({'x': x_pos, 'y': 40, 'z': -2275.0, 'color': random.choice(light_colors)})
    for z_pos in range(-2250, 2250, 20):
        fd.append({'x': 2275.0, 'y': 40, 'z': z_pos, 'color': random.choice(light_colors)})
        fd.append({'x': -2275.0, 'y': 40, 'z': z_pos, 'color': random.choice(light_colors)})
def singleFan(x, y, z, color):
    global LapComplete, cative, ctimer
    if LapComplete == True or cative == True:
        glPushMatrix()
        glTranslatef(x, y, z)
        
        # Body
        glColor3f(*color)
        glPushMatrix()
        glTranslatef(0, 5, 0)
        glScalef(8, 10, 8)
        glutSolidCube(1)
        glPopMatrix()
        
        # Head
        glColor3f(0.9, 0.7, 0.6)
        glPushMatrix()
        glTranslatef(0, 12, 0)
        glutSolidSphere(3, 20, 20)
        glPopMatrix()
        
        # Left Arm
        glPushMatrix()
        glColor3f(0.9, 0.7, 0.6)
        glTranslatef(-5, 12, 0)
        glRotatef(-90, 1, 0, 0)
        quad = gluNewQuadric()
        gluCylinder(quad, 1.2, 0.6, 8, 20, 20)
        glPopMatrix()

        # Right Arm
        glPushMatrix()
        glColor3f(0.9, 0.7, 0.6)
        glTranslatef(5, 12, 0)
        glRotatef(-90, 1, 0, 0)
        quad = gluNewQuadric()
        gluCylinder(quad, 1.2, 0.6, 8, 20, 20)
        glPopMatrix()
        
        glPopMatrix()
    else:
        glPushMatrix()
        glTranslatef(x, y, z)
        # Body
        glColor3f(*color)
        glPushMatrix()
        glTranslatef(0, 5, 0)
        glScalef(8, 10, 8)
        glutSolidCube(1)
        glPopMatrix()
        # Head
        glColor3f(0.9, 0.7, 0.6)
        glPushMatrix()
        glTranslatef(0, 12, 0)
        glutSolidSphere(3, 10, 10)
        glPopMatrix()
        glPopMatrix()

def drawFans():
    for fan in fd:
        singleFan(fan['x'], fan['y'], fan['z'], fan['color'])
def car():
    global px, pz, angle
    if nitroON == 1:
   
        glPushMatrix()
        glTranslatef(px, 20, pz)
        glRotatef(angle, 0, 1, 0)

        # --- Main body ---
        glPushMatrix()
        glColor3f(0.8, 0.0, 0.0)
        glScalef(30, 10, 15)
        glutSolidCube(1)
        glPopMatrix()

        # --- Roof ---
        glPushMatrix()
        glColor3f(0.9, 0.1, 0.1)
        glTranslatef(0, 7, 0)
        glScalef(20, 6, 12)
        glutSolidCube(1)
        glPopMatrix()

        


   
        glPushMatrix()
        glColor3f(0.1, 0.1, 0.1)
        glTranslatef(-10, -5, 8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -1)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

   
        glPushMatrix()
        glColor3f(0.1, 0.1, 0.1)
        glTranslatef(10, -5, 8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -1)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

    
        glPushMatrix()
        glColor3f(0.1, 0.1, 0.1)
        glTranslatef(-10, -5, -8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -1)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

   
        glPushMatrix()
        glColor3f(0.1, 0.1, 0.1)
        glTranslatef(10, -5, -8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -1)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

      
        glColor3f(0.3, 0.3, 0.3)

        # Left Cylinder
        glPushMatrix()
        glTranslatef(-8, -2, -12)
        glRotatef(-90, 0, 1, 0)
        quad = gluNewQuadric()
        gluCylinder(quad, 3, 3, 15, 20, 20)
        glPopMatrix()

        # Right Cylinder
        glPushMatrix()
        glTranslatef(8, -2, -12)
        glRotatef(-90, 0, 1, 0)
        quad = gluNewQuadric()
        gluCylinder(quad, 3, 3, 15, 20, 20)
        glPopMatrix()

        glPopMatrix()

    else:
        if hit == True or health<=20:
            broke = 15
            t1 = 2
            t2 = -4
        else:
            broke = 7
            t1 = -1
            t2 = -1
        glPushMatrix()
        glTranslatef(px, 20, pz)
        glRotatef(angle, 0, 1, 0)
    
        # --- Main body ---
        glPushMatrix()
        glColor3f(0.8, 0.0, 0.0)
        glScalef(30, 10, 15)
        glutSolidCube(1)
        glPopMatrix()

        # --- Roof ---
        glPushMatrix()
        glColor3f(0.9, 0.1, 0.1)
        glTranslatef(0, broke, 0)
        glScalef(20, 6, 12)
        glutSolidCube(1)
        glPopMatrix()


        wheel_color = (0.1, 0.1, 0.1)
        wheel_radius = 5
        wheel_width = 2


        glPushMatrix()
        glColor3f(*wheel_color)
        glTranslatef(-10, -5, 8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, t1)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

 
        glPushMatrix()
        glColor3f(*wheel_color)
        glTranslatef(10, -5, 8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -2 / 2)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()

 
        glPushMatrix()
        glColor3f(*wheel_color)
        glTranslatef(-10, -5, -8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, t2)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()


        glPushMatrix()
        glColor3f(*wheel_color)
        glTranslatef(10, -5, -8)
        quad = gluNewQuadric()
        glTranslatef(0, 0, -2 / 2)
        gluCylinder(quad, 5, 5, 2, 20, 20)
        glPopMatrix()


        glPopMatrix()

# --- KEYBOARD FUNCTIONS ---
def keyDown(key, x, y):
    key_str = key.decode('utf-8').lower()
    if key_str in key_states:
        key_states[key_str] = True
    global nitroON, nitrus, nitroTime, step, GameOver, LapCounter, health, px, pz, angle, points, hlsl, LapComplete, slide, timeHit, timer, val, walls, boulders, bots, nitro, coins, GameMode,timer2, slide_speed
    if key == b'N' or key == b'n':
        if nitrus>0 and nitroON == 0:
            nitroON = 1
            nitrus -= 1
            nitroTime = 3
            step = 50
    if key == b'R' or key == b'r':
        LapComplete = False
        hlsl = False
        px, pz = 0, -1880
        walls = {}
        boulders = {}
        bots = {}
        nitro = {}
        coins = {}
        nitroON = 0
        LapCounter = 0
        nitroTime = 0
        health = 50
        angle = 0
        points = 0
        GameOver = 0
        timeHit = 0
        timer = 120
        val = 10
        slide_speed = 2
        timer2 = 0
        step = 20
    if key == b'X' or key == b'x':
        LapComplete = False
        hlsl = False
        px, pz = 0, -1880
        walls = {}
        boulders = {}
        bots = {}
        nitro = {}
        coins = {}
        nitroON = 0
        LapCounter = 0
        nitroTime = 0
        health = 50
        angle = 0
        points = 0
        GameOver = 0
        timeHit = 0
        timer = 120
        val = 10
        GameMode = 1-GameMode
        timer2 = 0
        slide_speed = 2
        step = 20
        glutPostRedisplay()
        
def keyUp(key, x, y):
    key_str = key.decode('utf-8').lower()
    if key_str in key_states:
        key_states[key_str] = False


def update():
    global px, pz, angle, LapTime, LapCounter, LapComplete, points, GameOver, nitrus, nitroON,nitroTime,step, hit, hitTimer, bots, boulders, walls, hlsl, GameMode, slide, slide_speed, timeHit, regenrateTime,health,timer,val, timer2
    print(px,pz)
    print(nitroON)
    if GameOver == 0 and timer > 0 and GameMode == 1:
        timer -= 0.1
    if timer <= 0:
        timer = 0
        GameOver = 1
    if GameOver == 0 and health < 50:
        timeHit += 0.1
    if timeHit >= regenrateTime:
        health += 1
        if health > 50:
            health = 50
            timeHit = 0
    if key_states['a'] and GameOver == 0:
        angle += rstep
    if key_states['d'] and GameOver == 0:
        angle -= rstep
    rad = math.radians(angle)
    if key_states['w'] and GameOver == 0:
        px += math.cos(rad) * step
        pz -= math.sin(rad) * step
    if key_states['s'] and GameMode == 2 and GameOver == 0:
        px -= math.cos(rad) * step
        pz += math.sin(rad) * step
    global spin_angle
    spin_angle += 5
    if spin_angle >= 360:
        spin_angle = 0
    finishline = -2000 < pz < -1800 and -80 < px < 30.
    if not finishline:
        hlsl = True
        if LapComplete:
             LapComplete = False
    if finishline and hlsl:
        val+=5
        slide_speed += 4
        LapCounter += 1
        points+=50
        LapComplete = True
        hlsl = False
        bots = {}
        boulders = {}
        walls = {}
    if health<=0:
        GameOver = 1
    if nitroON == 1:
        nitroTime-=0.1
        if nitroTime<=0:
            nitroON = 0
            step = 20
    if GameOver == 1:
        newGame = 1
    if health>20:
        step = 20
    if health<20:
        step = 5
    if hit == True:
        hitTimer -= 0.1
        step = 5
        print(hitTimer)
        if hitTimer<=0:
            hit = False
            step = 20
    global  rightorleft
    slide += slide_speed  * rightorleft
    if slide > 50 or slide < 0:
        rightorleft *= -1
    if GameMode == 1:
        xx = -1800 < px < 1800 and -1800 < pz < 1800
        yy = px < -2040 or px > 2040 or pz < -2040 or pz > 2040
        if (xx or yy):
            if health > 0:
                health -= 1
    global cative, ctimer
    if cative:
        ctimer -= 0.1
        if ctimer <= 0:
            cative = False
    if GameMode == 0:
        timer2+=0.1
        
        
    glutPostRedisplay()

def display():
    global points, nitrus, health, points, hit, hitTimer, step, timer, val, cative, ctimer, slide
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    rad = math.radians(angle)
    gluLookAt(px - 120 * math.cos(rad), 60, pz + 120 * math.sin(rad), px, 20, pz, 0, 1, 0)
    for id in range(1, 20):
        if id not in coins:
            track = random.randint(1,4)
            if track == 1:
                cx = random.randint(-1600,1600)
                cz = random.randint(-1960,-1780)
            if track == 2:
                cx = random.randint(1780,1970)
                cz = random.randint(-1700,1740)
            if track == 3:
                cx = random.randint(-1700,1700)
                cz = random.randint(1780,1920)
            if track == 4:
                cx = random.randint(-1940,-1780)
                cz = random.randint(-1700,1780)
                
        

            coins[id] = {
                "track": track,
                "x": cx,
                "z": cz }
    for i in list(coins.keys()):
        c = coins[i]
        dx = px - c["x"]
        dz = pz - c["z"]
        length = math.sqrt(dx**2+dz**2)
        if length<20:
            points+=10
            print("Coin earned", points)
            cative = True
            ctimer = 1
            del coins[i]
        drawCoin(c["x"],c["z"])
    # Nitro section
    for id in range(1, 6):
        if id not in nitro:
            track = random.randint(1,4)
            if track == 1:
                nx = random.randint(-1600,1600)
                nz = random.randint(-1960,-1780)
            if track == 2:
                nx = random.randint(1780,1970)
                nz = random.randint(-1700,1740)
            if track == 3:
                nx = random.randint(-1700,1700)
                nz = random.randint(1780,1920)
            if track == 4:
                nx = random.randint(-1940,-1780)
                nz = random.randint(-1700,1780)
                
        

            nitro[id] = {
                "track": track,
                "x": nx,
                "z": nz }
    for i in list(nitro.keys()):
        n = nitro[i]
        dx = px - n["x"]
        dz = pz - n["z"]
        length = math.sqrt(dx**2+dz**2)
        if length<20:
            if nitrus<3:
                nitrus+=1
                print("Nitro earned", nitrus)
                del nitro[i]
        drawNitro(n["x"],n["z"])
        
    # obstacle section

    global newGame, walls,list1, boulders

        # --- obstacle section ---
        # wall section
    for id in range(1, val):
        if id not in walls:
            track = random.randint(1,4)
            if track == 1:
                choices = list(range(-1600, -199, 100)) + list(range(200, 1601, 100))
                wx = random.choice(choices)
                wz = random.randrange(-1960, -1779, 100)
                wangle = 90

            if track == 2:
                wx = random.randrange(1780, 1971, 100)
                wz = random.randrange(-1700, 1741, 100)
                wangle = 180

            if track == 3:
                wx = random.randrange(-1700, 1701, 100)
                wz = random.randrange(1780, 1921, 100)
                wangle = 90

            if track == 4:
                wx = random.randrange(-1940, -1779, 100)
                wz = random.randrange(-1700, 1781, 100)
                wangle = 360

            walls[id] = {
                "track": track,
                "x": wx,
                "z": wz ,
                "wangle": wangle,
                "avoided": False }
    for i in list(walls.keys()):
        w = walls[i]
        dx = px - w["x"]
        dz = pz - w["z"]
        length = math.sqrt(dx**2+dz**2)
        if length<50 and hit == False and nitroON == 0:
            health-=10
            hit = True
            step = 5
            hitTimer = 2
            timeHit = 0
            del walls[i]
            print("Car Hit", points)
        wall(w["x"],w["z"], w["wangle"])
        
        
        
        # boulders
    for id in range(1, val):
         if id not in boulders:
            track = random.randint(1,4)
            if track == 1:
                choices = list(range(-1600, -199, 100)) + list(range(200, 1601, 100))
                bx = random.choice(choices)
                bz = random.randrange(-1960, -1779, 100)


            if track == 2:
                bx = random.randrange(1780, 1971, 100)
                bz = random.randrange(-1700, 1741, 100)
       

            if track == 3:
                bx = random.randrange(-1700, 1701, 100)
                bz = random.randrange(1780, 1921, 100)
       

            if track == 4:
                bx = random.randrange(-1940, -1779, 100)
                bz = random.randrange(-1700, 1781, 100)
           

            boulders[id] = {
                "track": track,
                "x": bx,
                "z": bz ,
                "avoided": False }
    for i in list(boulders.keys()):
        b = boulders[i]
        final_bx, final_bz = b["x"], b["z"]
        if b["track"] == 1 or b["track"] == 3:
            final_bz += slide
        elif b["track"] == 2 or b["track"] == 4:
            final_bx += slide
        dx = px - final_bx
        dz = pz - final_bz
        length = math.sqrt(dx**2 + dz**2)
        if length<50 and hit == False and nitroON == 0:
            health-=5
            hit = True
            step = 5
            hitTimer = 2
            timeHit = 0

            del boulders[i]
            print("Car Hit", points)
        Boulder(b["x"], b["z"], b["track"])
        
    # Human bot
    
    for id in range(1, val):
        if id not in bots:
            track = random.randint(1,4)
            if track == 1:
                choices = list(range(-1600, -199, 100)) + list(range(200, 1601, 100))
                box = random.choice(choices)
                boz = random.randrange(-1960, -1779, 100)
                boangle = 90

            if track == 2:
                box = random.randrange(1780, 1971, 100)
                boz = random.randrange(-1700, 1741, 100)
                boangle = -90

            if track == 3:
                box = random.randrange(-1700, 1701, 100)
                boz = random.randrange(1780, 1921, 100)
                boangle = -180

            if track == 4:
                box = random.randrange(-1940, -1779, 100)
                boz = random.randrange(-1700, 1781, 100)
                boangle = 180

            bots[id] = {
                "track": track,
                "x": box,
                "z": boz ,
                "wangle": boangle,
                "cheered": False }
    for i in list(bots.keys()):
        bo = bots[i]
        final_box, final_boz = bo["x"], bo["z"]
        if bo["track"] == 1 or bo["track"] == 3:
            final_boz += slide
        elif bo["track"] == 2 or bo["track"] == 4:
            final_box += slide

        dx = px - final_box
        dz = pz - final_boz
        length = math.sqrt(dx**2 + dz**2)
        if length<30 and hit == False and nitroON == 0:
            health-=10
            hit = True
            step = 5
            hitTimer = 2
            timeHit = 0
            print("Car Hit", points)
            del bots[i]
        bot(bo["x"], bo["z"], bo["wangle"], bo["track"])
    draw_text(20, 740, f"Total Laps: {LapCounter}")
    draw_text(20, 770, f"Total Points: {points}")
    draw_text(20, 710, f"Health: {health}")
    draw_text(20, 680, f"Nitro: {nitrus}")
    if GameMode ==1:
        draw_text(800, 770, f"Time Left: {int(timer)}")
    elif GameMode == 0:
        draw_text(800, 770, f"Time Passed : {int(timer2)}")
        
    
    
    if nitroON == 1:
            draw_text(350, 730, f"Nitro Activated: {nitroTime}")
    if LapComplete == True:
            draw_text(350, 730, f"LAP COMPLETED!")
    if GameOver == 1 and GameMode == 1:
            draw_text(450, 740, f"{points} POINTS!")
            draw_text(400, 700, f"GAME OVER! PRESS R TO RESTART")
    if GameOver == 1 and GameMode == 0:
            draw_text(450, 730, f"{points} POINTS!")
            draw_text(450, 700, f"Total Time {timer2}!")
            draw_text(350, 670, f"GAME OVER! PRESS R TO RESTART")
            
            
        
        
    
    racetrack()
    start()
    strips()
    car()
    stadium()
    drawFence()
    drawFans()
    glutSwapBuffers()

def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, width / height, 0.5, 8000)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"TrackStorm")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    fans()
    glutKeyboardFunc(keyDown)
    glutKeyboardUpFunc(keyUp)
    glutIdleFunc(update)

    glutMainLoop()

if __name__ == "__main__":
    main()
