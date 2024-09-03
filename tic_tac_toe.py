import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = []
        self.current_player = "X"
        self.winner = False
        self.label = None
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [tk.Button(self.root, text="", font=("normal",25), width=6, height=2, command=lambda i=i: self.button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("normal", 16))
        self.label.grid(row=3, column=0, columnspan=3)

    def check_winner(self):
        for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if self.buttons[combo[0]]["text"] == self.buttons[combo[1]]["text"] == self.buttons[combo[2]]["text"] != "":
                self.buttons[combo[0]].config(bg="green")
                self.buttons[combo[1]].config(bg="green")
                self.buttons[combo[2]].config(bg="green")
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.buttons[combo[0]]['text']} wins!")
                self.root.quit()

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.winner:
            self.buttons[index]["text"] = self.current_player
            self.check_winner()
            self.toggle_player()
            self.computer_move()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s turn")

    def computer_move(self):
        empty_buttons = [i for i, button in enumerate(self.buttons) if button["text"] == ""]
        if empty_buttons:
            index = random.choice(empty_buttons)
            self.buttons[index]["text"] = "O"
            self.check_winner()
            self.toggle_player()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
