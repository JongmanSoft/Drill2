from pico2d import *

open_canvas()
hide_lattice()

grass = load_image('grass.png')
boy = load_image('character.png')
pikachu = load_image('pikachu.png')

i = 10

while(i>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    boy.draw_now((10-i)*80,80)
    pikachu.draw_now(i*80,i*60)
    i = i-1
    delay(0.05)

delay(3)
close_canvas()
