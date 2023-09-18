from pico2d import *

open_canvas()
hide_lattice()

x = 0

grass = load_image('grass.png')
boy = load_image('character.png')
grass.draw(400,30)
for i in range(0,10):
    for j in range(0,10):
        boy.draw_now(i*80 , j*60)

delay(3)
close_canvas()
