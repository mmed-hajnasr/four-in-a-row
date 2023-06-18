import time
from lib.slate import *
import tkinter as tk

class token:

    def __init__(self, window, turn):
        self.position = 0
        self.window = window
        self.turn = turn
        color = "red" if turn == Red_turn else "yellow"
        self.image = window.canvas.create_oval(
            token_positions[0], 10, token_positions[0] + 80, 90, fill=color
        )
        window.canvas.tag_raise(window.board)

        
    def get_coordinates(self):
        return self.window.canvas.coords(self.image)
    
    def move_to(self, index):
        if index < 0 or index >= N:
            return 
        self.position = index
        step = 5 if self.get_coordinates()[0] < token_positions[index] else -5
        while self.get_coordinates()[0] != token_positions[index]:
            current_position = self.get_coordinates()[0]
            if abs(current_position - token_positions[index]) < abs(step):
                self.window.canvas.move(
                    self.image, token_positions[index] - current_position, 0
                )
            else:
                self.window.canvas.move(self.image, step, 0)
            self.window.update()
            time.sleep(0.01)

    def put_down(self,peak):
        if peak == M:
            return
        step = 5
        destination = (M - peak) * 100 + 10
        while self.window.canvas.coords(self.image)[1] != destination:
            self.window.canvas.move(
                self.image,
                0,
                min(destination - self.window.canvas.coords(self.image)[1], step),
            )
            self.window.update()
            time.sleep(0.01)

