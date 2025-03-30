import secrets
from enum import Enum, auto
from typing import Callable, NamedTuple


class LSystemType(Enum):
    DETERMINISTIC = auto()
    STOCHASTIC = auto()
    PARAMETRIC = auto()
    CONTEXT_SENSITIVE = auto()


class Shape(NamedTuple):
    axiom: str
    rules: dict[str, str]
    angle: Callable[[], int]
    iterations: int
    step_length: int
    actions: dict[str, str]
    type: LSystemType


koch_curve = Shape(
    axiom="F",
    rules={"F": "F+F-F-F+F"},
    angle=lambda: 90,
    iterations=3,
    step_length=20,
    actions={
        "F": "DRAW_FORWARD",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.DETERMINISTIC
)

sierpinski = Shape(
    axiom="F-G-G",
    rules={
        "F": "F-G+F+G-F",
        "G": "GG",
    },
    angle=lambda: 120,
    iterations=6,
    step_length=10,
    actions={
        "F": "DRAW_FORWARD",
        "G": "DRAW_FORWARD",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.DETERMINISTIC
)

sierpinski_approx = Shape(
    axiom="A",
    rules={
        "A": "B-A-B",
        "B": "A+B+A",
    },
    angle=lambda: 60,
    iterations=6,
    step_length=10,
    actions={
        "A": "DRAW_FORWARD",
        "B": "DRAW_FORWARD",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.DETERMINISTIC
)

dragon = Shape(
    axiom="F",
    rules={
        "F": "F+G",
        "G": "F-G",
    },
    angle=lambda: 90,
    iterations=10,
    step_length=10,
    actions={
        "F": "DRAW_FORWARD",
        "G": "DRAW_FORWARD",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.DETERMINISTIC
)

plant = Shape(
    axiom="X",
    rules={
        "F": "FF",
        "X": "F+[[X]-X]-F[-FX]+X",
    },
    angle=lambda: 25,
    iterations=6,
    step_length=15,
    actions={
        "F": "DRAW_FORWARD",
        "[": "START_BRANCH",
        "]": "END_BRANCH",
        "X": "NOTHING",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.DETERMINISTIC
)

plant_sth = Shape(
    axiom="F",
    rules={
        "F": [
            ("F[+F[+F]F][-F[-F]F]F[+F][-F]", 0.5),
            ("FF-[-F+F+F]+[+F-F-F]", 0.5)
        ]
    },
    angle=lambda: secrets.randbelow(26) + 20,
    iterations=5,
    step_length=25,
    actions={
        "F": "DRAW_FORWARD",
        "[": "START_BRANCH",
        "]": "END_BRANCH",
        "X": "NOTHING",
        "+": "TURN_LEFT",
        "-": "TURN_RIGHT",
    },
    type=LSystemType.STOCHASTIC
)

