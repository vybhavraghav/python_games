from tkinter import *
from time import sleep
import random

class Ball:

    def __init__(self, canvas, paddle,scoreboard, color):
        self.canvas = canvas
        self.paddle = paddle
        self.scoreboard = scoreboard

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.speed = 2

    def bounce(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y =self.speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.speed+=0.1
            self.y = -self.speed
            self.scoreboard.updateScore()

        if pos[0] <= 0:
            self.x =self.speed
        if pos[2] >= self.canvas_width:
            self.x = -self.speed

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def bounce(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self, evt):
        self.x = -2
    def turn_right(self, evt):
        self.x = 2

class scoreBoard:

    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(50,470,text = f'Score: {self.score}', fill = "green", font=(14))

    def updateScore(self):
        canvas.delete(self.id)
        self.score += 10
        self.id = canvas.create_text(50,470,text = f'Score: {self.score}', fill = "green" , font=(14))



tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0, bg='black')
canvas.pack()
tk.update()
paddle = Paddle(canvas, 'blue')
score = scoreBoard(canvas)
ball = Ball(canvas, paddle, score, 'red')
while 1:
    if ball.hit_bottom == False:
        ball.bounce()
        paddle.bounce()
        tk.update_idletasks()
        tk.update()
    sleep(0.01)