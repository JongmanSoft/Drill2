from pico2d import *

open_canvas()
hide_lattice()

grass = load_image('grass.png')
boy = load_image('character.png')
pikachu = load_image('pikachu.png')

grass.draw_now(400,30)
boy.draw_now(400,80)
pikachu.draw_now(100,120)

delay(3)
close_canvas()
