import tkinter
from tkinter import Tk
from tkinter import Canvas
import time
import random
snake = [[0, 0]]
eat = [40, 40]
block1 = [200, 360]
block2 = [340, 80]
color = 'blue'
direction = 'right2'
colorized = False
def tick():
    global snake3
    global direction
    global eat
    global eat2
    global count
    global color
    global colorized
    snake2 = snake
    if direction == 'right':
        snake.insert(0, [(snake[0][0])+20, snake[0][1]])
    elif direction == 'left':
        snake.insert(0, [(snake[0][0])-20, snake[0][1]])
    elif direction == 'down':
        snake.insert(0, [(snake[0][0]), snake[0][1]+20])
    elif direction == 'up':
        snake.insert(0, [(snake[0][0]), snake[0][1]-20])
    else:
        snake.insert(0, [snake[0][0], snake[0][1]])
    snake.pop(len(snake)-1)
    if snake[0] == block1 or snake[0] == block2:
        exit()
    if snake[0] == eat:
        r = random.randrange(0, 800, 20)
        r2 = random.randrange(0, 600, 20)
        if not ([r, r2] == block1 or [r, r2] == block2):
            eat = [r, r2]
        else:
            r += 20
            r2 += 20
            eat = [r, r2]
        snake.append(snake[len(snake2)-1])
        c1.delete(eat2)
        eat2 = c1.create_rectangle(eat[0], eat[1], eat[0] + 20, eat[1] + 20, fill='green')
    for i in snake3:
        c1.delete(i)
    snake3 = []
    if colorized:
        color = 'yellow'
    for i in snake:
        if color == 'blue' and colorized:
            color = 'yellow'
        else:
            color = 'blue'
        snake3.append(c1.create_rectangle(i[0], i[1], i[0]+20, i[1]+20, fill=color))
    c1.delete(count)
    count = c1.create_text(35, 20, text=len(snake), fill='white', font=('Courier New', 20))
    tk1.update()
    c1.update()
    for i in snake[1:len(snake)]:
        if i == snake[0] and len(snake)>2:
            exit()
    if snake[0][0] < 0:
        snake[0][0] = 800
    elif snake[0][0] > 780:
        snake[0][0] = -20
    elif snake[0][1] < 0:
        snake[0][1] = 600
    elif snake[0][1] > 580:
        snake[0][1] = -20
def up(event):
    global direction
    if not direction == 'down':
        direction = 'up'
def left(event):
    global direction
    if not direction == 'right':
        direction = 'left'
def down(event):
    global direction
    if not direction == 'up':
        direction = 'down'
def right(event):
    global direction
    if not direction == 'left':
        direction = 'right'
tk1 = Tk()
tk1.title('Snake stargame')
c1 = Canvas(tk1, width=800, height=600)
c1.grid(column=0, row=0)
c1['background'] = 'black'
tk1.bind('<Key-w>', up)
tk1.bind('<Key-a>', left)
tk1.bind('<Key-s>', down)
tk1.bind('<Key-d>', right)
count = c1.create_text(35, 20, text='1', fill='white', font=('Courier New', 20))
block12 = c1.create_rectangle(block1[0], block1[1], block1[0]+20, block1[1]+20, fill='red')
block22 = c1.create_rectangle(block2[0], block2[1], block2[0]+20, block2[1]+20, fill='red')
eat2 = c1.create_rectangle(eat[0], eat[1], eat[0]+20, eat[1]+20, fill='green')
snake3 = [c1.create_rectangle(snake[0][0], snake[0][1], snake[0][0]+20, snake[0][1]+20, fill='blue')]
true = True
while true:
    tick()
    time.sleep(0.1)
tk1.mainloop()

