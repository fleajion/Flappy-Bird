from ursina import *

app = Ursina()
Sky()
bird = Animation('assets\img',
                 Collider= 'box',
                 scale=(2,2,2),
                 y=5)
camera.orthographic = True
camera.fov = 20

def update():
    bird.y = bird.y - 4*time.dt
    for p in pipes:
        bird.y = bird.y + 3
    
def inpu(key):
    if key == 'space':
        bird.y = bird.y + 3
        
pipes = []
pipe = Entity(model = 'quad',
              color=color.green,
              texture='white_cube',
              scale=(3,15,1),
              Collider='box')
import random as r
def newPipe():
    y = r.randint(4, 12)
new1 = duplicate(pipe, y=y)
new2 = duplicate(pipe, y=y-22)
pipe2.extend((new1, new2))
invoke(newPipe, delay=5)
newPipe()
app.run()