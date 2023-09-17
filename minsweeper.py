import turtle as t

import math


import random

t.screensize(720, 720)

t.speed(0)

t.shape('square')

t.resizemode("user")

t.penup()

t.shapesize(4, 4, 0)

t.ht()

user = [[0 for _ in range(9)] for _ in range(9)]
bomb = [[0 for _ in range(9)] for _ in range(9)]

color = ['#fff', '#00f', '#8f8', '#f88', '#008', '#800', "#88f"]

for j in range(9):
    for i in range(9):
        t.color('gray')
        t.goto(80*i-360, 80*j-360)
        t.stamp()


def click(mouse_x, mouse_y):
    mouse_r = math.floor((mouse_y+400)/80)
    mouse_c = math.floor((mouse_x+400)/80)

    if (mouse_x < -360 or mouse_x >= 360 or mouse_y < -360 or mouse_y >= 360):
        return
    if bomb[mouse_r][mouse_c] == 1:
        for j in range(9):
            for i in range(9):
                t.goto(80*i-360, 80*j-360)
                if bomb[j][i] == 1:
                    t.color('#000')
                    t.shape('circle')
                    t.stamp()
        return

    board = [[-1 for _ in range(9)] for _ in range(9)]
    if not any([any(row) for row in user]):
        bomb[mouse_r][mouse_c] = 1

        def set_bomb():
            a = random.randint(0, 8)
            b = random.randint(0, 8)
            if bomb[b][a] == 1:
                set_bomb()
            bomb[b][a] = 1
        for _ in range(10):
            set_bomb()
        bomb[mouse_r][mouse_c] = 0
    user[mouse_r][mouse_c] = 1

    def check8(x, y):
        count = 0
        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if 0 <= n+y < 9 and 0 <= m+x < 9:
                    if bomb[n+y][m+x] == 1:
                        count += 1
        board[y][x] = count
        if board[y][x] == 0:
            for nn in [-1, 0, 1]:
                for mm in [-1, 0, 1]:
                    if 0 <= nn+y < 9 and 0 <= mm+x < 9:
                        if board[nn+y][mm+x] == -1:
                            check8(mm+x, y+nn)

    for y in range(9):
        for x in range(9):
            if user[y][x] == 1:
                check8(x, y)
    for j in range(9):
        for i in range(9):
            t.color(('gray' if board[j][i]
                    == -1 else color[board[j][i]]))
            t.goto(80*i-360, 80*j-360)
            t.stamp()


t.onscreenclick(click, btn=1)
t.done()
