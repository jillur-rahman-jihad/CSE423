from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math
# Camera position
gameOver = 0
phealth = 5
points = 0
bulletmiss = 0
px = 0
pz = 0          # position
angle = 0.0             # rotation around Y-axis in degrees
step = 20            # movement per key press
rstep = 10
enemies = {}
bullets = {}
bid = 1
bs = 20
s = 1
cheatmode = 0
cangle = 45
ch = 600
cdistance = 600
fps = 0
cheatmodefps = 0
cfs = 0


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, 1000, 0, 800)  # left, right, bottom, top

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


#Top-left : (-520, 0, -520)
#Top-right : (440, 0, -520)
#Bottom-left : (-520, 0, 440)
#Bottom-right : (440, 0, 440)

def box(r,c,color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_QUADS)
    glVertex3f((r - 6.5) * 80, 0, (c - 6.5) * 80)
    glVertex3f((r - 6.5) * 80 + 80, 0, (c - 6.5) * 80)
    glVertex3f((r - 6.5) * 80 + 80, 0, (c - 6.5) * 80 + 80)
    glVertex3f((r - 6.5) * 80, 0, (c- 6.5) * 80 + 80)
    glEnd()

def grid():
    counter = 0
    for i in range(13):
        for j in range(13):
            if counter%2==0:
                color = (1.0, 1.0, 1.0)
            else:
                color =(0.5, 0.0, 0.5)
            counter+=1
            box(i,j,color)

    
    glPushMatrix()
    glColor3f(1, 0,1)
    glTranslatef(-520, 25, 0)
    glScalef(2,50,260)#thick, up,h
    glutSolidCube(4)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0, 1, 0)
    glTranslatef(520, 25, 0)
    glScalef(2,50,260)#thick, up,h
    glutSolidCube(4)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0, 0, 1)
    glTranslatef(0, 25, -520)
    glScalef(260,50,2)#thick, up,h
    glutSolidCube(4)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(0, 25, 520)
    glScalef(260,50,2)#thick, up,h
    glutSolidCube(4)
    glPopMatrix()
def player():
    global px, pz, angle, gameOver
    if gameOver ==1 :
        
        glPushMatrix()
        glTranslatef(0 + px, 30, 0 + pz)
        glRotatef(-270, 1, 0, 0)

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
        #Gun
        glPushMatrix()
        glColor3f(0.5, 0.5, 0.5)
        glTranslatef(0, 10, 0)
        glRotatef(180, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 15, 0, 80, 10, 10)
        glPopMatrix()
        # leg1
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
    
    else:
        
        glPushMatrix()
        glTranslatef(0 + px, 100, 0 + pz)
        glRotatef(angle, 0, 1, 0)

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
        #Gun
        glPushMatrix()
        glColor3f(0.5, 0.5, 0.5)
        glTranslatef(0, 10, 0)
        glRotatef(180, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 15, 0, 100, 10, 10)
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
def enemy(x,y):
    global s
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslatef(x, 90, y)
    glScalef(s,s,s)
    glutSolidSphere(15, 100, 100)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(x, 40, y)
    glScalef(s,s,s)
    glutSolidSphere(40, 100, 100)
    glPopMatrix()

def bullet(x=0,y=0):
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(x, 105, y)
    glutSolidCube(12)
    glPopMatrix()
    

def keyboard(key, x, y):
    global px, pz, angle, cheatmode, phealth, bulletmiss, points, enemies, bullets, bid, gameOver, cheatmodefps, cfs, rstep

    rad = math.radians(angle)
    dirForward = (math.sin(rad), 0, -math.cos(rad))

    if key == b'a':      # rotate left
        angle = angle + rstep
        if angle >= 360:
            angle -= 360
        elif angle < 0:
            angle += 360
    elif key == b'd':    # rotate right
        angle = angle - rstep
        if angle >= 360:
            angle -= 360
        elif angle < 0:
            angle += 360
    elif key == b'w':
        if gameOver!=1:
            if -500 <= (px - dirForward[0] * step) <= 500 and -500 <= (pz + dirForward[2] * step) <= 500:
                px -= dirForward[0] * step
                pz += dirForward[2] * step
    elif key == b's':
        if gameOver!=1:
            if -500 <= (px + dirForward[0] * step) <= 500 and -500 <= (pz - dirForward[2] * step) <= 500:
                px += dirForward[0] * step
                pz -= dirForward[2] * step
    elif key == b'c':
        if gameOver!=1:
            cheatmode = 1 - cheatmode
            if cheatmode == 1:
                bulletmiss = 0
    elif key == b'r':
        gameOver = 0
        points = 0
        phealth = 5
        bulletmiss = 0
        enemies = {}
        bullets = {}
        bid = 1
        px = 0
        pz = 0
        angle = 0.0
        fps = 0
        cheatmodefps = 0
        cfs = 0

        print(gameOver)
    if cheatmode == 1:
        if key == b'v':
            cheatmodefps = 1-cheatmodefps
            cfs = angle
    glutPostRedisplay()
