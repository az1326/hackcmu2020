import math

symbols_dict = {
    "less than or equal to": "\leq",
    "geater than or equal to": "\geq",
    "not equal to": "\\neq",
    "times": "\\times",
    "integer divided by": "\div",
    "plus or minus": "\pm",
    "infinity": "\infty",
    "pie": "\pi",
    "theta": "\\theta",
    "approximately": "\\approx",
    "two": "2"
    
}

def mathSymbolsGeneral(math_array):
    
    for n in range (0, len(math_array)):
        baseString = symbols_dict(math_array[n])
        print(baseString)

print(mathSymbolsGeneral)
