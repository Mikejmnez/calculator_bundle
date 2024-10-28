from adder import add
from multiplier import multiply

def calculate(a: float, b: float) -> dict:
    return {
        "addition": add(a, b),
        "multiplication": multiply(a, b)
    }