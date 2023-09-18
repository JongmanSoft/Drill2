from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

shape = 0
dir = 0
x = 40
y = 80
i = 0
while(1):
    clear_canvas_now()
    update_canvas()
    grass.draw_now(400,30)
    if (shape == 0):
        if (dir == 0):
            x = x+5
            delay(0.01)
            if (x>695):
                dir = 1
        if (dir == 1):
            y = y+5
            delay(0.01)
            if (y > 495):
                dir = 2
        if (dir == 2):
            x = x-5
            delay(0.01)
            if (x < 45):
                dir =3
        if (dir == 3):
            y = y-5
            delay(0.01)
            if (y < 85):
                dir =0
                shape = 1
    else : 
        i = i+2
        x = math.cos(math.radians(i)) * 200 +300
        y = math.sin(math.radians(i)) *200 + 300
        delay(0.01)
        if (i >360):
            i =0
            shape = 0
            x = 40
            y = 80
    boy.draw_now(x,y)
            
        

