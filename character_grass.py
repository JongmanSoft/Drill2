from pico2d import *

open_canvas()
hide_lattice()

x = 0

grass = load_image('grass.png')
boy = load_image('character.png')

while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    boy.draw_now(x,90)
    x = x+2
    delay(0.01)

close_canvas()
