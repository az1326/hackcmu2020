# implementation plan:
# - make a dictionary of common commands/implementation functions for them
# - multiple word functions, functions that involve brackets will require a separate function
# things that require start/ends: fraction, square root

def fraction(word_array):
    result = ""
    return result


poly_dict = {
    "square": "^2",
    "squared": "^2",
    "cube": "^3",
    "cubed": "^3",
    "plus": "+",
    "minus": "-",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5"
}


# just call it simply
def process(word_array):
    result = ""
    for i in range(0, len(word_array)):
        raw_str = poly_dict.get(word_array[i], word_array[i])
        if raw_str == "to" and i + 1 < len(word_array) and word_array[i + 1] == "the":
            result += "^"
        else:
            result += raw_str
    return result


def poly_str(str):
    return process(str.split())


dictionary = {
    "times": "\\times"

}


def parse(str):
    result = ""
    word_array = str.split()

    # some phrases are multiple words long, so we can't naively process word by word
    for i in range(0, len(word_array)):
        result += dictionary.get(word_array[i], word_array[i]) + " "

    return result


def matrix_parse(str):
    result = "\\begin{pmatrix}\n"
    word_array = str.split()

    newRow = True

    for i in range(0 ,len(word_array)):
        if (word_array[i] == "element" and not newRow):
            result += " & "
        elif (word_array[i] == "element"):
            newRow = False
            result += "    "
        elif (word_array[i] == "row" or word_array[i] == "roll"):
            newRow = True
            result += "\\\\\n"
        else:
            result += word_array[i]
    
    result += "\n\\end{pmatrix}"

    return result
        
print(poly_str("2 x to the fourth plus x squared minus x"))
