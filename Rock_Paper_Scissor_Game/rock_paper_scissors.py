import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.resizable(False, False)

# Load images for Rock, Paper, and Scissors
rock_img = ImageTk.PhotoImage(Image.open("Rock_Paper_Scissor_Game/pictures/rock.jpg").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("Rock_Paper_Scissor_Game/pictures/paper.jpg").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("Rock_Paper_Scissor_Game/pictures/scissors.jpg").resize((100, 100)))

# Scores Initialization
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    computer_label.config(image=get_choice_image(computer_choice))

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1
    
    update_score_labels()

# Function to update and keep track of scores
def update_score_labels():
    user_score_label.config(text="Your Score: " + str(user_score))
    computer_score_label.config(text="Computer's Score: " + str(computer_score))

# Function to compare the User's Choice and Computer's Random choice
def get_choice_image(choice):
    if choice == "rock":
        return rock_img
    elif choice == "paper":
        return paper_img
    else:
        return scissors_img

user_label = tk.Label(root, text="Your Choice")
user_label.pack()

rock_button = tk.Button(root, image=rock_img, command=lambda: play_game("rock"))
paper_button = tk.Button(root, image=paper_img, command=lambda: play_game("paper"))
scissors_button = tk.Button(root, image=scissors_img, command=lambda: play_game("scissors"))

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)

computer_label = tk.Label(root, text="Computer's Choice")
computer_label.pack()

result_label = tk.Label(root, text="Result")
result_label.pack()

user_score_label = tk.Label(root, text="Your Score: 0")
user_score_label.pack()

computer_score_label = tk.Label(root, text="Computer's Score: 0")
computer_score_label.pack()

root.mainloop()