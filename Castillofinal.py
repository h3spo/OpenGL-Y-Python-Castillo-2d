from random import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
#import glfw
import random
import pyglet
import sys
import threading
import pygame,sys
from pygame.locals import *

class Ddragon(object):
    def ventana(self):
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowSize(1100,700)
        glutCreateWindow("El castillo mas malote")
        self.mov_X=0.0
        self.mov_Y=0.0
        self.rot_X=0.0
        self.rot_Y=0.0
        self.rot=0.0
        self.escalar=15
        s=Sonido()
        s.musica()
        glClearColor(0.0,0.0,0.0,0.0)
        glutDisplayFunc(self.dragon)
        glutKeyboardFunc(self.trasladar)
        glutSpecialFunc(self.Rotar)
       # glutDisplayFunc(self.texto)
        glutMainLoop()

    

   

    




    def dragon(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        self.dc=Dcastillo()
        self.dc.castillo()
        self.dc.texto()
        glScalef(self.escalar,self.escalar,0)#
        glTranslatef(self.mov_X, self.mov_Y, 0.0)
        glRotatef(self.rot_X,1.0,0.0,0.0)
        glRotatef(self.rot_Y,0.0,1.0,0.0)
        glRotatef(self.rot,0.0,0.0,1.0)
        gluOrtho2D(-30,30,-30,40)


        glBegin(GL_POLYGON)
        glColor3f( 0.945 , 0.486 , 0.050)
        glVertex2d(2,10)
        glVertex2d(2,0)
        glVertex2d(-3,0)
        glVertex2d(-5,10)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f( 0.945 , 0.486 , 0.050)#naranja cuerpo
        glVertex2d(-5,10)
        glVertex2d(-3,0)
        glVertex2d(-7,-2)
        glVertex2d(-10,-2)
        glEnd()
         #sus alitas
        glBegin(GL_TRIANGLES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-3,10)
        glVertex2d(2,10)
        glVertex2d(-1,-0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-4,12)
        glVertex2d(2,10)
        glVertex2d(-3,10)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f( 0.890 , 0.164 , 0.047)
        glVertex2d(-2,15)
        glVertex2d(3,14)
        glVertex2d(2,10)
        glVertex2d(-4,12)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f( 0.890 , 0.164 , 0.047)
        glVertex2d(5,24)
        glVertex2d(6,22)
        glVertex2d(3,14)
        glVertex2d(-2,15)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(5,24)
        glVertex2d(10,25)
        glVertex2d(6,22)
        glEnd()






        glBegin(GL_TRIANGLES)
        glColor3f(0.933 , 0.376 , 0.094)#naranja patas
        glVertex2d(-8,-2)
        glVertex2d(-7,-2)
        glVertex2d(-8,-3)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.945 , 0.486 , 0.050)
        glVertex2d(-5,10)
        glVertex2d(-11,11)
        glVertex2d(-8,-3)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.933 , 0.376 , 0.094)#naranja patas
        glVertex2d(-10,-2)
        glVertex2d(-8,-3)
        glVertex2d(-8,-2)
        glEnd()
        #cuello
        glBegin(GL_POLYGON)
        glColor3f( 0.945 , 0.486 , 0.050)#naranja cuerpo
        glVertex2d(-10,20)
        glVertex2d(-6,20)
        glVertex2d(-5,10)
        glVertex2d(-11,11)
        glEnd()
        #cabeza
        glBegin(GL_TRIANGLES)
        glColor3f(0.945 , 0.486 , 0.050)
        glVertex2d(-10,20)
        glVertex2d(-9,25)
        glVertex2d(-6,20)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f( 0.945 , 0.486 , 0.050)#naranja cuerpo
        glVertex2d(-14,23)
        glVertex2d(-9,25)
        glVertex2d(-10,20)
        glVertex2d(-14,20)
        glEnd()
        #ojito
        glBegin(GL_TRIANGLES)
        glColor3f(0.0 , 0.0 , 0.0)
        glVertex2d(-11,22)
        glVertex2d(-10,23)
        glVertex2d(-10,22)
        glEnd()
        #oreja
        glBegin(GL_TRIANGLES)
        glColor3f(0.047 , 0.725 , 0.890)#azul
        glVertex2d(-9,25)
        glVertex2d(-6,26)
        glVertex2d(-9,23)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.945 , 0.486 , 0.050)
        glVertex2d(-9,23.5)
        glVertex2d(-6,26)
        glVertex2d(-9,23)
        glEnd()
        #cola
        glBegin(GL_POLYGON)
        glColor3f( 0.945 , 0.486 , 0.050)#naranja cuerpo
        glVertex2d(2,10)
        glVertex2d(5,8)
        glVertex2d(5,2)
        glVertex2d(2,0)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.933 , 0.376 , 0.094)#naranja patas
        glVertex2d(2,0)
        glVertex2d(5,2)
        glVertex2d(1,-2)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f( 0.890 , 0.164 , 0.047)#rojo
        glVertex2d(5,8)
        glVertex2d(8,8)
        glVertex2d(8,4)
        glVertex2d(5,2)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(0.047 , 0.725 , 0.890)#azul
        glVertex2d(8,10)
        glVertex2d(12,9)
        glVertex2d(12,5)
        glVertex2d(8,4)
        glEnd()
        glBegin(GL_TRIANGLES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(12,9)
        glVertex2d(20,7)
        glVertex2d(12,5)
        glEnd()
        #fuego
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,23)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,23.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,24)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,24.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,25)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,25.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,26)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,26.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,27)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,27.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,28)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,28.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,29)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,29.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,30)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,30.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,31)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,31.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,32)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,32.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,33)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,33.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,34)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,34.5)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,35)
        glEnd()
        glBegin(GL_LINES)
        glColor3f(0.890 , 0.164 , 0.047)#rojo alitas
        glVertex2d(-13,21.5)
        glVertex2d(-25,35.5)
        glEnd()


        glutSwapBuffers()





    def trasladar(self,key,x,y):
        if  key ==as_8_bit('w') or key== as_8_bit('W'):#
            self.mov_Y+=0.05
        if  key ==as_8_bit('s') or key== as_8_bit('S'):
            self.mov_Y-=0.05
        if  key ==as_8_bit('a') or key== as_8_bit('A'):
            self.mov_X-=0.05
        if  key ==as_8_bit('d') or key== as_8_bit('D'):
            self.mov_X+=0.05


        if  key ==as_8_bit('r') or key== as_8_bit('R'):#+
              self.escalar+=1
        if  key ==as_8_bit('t') or key== as_8_bit('T'):#-
              self.escalar-=1
        glutPostRedisplay()

    def Rotar(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.rot_X+=2.0
        if key == GLUT_KEY_DOWN:
            self.rot_X-=2.0
        if key == GLUT_KEY_LEFT:
            self.rot_Y+=2.0
        if key == GLUT_KEY_RIGHT:
            self.rot_Y-=2.0
        if key == GLUT_KEY_HOME:
            self.rot+=2.0
        if key == GLUT_KEY_END:
            self.rot-=2.0
        glutPostRedisplay()


class Dcastillo(object):
    def castillo(self):





         glMatrixMode(GL_PROJECTION)
         glLoadIdentity()
           #Izq, Der,Abajo,Arriba

         gluOrtho2D(-30,30,-30,40)


         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-10,-3)
         glVertex2d(-10,-15)
         glVertex2d(10,-15)
         glVertex2d(10,-3)
         glEnd()
         #FINALIZA FIGURA 3
         #detalles figura 3
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(-8,-7)
         glVertex2d(-8,-5)
         glVertex2d(-6,-5)
         glVertex2d(-6,-7)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(-4,-7)
         glVertex2d(-4,-5)
         glVertex2d(-2,-5)
         glVertex2d(-2,-7)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(0,-7)
         glVertex2d(0,-5)
         glVertex2d(2,-5)
         glVertex2d(2,-7)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(4,-7)
         glVertex2d(4,-5)
         glVertex2d(6,-5)
         glVertex2d(6,-7)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(8,-7)
         glVertex2d(8,-5)
         glVertex2d(10,-5)
         glVertex2d(10,-7)
         glEnd()
         #parte baja
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(-6,-11)
         glVertex2d(-6,-9)
         glVertex2d(-8,-9)
         glVertex2d(-8,-11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(-2,-11)
         glVertex2d(-2,-9)
         glVertex2d(-4,-9)
         glVertex2d(-4,-11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(2,-11)
         glVertex2d(2,-9)
         glVertex2d(0,-9)
         glVertex2d(0,-11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(6,-11)
         glVertex2d(6,-9)
         glVertex2d(4,-9)
         glVertex2d(4,-11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0 , 0.0 , 0.0)
         glVertex2d(10,-11)
         glVertex2d(10,-9)
         glVertex2d(8,-9)
         glVertex2d(8,-11)
         glEnd()



         #figura 1
         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341,0.333)
         glVertex2d(-10,-15)
         glVertex2d(10,-15)
         glVertex2d(-10,-30)
         glEnd()
          #figura1
         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341,0.333)
         glVertex2d(-10,-30)
         glVertex2d(10,-15)
         glVertex2d(10,-30)
         glEnd()

         #cubo de la puerta figura 1
         glBegin(GL_POLYGON)
         glColor3f( 0.627 , 0.250 , 0.0)
         glVertex2d(-2,-27)
         glVertex2d(-2,-30)
         glVertex2d(2,-30)
         glVertex2d(2,-27)
         glEnd()
         #fin  de cubo de la puerta
         #circulo de la puerta
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.627 , 0.250 , 0.0)
         glVertex2d(0,-27)
         glVertex2d(-2,-27)
         glVertex2d(-1,-26)
         glVertex2d(0,-25.5)
         glVertex2d(1,-26)
         glVertex2d(2,-27)
         glEnd()
         #lineas de la puerta
         glBegin(GL_LINES)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-1,-26)
         glVertex2d(-1,-30)
         glEnd()
         glBegin(GL_LINES)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(0,-26)
         glVertex2d(0,-30)
         glEnd()
         glBegin(GL_LINES)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(1,-26)
         glVertex2d(1,-30)
         glEnd()
           #ladrillos oscuros de figura 1
         glBegin(GL_POLYGON)
         glColor3f(0.0,0.0,0.0)
         glVertex2d(-8,-23)
         glVertex2d(-8,-24)
         glVertex2d(-7,-24)
         glVertex2d(-7,-23)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0,0.0,0.0)
         glVertex2d(4,-23)
         glVertex2d(4,-24)
         glVertex2d(5,-24)
         glVertex2d(5,-23)
         glEnd()







         #CUBOS CENTRALES FIGURA 1
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(-9,-14)
         glVertex2d(-9,-15)
         glVertex2d(-8,-15)
         glVertex2d(-8,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(-7,-14)
         glVertex2d(-7,-15)
         glVertex2d(-6,-15)
         glVertex2d(-6,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(-5,-14)
         glVertex2d(-5,-15)
         glVertex2d(-4,-15)
         glVertex2d(-4,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(-3,-14)
         glVertex2d(-3,-15)
         glVertex2d(-2,-15)
         glVertex2d(-2,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(-1,-14)
         glVertex2d(-1,-15)
         glVertex2d(0,-15)
         glVertex2d(0,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(1,-14)
         glVertex2d(1,-15)
         glVertex2d(0.3,-15)
         glVertex2d(0.3,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(3,-14)
         glVertex2d(3,-15)
         glVertex2d(2,-15)
         glVertex2d(2,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(5,-14)
         glVertex2d(5,-15)
         glVertex2d(4,-15)
         glVertex2d(4,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(7,-14)
         glVertex2d(7,-15)
         glVertex2d(6,-15)
         glVertex2d(6,-14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341, 0.33)
         glVertex2d(9,-14)
         glVertex2d(9,-15)
         glVertex2d(8,-15)
         glVertex2d(8,-14)
         glEnd()

         #figura 1
         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(-15,-30)
         glVertex2d(-10,-21)
         glVertex2d(-10,-30)
         glEnd()
         #figura 1
         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(15,-30)
         glVertex2d(10,-21)
         glVertex2d(10,-30)
         glEnd()

         #FIGURA H5.1
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(17,24)
         glVertex2d(17,20)
         glVertex2d(11,20)
         glVertex2d(11,24)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(0.027 , 0.223 , 0.529)#azul
         glVertex2d(10,24)
         glVertex2d(14,32)
         glVertex2d(18,24)
         glEnd()

         #FIGURA H5
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(17.5,18)
         glVertex2d(17.5,15)
         glVertex2d(10.5,15)
         glVertex2d(10.5,18)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(18,20)
         glVertex2d(17.5,18)
         glVertex2d(10.5,18)
         glVertex2d(10,20)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(11,21)
         glVertex2d(11,20)
         glVertex2d(10,20)
         glVertex2d(10,21)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(13,21)
         glVertex2d(13,20)
         glVertex2d(12,20)
         glVertex2d(12,21)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(15,21)
         glVertex2d(15,20)
         glVertex2d(14,20)
         glVertex2d(14,21)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(17,21)
         glVertex2d(17,20)
         glVertex2d(16,20)
         glVertex2d(16,21)
         glEnd()


         #FIGURA5
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(18,15)
         glVertex2d(18,-13)
         glVertex2d(10,-13)
         glVertex2d(10,15)
         glEnd()
         #cubos superiores figura5
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(10,15)
         glVertex2d(10,16)
         glVertex2d(11,16)
         glVertex2d(11,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(12,15)
         glVertex2d(12,16)
         glVertex2d(13,16)
         glVertex2d(13,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(14,15)
         glVertex2d(14,16)
         glVertex2d(15,16)
         glVertex2d(15,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(16,15)
         glVertex2d(16,16)
         glVertex2d(17,16)
         glVertex2d(17,15)
         glEnd()
         #Detalles figura 5
         glBegin(GL_POLYGON)
         glColor3f(0.996 , 0.996 , 0.996)
         glVertex2d(12,14)
         glVertex2d(12,12)
         glVertex2d(12.5,12)
         glVertex2d(12.5,14)
         glEnd()

         glBegin(GL_POLYGON)
         glColor3f(0.996 , 0.996 , 0.996)
         glVertex2d(14,10)
         glVertex2d(14,8)
         glVertex2d(14.5,8)
         glVertex2d(14.5,10)
         glEnd()

         #FIGURA H6
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(28,10)
         glVertex2d(28,15)
         glVertex2d(25,15)
         glVertex2d(25,10)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(28.5,15.5)
         glVertex2d(28,15)
         glVertex2d(25,15)
         glVertex2d(24.5,15.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(28.5,17)
         glVertex2d(24.5,17)
         glVertex2d(24.5,15.5)
         glVertex2d(28.5,15.5)
         glEnd()

         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(24.5,17)
         glVertex2d(26.5,22)
         glVertex2d(28.5,17)
         glEnd()
         #FIGURA6

         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(28,10)
         glVertex2d(28,-13)
         glVertex2d(18,-13)
         glVertex2d(18,10)
         glEnd()
         #escudo
         glBegin(GL_TRIANGLES)
         glColor3f(1.0, 0.0, 0.0)
         glVertex2d(19,8)
         glVertex2d(19,4)
         glVertex2d(21,4)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(1.0, 0.0, 0.0)
         glVertex2d(21,4)
         glVertex2d(23,8)
         glVertex2d(23,4)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(1.0, 0.0, 0.0)
         glVertex2d(23,4)
         glVertex2d(23,-10)
         glVertex2d(19,-10)
         glVertex2d(19,4)
         glEnd()
         #cubos superiores
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(20,10)
         glVertex2d(20,12)
         glVertex2d(22,12)
         glVertex2d(22,10)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(23,10)
         glVertex2d(23,12)
         glVertex2d(25,12)
         glVertex2d(25,10)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(27,10)
         glVertex2d(27,12)
         glVertex2d(28,12)
         glVertex2d(28,10)
         glEnd()



         #FIGURA 7

         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(29,-6)
         glVertex2d(28,-13)
         glVertex2d(19,-13)
         glVertex2d(18,-6)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(25.5,-4)
         glVertex2d(25.5,-6)
         glVertex2d(21.5,-6)
         glVertex2d(21.5,-4)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(26,-3)
         glVertex2d(25.5,-4)
         glVertex2d(21.5,-4)
         glVertex2d(21,-3)
         glEnd()

         #cubos superiores
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(21.5,-2.5)
         glVertex2d(21.5,-3)
         glVertex2d(21,-3)
         glVertex2d(21,-2.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(22.5,-2.5)
         glVertex2d(22.5,-3)
         glVertex2d(22,-3)
         glVertex2d(22,-2.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(23.5,-2.5)
         glVertex2d(23.5,-3)
         glVertex2d(23,-3)
         glVertex2d(23,-2.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(24.5,-2.5)
         glVertex2d(24.5,-3)
         glVertex2d(24,-3)
         glVertex2d(24,-2.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(26,-2.5)
         glVertex2d(26,-3)
         glVertex2d(25.5,-3)
         glVertex2d(25.5,-2.5)
         glEnd()
         #cubos medio/bajo
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(29,-4)
         glVertex2d(29,-6)
         glVertex2d(26.5,-6)
         glVertex2d(26.5,-4)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(20.5,-4)
         glVertex2d(20.5,-6)
         glVertex2d(18,-6)
         glVertex2d(18,-4)
         glEnd()
         #centro
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(22.5,-4.5)
         glVertex2d(22.5,-5.5)
         glVertex2d(22,-5.5)
         glVertex2d(22,-4.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(25,-4.5)
         glVertex2d(25,-5.5)
         glVertex2d(24.5,-5.5)
         glVertex2d(24.5,-4.5)
         glEnd()


          #FIGURA H5.2
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-18,24)
         glVertex2d(-18,20)
         glVertex2d(-14,20)
         glVertex2d(-14,24)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(0.027 , 0.223 , 0.529)#azul
         glVertex2d(-19,24)
         glVertex2d(-16,32)
         glVertex2d(-13,24)
         glEnd()

         #FIGURA H4.1
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-18.5,18)
         glVertex2d(-18.5,15)
         glVertex2d(-13.5,15)
         glVertex2d(-13.5,18)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-19,20)
         glVertex2d(-18.5,18)
         glVertex2d(-13.5,18)
         glVertex2d(-13,20)
         glEnd()


         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-18,21)
         glVertex2d(-18,20)
         glVertex2d(-17,20)
         glVertex2d(-17,21)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-16,21)
         glVertex2d(-16,20)
         glVertex2d(-15,20)
         glVertex2d(-15,21)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-14,21)
         glVertex2d(-14,20)
         glVertex2d(-13,20)
         glVertex2d(-13,21)
         glEnd()



           #FIGURA H4.1.1
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-26,14)
         glVertex2d(-26,10)
         glVertex2d(-24,10)
         glVertex2d(-24,14)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-26.5,14.5)
         glVertex2d(-26,14)
         glVertex2d(-24,14)
         glVertex2d(-23.5,14.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-26.5,16)
         glVertex2d(-26.5,14.5)
         glVertex2d(-23.5,14.5)
         glVertex2d(-23.5,16)
         glEnd()

         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(-26.5,16)
         glVertex2d(-25,20)
         glVertex2d(-23.5,16)
         glEnd()

         #H4.1.1 PT2
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-23,16)
         glVertex2d(-23,10)
         glVertex2d(-21,10)
         glVertex2d(-21,16)
         glEnd()

         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-23.5,16.5)
         glVertex2d(-23,16)
         glVertex2d(-21,16)
         glVertex2d(-20.5,16.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-23.5,18)
         glVertex2d(-23.5,16.5)
         glVertex2d(-20.5,16.5)
         glVertex2d(-20.5,18)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(0.341, 0.341, 0.333)
         glVertex2d(-23.5,18)
         glVertex2d(-22,23)
         glVertex2d(-20.5,18)
         glEnd()



         # INICIA LA FIGURA 4

         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-28,10)
         glVertex2d(-28,-12)
         glVertex2d(-19,-12)
         glVertex2d(-19,10)
         glEnd()
            #ESCUDO FIGURA 4
         glBegin(GL_TRIANGLES)
         glColor3f( 1.0  ,  0.0  , 0.090)
         glVertex2d(-25,4)
         glVertex2d(-25,2)
         glVertex2d(-22.4,2)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f( 1.0  ,  0.0  , 0.090)
         glVertex2d(-22.4,2)
         glVertex2d(-20,4)
         glVertex2d(-20,2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(1.0, 0.0, 0.090)
         glVertex2d(-25,2)
         glVertex2d(-25,-10)
         glVertex2d(-20,-10)
         glVertex2d(-20,2)
         glEnd()
         #CUBOS SUPERIORES
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-28,11)
         glVertex2d(-28,10)
         glVertex2d(-27,10)
         glVertex2d(-27,11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-26,11)
         glVertex2d(-26,10)
         glVertex2d(-25,10)
         glVertex2d(-25,11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-24,11)
         glVertex2d(-24,10)
         glVertex2d(-23,10)
         glVertex2d(-23,11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-22,11)
         glVertex2d(-22,10)
         glVertex2d(-21,10)
         glVertex2d(-21,11)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.835, 0.835, 0.811)
         glVertex2d(-20,11)
         glVertex2d(-20,10)
         glVertex2d(-19,10)
         glVertex2d(-19,11)
         glEnd()

         #figura 4.1
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-19,15)
         glVertex2d(-19,-12)
         glVertex2d(-13,-12)
         glVertex2d(-13,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-19,15)
         glVertex2d(-19,16)
         glVertex2d(-18,16)
         glVertex2d(-18,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-17,15)
         glVertex2d(-17,16)
         glVertex2d(-16,16)
         glVertex2d(-16,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-15,15)
         glVertex2d(-15,16)
         glVertex2d(-14,16)
         glVertex2d(-14,15)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.741, 0.741, 0.717)
         glVertex2d(-14.5,15)
         glVertex2d(-14.5,16)
         glVertex2d(-13.5,16)
         glVertex2d(-13.5,15)
         glEnd()

         #figura 4.2
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-15,-2)
         glVertex2d(-15,-12)
         glVertex2d(-11,-12)
         glVertex2d(-11,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341,0.333)
         glVertex2d(-14.5,-2)
         glVertex2d(-14.5,-2.5)
         glVertex2d(-14,-2.5)
         glVertex2d(-14,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341,0.333)
         glVertex2d(-13.5,-2)
         glVertex2d(-13.5,-2.5)
         glVertex2d(-13,-2.5)
         glVertex2d(-13,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.341, 0.341,0.333)
         glVertex2d(-12.5,-3)
         glVertex2d(-12.5,-3.5)
         glVertex2d(-12.5,-3.5)
         glVertex2d(-12.5,-3)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5,0.5)
         glVertex2d(-15,-1.5)
         glVertex2d(-15,-2)
         glVertex2d(-14.5,-2)
         glVertex2d(-14.5,-1.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5,0.5)
         glVertex2d(-14,-1.5)
         glVertex2d(-14,-2)
         glVertex2d(-13.5,-2)
         glVertex2d(-13.5,-1.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5,0.5)
         glVertex2d(-13,-1.5)
         glVertex2d(-13,-2)
         glVertex2d(-12.5,-2)
         glVertex2d(-12.5,-1.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5,0.5)
         glVertex2d(-12,-1.5)
         glVertex2d(-12,-2)
         glVertex2d(-11.5,-2)
         glVertex2d(-11.5,-1.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5,0.5)
         glVertex2d(-11.5,-1.5)
         glVertex2d(-11.5,-2)
         glVertex2d(-11,-2)
         glVertex2d(-11,-1.5)
         glEnd()

         # 4.3
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-25,-7)
         glVertex2d(-25,-12)
         glVertex2d(-18,-12)
         glVertex2d(-18,-7)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-26,-7)
         glVertex2d(-25,-7)
         glVertex2d(-25,-8)
         glEnd()
         glBegin(GL_TRIANGLES)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-18,-7)
         glVertex2d(-17,-7)
         glVertex2d(-18,-8)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-19,-6)
         glVertex2d(-19,-7)
         glVertex2d(-17,-7)
         glVertex2d(-17,-6)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-26,-6)
         glVertex2d(-26,-7)
         glVertex2d(-24,-7)
         glVertex2d(-24,-6)
         glEnd()
         #4.3
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-23,-4)
         glVertex2d(-23,-7)
         glVertex2d(-20,-7)
         glVertex2d(-20,-4)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-23,-4)
         glVertex2d(-24,-3)
         glVertex2d(-19,-3)
         glVertex2d(-20,-4)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-24,-2)
         glVertex2d(-24,-3)
         glVertex2d(-23,-3)
         glVertex2d(-23,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-22,-2)
         glVertex2d(-22,-3)
         glVertex2d(-21,-3)
         glVertex2d(-21,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-20,-2)
         glVertex2d(-20,-3)
         glVertex2d(-19,-3)
         glVertex2d(-19,-2)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-22.5,-5.5)
         glVertex2d(-22.5,-5)
         glVertex2d(-22,-5)
         glVertex2d(-22,-5.5)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-20.5,-5.5)
         glVertex2d(-20.5,-5)
         glVertex2d(-20,-5)
         glVertex2d(-20,-5.5)
         glEnd()

         #INICIA FIGURA 3
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-10,-1)
         glVertex2d(-10,-3)
         glVertex2d(-8.5,-3)
         glVertex2d(-8.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-7,-1)
         glVertex2d(-7,-3)
         glVertex2d(-5.5,-3)
         glVertex2d(-5.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-4,-1)
         glVertex2d(-4,-3)
         glVertex2d(-2.5,-3)
         glVertex2d(-2.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(-1,-1)
         glVertex2d(-1,-3)
         glVertex2d(0.5,-3)
         glVertex2d(0.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(2,-1)
         glVertex2d(2,-3)
         glVertex2d(3.5,-3)
         glVertex2d(3.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(5,-1)
         glVertex2d(5,-3)
         glVertex2d(6.5,-3)
         glVertex2d(6.5,-1)
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.5, 0.5, 0.5)
         glVertex2d(8,-1)
         glVertex2d(8,-3)
         glVertex2d(10,-3)
         glVertex2d(10,-1)
         glEnd()






         glBegin(GL_POLYGON)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-13,-28)
         glVertex2d(-13,-29)
         glVertex2d(-12,-29)
         glVertex2d(-12,-28)
         glEnd()
          #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-29,-21)#p1
         glVertex2d(-24,-30)#p2
         glVertex2d(-15,-30)#p3
         glVertex2d(-10,-21)#p4
         glEnd()
        #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(29,-21)#p1
         glVertex2d(24,-30)#p2
         glVertex2d(15,-30)#p3
         glVertex2d(10,-21)#p4
         glEnd()
         #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(29,-13)#p1
         glVertex2d(29,-21)#p2
         glVertex2d(10,-21)#p3
         glVertex2d(10,-13)#p4
         glEnd()
         #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-29,-13)#p1
         glVertex2d(-29,-21)#p2
         glVertex2d(-10,-21)#p3
         glVertex2d(-10,-13)#p4
         glEnd()
         #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-30,-12)#p1
         glVertex2d(-29,-13)#p2
         glVertex2d(-10,-13)#p3
         glVertex2d(-9,-12)#p4
         glEnd()
         #figura 2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(30,-12)#p1
         glVertex2d(29,-13)#p2
         glVertex2d(10,-13)#p3
         glVertex2d(9,-12)#p4
         glEnd()

           #ventana baja
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(18.5,-26)
         glVertex2d(18.5,-30)
         glVertex2d(21.5,-30)
         glVertex2d(21.5,-26)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(20,-26)
         glVertex2d(18.5,-26)
         glVertex2d(18.7,-25.5)
         glVertex2d(19.5,-25)
         glVertex2d(20,-25)
         glVertex2d(20.5,-25)
         glVertex2d(21.3,-25.5)
         glVertex2d(21.5,-26)
         glEnd()
         #Ventana superior
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(11,-17)#p1
         glVertex2d(11,-21)#p2
         glVertex2d(12.5,-21)#p3
         glVertex2d(12.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(16,-17)#p1
         glVertex2d(16,-21)#p2
         glVertex2d(17.5,-21)#p3
         glVertex2d(17.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(22,-17)#p1
         glVertex2d(22,-21)#p2
         glVertex2d(23.5,-21)#p3
         glVertex2d(23.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(26.5,-17)#p1
         glVertex2d(26.5,-21)#p2
         glVertex2d(28,-21)#p3
         glVertex2d(28,-17)#p4
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(11.7,-17)
         glVertex2d(11,-17)
         glVertex2d(11.2,-16.6)
         glVertex2d(11.6,-16)
         glVertex2d(12.2,-16.2)
         glVertex2d(12.3,-16.6)
         glVertex2d(12.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(16.8,-17)
         glVertex2d(16,-17)
         glVertex2d(16.2,-16.5)
         glVertex2d(16.6,-16.2)
         glVertex2d(16.8,-16)
         glVertex2d(17.2,-16.2)
         glVertex2d(17.4,-16.5)
         glVertex2d(17.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(22.8,-17)
         glVertex2d(22,-17)
         glVertex2d(22.2,-16.8)
         glVertex2d(22.4,-16.6)
         glVertex2d(22.8,-16.4)
         glVertex2d(23.1,-16.5)
         glVertex2d(23.2,-16.8)
         glVertex2d(23.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(27.3,-17)
         glVertex2d(26.5,-17)
         glVertex2d(26.7,-16.6)
         glVertex2d(27,-16.2)
         glVertex2d(27.3,-16)
         glVertex2d(27.6,-16.2)
         glVertex2d(27.7,-16.6)
         glVertex2d(28,-17)
         glEnd()

    #inicia cubos superiores
    #izquierda
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-30,-10)#p1
         glVertex2d(-30,-12)#p2
         glVertex2d(-29,-12)#p3
         glVertex2d(-29,-10)#p4
         glEnd()
         #2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-26,-10)
         glVertex2d(-26,-12)
         glVertex2d(-24,-12)
         glVertex2d(-24,-10)
         glEnd()
         #3
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-22,-10)
         glVertex2d(-22,-12)
         glVertex2d(-20,-12)
         glVertex2d(-20,-10)
         glEnd()
         #4
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-18,-10)
         glVertex2d(-18,-12)
         glVertex2d(-16,-12)
         glVertex2d(-16,-10)
         glEnd()
         #5
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-14,-10)
         glVertex2d(-14,-12)
         glVertex2d(-12,-12)
         glVertex2d(-12,-10)
         glEnd()
         #6
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(-10,-10)
         glVertex2d(-10,-12)
         glVertex2d(-9,-12)
         glVertex2d(-9,-10)
         glEnd()
         #ventana baja izquierda
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-18.5,-26)
         glVertex2d(-18.5,-30)
         glVertex2d(-21.5,-30)
         glVertex2d(-21.5,-26)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-20,-26)
         glVertex2d(-18.5,-26)
         glVertex2d(-18.7,-25.5)
         glVertex2d(-19.5,-25)
         glVertex2d(-20,-25)
         glVertex2d(-20.5,-25)
         glVertex2d(-21.3,-25.5)
         glVertex2d(-21.5,-26)
         glEnd()
         #ventanas superior izquierda
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-11,-17)#p1
         glVertex2d(-11,-21)#p2
         glVertex2d(-12.5,-21)#p3
         glVertex2d(-12.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-16,-17)#p1
         glVertex2d(-16,-21)#p2
         glVertex2d(-17.5,-21)#p3
         glVertex2d(-17.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-22,-17)#p1
         glVertex2d(-22,-21)#p2
         glVertex2d(-23.5,-21)#p3
         glVertex2d(-23.5,-17)#p4
         glEnd()
         glBegin(GL_POLYGON)
         glColor3f(0.0, 0.0, 0.0)
         glVertex2d(-26.5,-17)#p1
         glVertex2d(-26.5,-21)#p2
         glVertex2d(-28,-21)#p3
         glVertex2d(-28,-17)#p4
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-11.7,-17)
         glVertex2d(-11,-17)
         glVertex2d(-11.2,-16.6)
         glVertex2d(-11.6,-16)
         glVertex2d(-12.2,-16.2)
         glVertex2d(-12.3,-16.6)
         glVertex2d(-12.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-16.8,-17)
         glVertex2d(-16,-17)
         glVertex2d(-16.2,-16.5)
         glVertex2d(-16.6,-16.2)
         glVertex2d(-16.8,-16)
         glVertex2d(-17.2,-16.2)
         glVertex2d(-17.4,-16.5)
         glVertex2d(-17.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-22.8,-17)
         glVertex2d(-22,-17)
         glVertex2d(-22.2,-16.8)
         glVertex2d(-22.4,-16.6)
         glVertex2d(-22.8,-16.4)
         glVertex2d(-23.1,-16.5)
         glVertex2d(-23.2,-16.8)
         glVertex2d(-23.5,-17)
         glEnd()
         glBegin(GL_TRIANGLE_FAN)
         glColor3f( 0.0 , 0.0 , 0.0)
         glVertex2d(-27.3,-17)
         glVertex2d(-26.5,-17)
         glVertex2d(-26.7,-16.6)
         glVertex2d(-27,-16.2)
         glVertex2d(-27.3,-16)
         glVertex2d(-27.6,-16.2)
         glVertex2d(-27.7,-16.6)
         glVertex2d(-28,-17)
         glEnd()
         #derecha
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(30,-10)#p1
         glVertex2d(30,-12)#p2
         glVertex2d(29,-12)#p3
         glVertex2d(29,-10)#p4
         glEnd()
         #2
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(26,-10)
         glVertex2d(26,-12)
         glVertex2d(24,-12)
         glVertex2d(24,-10)
         glEnd()
         #3
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(22,-10)
         glVertex2d(22,-12)
         glVertex2d(20,-12)
         glVertex2d(20,-10)
         glEnd()
         #4
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(18,-10)
         glVertex2d(18,-12)
         glVertex2d(16,-12)
         glVertex2d(16,-10)
         glEnd()
         #5
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(14,-10)
         glVertex2d(14,-12)
         glVertex2d(12,-12)
         glVertex2d(12,-10)
         glEnd()
         #6
         glBegin(GL_POLYGON)
         glColor3f(0.674, 0.674, 0.643)
         glVertex2d(10,-10)
         glVertex2d(10,-12)
         glVertex2d(9,-12)
         glVertex2d(9,-10)
         glEnd()
         #FINALIZA LA FIGUIRA 2
        
        







         glFlush()#Dibujar
         glutSwapBuffers()#Dibujar

    def draw_text(self,text, font):
        for c in text:
            glutBitmapCharacter(font, ord(c))


    def texto(self):
        glTranslatef(-5,30,0)
        glColor3f( 1.0,1.0,1.0)
        glRasterPos3f(-0.8, 2.5,1.0)
        #!ERROR DE VS CODE
        self.draw_text("TRIQUITRACATELAS ",GLUT_BITMAP_TIMES_ROMAN_24)
   

class Sonido():
    def musica(self):
        pygame.init()
        pygame.mixer.music.load("castillo.wav")
        pygame.mixer.music.play(3)



inicio=Ddragon()
inicio.ventana()

#cambio para got
#despues del commit
#mas modificaciones
#chanchito triste 
#felipe