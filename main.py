from typing import Callable, List
from shapes import Shape, koch_curve, sierpinski, sierpinski_approx, plant
from turtle import Turtle, mode, window_height


class Interpreter:
    def render(self, shape: Shape):
        turtle = Turtle()
        current_string = shape.axiom
        alphabet = self.__create_alphabet(shape)

        for _ in range(shape.iterations):
            current_string = self.__build_string(shape, current_string)

        self.__setup_turtle(turtle)
        self.__draw(turtle, shape, alphabet, current_string)
        turtle.screen.mainloop()

    def __create_alphabet(
        self, shape: Shape
    ) -> dict[str, Callable[[Turtle, Shape, List], None]]:
        alphabet = {}

        for variable, action in shape.actions.items():
            match action:
                case 'DRAW_FORWARD':
                    alphabet[variable] = self.__draw_forward
                case 'MOVE_FORWARD':
                    alphabet[variable] = self.__move_forward
                case 'TURN_LEFT':
                    alphabet[variable] = self.__turn_left
                case 'TURN_RIGHT':
                    alphabet[variable] = self.__turn_right
                case 'START_BRANCH':
                    alphabet[variable] = self.__start_branch
                case 'END_BRANCH':
                    alphabet[variable] = self.__end_branch
                case 'NOTHING':
                    alphabet[variable] = lambda *args: None
                case _:
                    print(f'Unrecognized action "{action}" for variable "{variable}"!')
                    continue

        return alphabet

    def __start_branch(self, turtle, shape, stack):
        stack.append((turtle.position(), turtle.heading()))

    def __end_branch(self, turtle, shape, stack):
        [position, heading] = stack.pop()
        turtle.penup()
        turtle.goto(position)
        turtle.setheading(heading)
        turtle.pendown()

    def __turn_left(self, turtle, shape, stack):
        turtle.left(shape.angle)

    def __turn_right(self, turtle, shape, stack):
        turtle.right(shape.angle)

    def __draw_forward(self, turtle, shape, stack):
        turtle.forward(shape.step_length)
        
    def __move_forward(self, turtle, shape, stack):
        turtle.penup()
        turtle.forward(shape.step_length)
        turtle.pendown()

    def __build_string(self, shape: Shape, prev_string: str):
        return ''.join([shape.rules.get(token, token) for token in prev_string])

    def __setup_turtle(self, turtle: Turtle):
        mode('logo')

        turtle.color('green')
        turtle.pensize(3)
        turtle.penup()
        turtle.setpos((0, -window_height() / 2))
        turtle.pendown()
        turtle.speed(0)

    def __draw(
        self,
        turtle: Turtle,
        shape: Shape,
        alphabet: dict[str, Callable[[Turtle, Shape, List], None]],
        lsys_string: str,
    ):
        stack = []

        for token in lsys_string:
            executor = alphabet.get(token)

            if executor is not None:
                executor(turtle, shape, stack)


def main():
    interpreter = Interpreter()

    try:
        interpreter.render(plant)
    except KeyboardInterrupt:
        print('Bye.')
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
