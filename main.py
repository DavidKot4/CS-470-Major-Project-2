import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_baseplate():

    #draw main ground plane
    glColor3f(0.2, 0.6, 0.2) # Green
    glBegin(GL_QUADS)
    glVertex3f(-50.0, 0.0, -50.0) # Bottom-left back
    glVertex3f(-50.0, 0.0,  50.0) # Bottom-left front
    glVertex3f( 50.0, 0.0,  50.0) # Bottom-right front
    glVertex3f( 50.0, 0.0, -50.0) # Bottom-right back
    glEnd()
    

def main():
    pygame.init()
    display = (800,600)

    #create pyGame window
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    #enables depth testing of objects
    glEnable(GL_DEPTH_TEST)

    #initialize perspective and camera FOV, aspect ratio, and clipping planes
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    #swap back to ModelView matrix for drawing
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(0.0, 5.0, 20.0,  
                  0.0, 0.0, 0.0,   
                  0.0, 1.0, 0.0)

        draw_baseplate()
        pygame.display.flip()
        pygame.time.wait(10)

    
main()
    
