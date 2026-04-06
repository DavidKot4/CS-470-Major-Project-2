import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def mySquare():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    glFlush()
    

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mySquare()
        pygame.display.flip()
        pygame.time.wait(10)

main()
    
