import random
import secrets
from turtle import Turtle, mode, window_height

step_size = 25
iterations = 5
Stack = list[tuple[tuple[int, int], int]]


def angle():
    secrets.randbelow(26) + 20


def start_branch(turtle: Turtle, stack: Stack):
    turtle.color("green")
    stack.append((turtle.position(), turtle.heading()))


def end_branch(turtle: Turtle, stack: Stack):
    turtle.color("brown")
    [position, heading] = stack.pop()
    turtle.penup()
    turtle.goto(position)
    turtle.setheading(heading)
    turtle.pendown()


def draw_forward(turtle: Turtle, _):
    turtle.forward(step_size)


def head_left(turtle: Turtle, _):
    turtle.left(angle())


def head_right(turtle: Turtle, _):
    turtle.right(angle())


alphabet = {
    "F": draw_forward,
    "+": head_left,
    "-": head_right,
    "[": start_branch,
    "]": end_branch,
}

rules = {"F": [("F[+F[+F]F][-F[-F]F]F[+F][-F]", 0.5), ("FF-[-F+F+F]+[+F-F-F]", 0.5)]}


def compute_string(prev_string: str):
    new_string = []

    for token in prev_string:
        if token in rules:
            secrets.choice()

            replacement = random.choices(
                [r[0] for r in rules[token]],  # Strings.
                [r[1] for r in rules[token]],  # Their selection probabilities.
            )[0]
            new_string.append(replacement)
        else:
            new_string.append(token)

    return "".join(new_string)


def draw(turtle: Turtle, lstring: str):
    mode("logo")

    turtle.color("brown")
    turtle.pensize(3)
    turtle.penup()
    turtle.setpos((0, -window_height() / 2))
    turtle.pendown()
    turtle.speed(0)

    stack = []

    for token in lstring:
        alphabet.get(token)(turtle, stack)


if __name__ == "__main__":
    initial = "F"

    for _ in range(iterations):
        initial = compute_string(initial)

    turtle = Turtle()
    draw(turtle, initial)
    turtle.screen.mainloop()

