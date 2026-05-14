"""
Turtle Memory Challenge

Watch the turtle draw a path, then recreate it from memory!
"""

import random
import time
import turtle

STEP_SIZE = 10
MIN_STEPS = 6
MAX_STEPS = 10
SHOW_SPEED = 1


# ==> TASK 1: Change this value to make the path shorter or longer.
NUMBER_OF_MOVES = 8


# ==> TASK 2: Change this value to pick how long the path is shown before clear.
SHOW_TIME_MS = 1200


# ==> TASK 3: Stop the path from going too close to the window edge.
# Tip: add checks before moving, and pick a safer move when needed.


# ==> TASK 4: Improve grading so distance and turn direction both matter.
# Tip: compare each user move to the matching computer move.


# ==> TASK 5: Add a second round and keep a total score.


computer_moves = []
user_moves = []


screen = turtle.Screen()
screen.title("Turtle Memory Challenge")
screen.setup(width=800, height=600)

artist = turtle.Turtle()
artist.shape("turtle")
artist.color("green")
artist.pensize(3)
artist.speed(SHOW_SPEED)

helper = turtle.Turtle()
helper.hideturtle()
helper.penup()
helper.goto(-380, 260)


def write_message(text):
    helper.clear()
    helper.write(text, font=("Arial", 14, "normal"))


def make_computer_path():
    """Create and draw the path that the player must remember."""
    artist.clear()
    artist.penup()
    artist.goto(0, 0)
    artist.setheading(0)
    artist.pendown()

    computer_moves.clear()

    move_count = NUMBER_OF_MOVES
    if move_count < MIN_STEPS:
        move_count = MIN_STEPS
    if move_count > MAX_STEPS:
        move_count = MAX_STEPS

    for _ in range(move_count):
        turn = random.choice([-90, 0, 90])
        distance = random.choice([10, 20, 30, 40, 50])

        if turn == -90:
            artist.left(90)
            computer_moves.append("L")
        elif turn == 90:
            artist.right(90)
            computer_moves.append("R")

        artist.forward(distance)
        computer_moves.append(f"F{distance}")


def start_player_turn():
    """Clear and let the user try to redraw the path."""
    artist.clear()
    artist.penup()
    artist.goto(0, 0)
    artist.setheading(0)
    artist.pendown()

    user_moves.clear()

    write_message(
        "Enter moves in pop-ups: F=forward 10, L=left, R=right, X=finish"
    )


def score_attempt():
    """Simple score: compare matching moves in order."""
    matches = 0
    total = len(computer_moves)

    limit = min(len(computer_moves), len(user_moves))
    for i in range(limit):
        if computer_moves[i] == user_moves[i]:
            matches += 1

    if total == 0:
        percent = 0
    else:
        percent = int((matches / total) * 100)

    return matches, total, percent


def collect_player_moves():
    """Collect user commands through text input dialogs."""
    while True:
        entry = screen.textinput(
            "Your Move",
            "Type F (forward 10), L (left), R (right), or X (finish):",
        )

        if entry is None:
            return

        command = entry.strip().upper()

        if command == "F":
            artist.forward(STEP_SIZE)
            user_moves.append(f"F{STEP_SIZE}")
        elif command == "L":
            artist.left(90)
            user_moves.append("L")
        elif command == "R":
            artist.right(90)
            user_moves.append("R")
        elif command == "X":
            return


def play_round():
    write_message("Watch the path carefully...")
    make_computer_path()
    time.sleep(SHOW_TIME_MS / 1000)

    start_player_turn()
    collect_player_moves()

    matches, total, percent = score_attempt()
    write_message(f"Score: {matches}/{total} moves matched ({percent}%).")


def game_loop():
    while True:
        play_round()
        again = screen.textinput("Play Again", "Play another round? (y/n)")
        if again is None or again.strip().lower() != "y":
            write_message("Thanks for playing!")
            break


if __name__ == "__main__":
    game_loop()