def mouse(button, state, x, y):
    global px, pz, angle, bid, fps, cfs
    
    rad = math.radians(angle)
    dirForward = (math.sin(rad), 0, -math.cos(rad))
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        bullets[bid] = (px,pz,dirForward[0],dirForward[2])
        print("Player Bullet Fired!")
        bid+=1
        glutPostRedisplay()
        
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fps = 1-fps
            
    
def special_keys(key, x, y):
    global cangle, ch
    if key == GLUT_KEY_LEFT:
        cangle += 5
    elif key == GLUT_KEY_RIGHT:
        cangle -= 5
    elif key == GLUT_KEY_UP:
        ch+= 20
    elif key == GLUT_KEY_DOWN:
        ch-= 20

    glutPostRedisplay()

def display():
    
    global enemies, angle, px, pz, bullets, bid, bs, bulletmiss, points, phealth, cheatmode, gameOver, cangle, ch, cdistance, cheatmodefps, cfs
    rad = math.radians(angle)
    dirForward = (math.sin(rad), 0, -math.cos(rad))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    if fps == 0:
        gluLookAt(cdistance * math.cos(math.radians(cangle)), ch, cdistance * math.sin(math.radians(cangle)), 0, 0, 0, 0, 1, 0)
    elif fps==1:
        if cheatmodefps ==0:
            gluLookAt(px-50, 190, pz+40, -dirForward[0]+px-50, 190, dirForward[2]+pz+40, 0, 1, 0)
        elif cheatmodefps == 1:
            gluLookAt(px-50, 190, pz+40, -math.sin(math.radians(cfs))+px-50, 190, math.cos(math.radians(cfs))+pz+40, 0, 1, 0)
    if phealth == 0 or bulletmiss >50:
        gameOver = 1
    # Draw grid and player
    if gameOver == 1:
        
        grid()
        player()
        draw_text(20, 770, f"Game is Over! Your Score is {points}")
        draw_text(20, 740, f"PRESS "R" to Restart The Game!")

    elif gameOver == 0:
        grid()
        player()
        
        if cheatmode ==1:
            angle = (angle - 1) % 360
            bullets[bid] = (px,pz,dirForward[0],dirForward[2])
            bid+=1
        #enemy respawn
        for id in range(1, 6):
            if id not in enemies:
                enemies[id] = {
                    "x": random.randint(-500, 500),
                    "z": random.randint(-500, 500),
                    "health": 1,
                    "speed": 0.2
                }

        # Draw enemies
        for i in list(enemies.keys()):
            e = enemies[i]
            dx = px - e["x"]
            dz = pz - e["z"]
            length = math.sqrt(dx**2+dz**2)
            if length <50:
                phealth-=1
                print("Remaining Player Life: ", phealth)
                del enemies[i]
                continue
            #enemy position change
            dx /= length
            dz /= length
            e["x"] += dx * e["speed"]
            e["z"] += dz * e["speed"]
            enemy(e["x"], e["z"])
        for eid in list(enemies.keys()):
            e = enemies[eid]
            ex, ez = e["x"], e["z"]
            for bidk in list(bullets.keys()):
                bx = bullets[bidk][0]
                bz = bullets[bidk][1]
                fx = bullets[bidk][2]
                fz = bullets[bidk][3]
                if (ex - 60 <= bx <= ex + 60) and (ez - 60 <= bz <= ez + 60):
                    del enemies[eid]
                    del bullets[bidk]
                    points+=1
                    break
        for i in list(bullets.keys()):
            bx, by, fx, fz = bullets[i]
            bx -= fx * bs
            by += fz * bs
            if -500 <= bx <= 500 and -500 <= by <= 500:
                bullets[i] = (bx, by, fx, fz)
                bullet(bx, by)
            else:
                if cheatmode!=1:
                    bulletmiss+=1
                    print("Bullet Missed: ", bulletmiss)
                del bullets[i]
        draw_text(10, 770, f"Points:{points}")
        draw_text(10, 740, f"Health:{phealth}")
        draw_text(10, 710, f"Bullet Missed: {bulletmiss}")



    glutSwapBuffers()
def idle():
    global s, gameOver
    if s<1.5:
        if gameOver==0:
    
            s+=0.009
        else:
            s+=0
    else:
        s = 1
    glutPostRedisplay()
    


def reshape(width, height):
    if height == 0:
        height = 1
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, width / height, 0.5, 1500)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Shooting")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special_keys)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    glutMainLoop()

if __name__ == "__main__":
    main()

