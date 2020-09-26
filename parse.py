# implementation plan:
# - make a dictionary of common commands/implementation functions for them
# - multiple word functions, functions that involve brackets will require a separate function
# things that require start/ends: fraction, square root

import re

dict = {
    "square": "^2",
    "squared": "^2",
    "cube": "^3",
    "cubed": "^3",
    "plus": "+",
    "minus": "-",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5",
    "root": "{\\sqrt"
}

matrix_dict = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "to" : "2",
    "too" : "2",
    "three" : "3",
    "four" : "4",
    "for" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
    "sub" : "_",
    "super" : "^",
    "power" : "^",
    "powers" : "^",
    "be" : "b",
    
}


# lower bound is inclusive, upper bound is exclusive
def process(word_array, start_index, end_index):
    result = ""
    i = start_index
    while i < end_index:
        raw_str = dict.get(word_array[i], word_array[i])
        if raw_str == "to" and i + 1 < len(word_array) and word_array[i + 1] == "the":
            result += "^"
            i += 1
        elif raw_str == "fraction":
            j = i + 1
            while j < len(word_array) and word_array[j] != "fraction":
                j += 1
            result += fraction(word_array, i, j)
            i = j
        elif raw_str[0] == '{':
            j = i + 1
            while j < len(word_array) and dict.get(word_array[j]) != raw_str:
                j += 1
            result += single_brace_function(raw_str[1:], word_array, i, j)
            i = j
        else:
            result += raw_str
        i += 1
    return result


def poly_str(str):
    word_array = str.split()
    return process(str.split(), 0, len(word_array))


# word_array[start_index] == "fraction"; end_index = "fraction"
def fraction(word_array, start_index, end_index):
    result = "\\frac{"
    i = start_index
    while i < end_index and word_array[i] != "denominator":
        i += 1
    result += process(word_array, start_index + 1, i) + "}"
    result += "{" + process(word_array, i + 1, end_index) + "}"
    return result


def single_brace_function(term, word_array, start_index, end_index):
    result = term + "{"
    result += process(word_array, start_index + 1, end_index) + "}"
    return result


def parse(str):
    return poly_str(str)


def matrix_parse(str):
    result = "\\begin{pmatrix}\n"
    word_array = re.findall(r"[\w']+", str)

    newRow = True

    for i in range(0 ,len(word_array)):
        if (word_array[i].lower() == "element" and not newRow):
            result += " & "
        elif (word_array[i].lower() == "element"):
            newRow = False
            result += "    "
        elif (word_array[i].lower() == "row" or word_array[i].lower() == "roll"):
            newRow = True
            result += "\\\\\n"
        else:
            result += matrix_dict.get(word_array[i].lower(), word_array[i].lower())
    
    result += "\n\\end{pmatrix}"

    return result


print(poly_str("x minus 1 plus fraction 2 x to the fourth plus root x root minus x denominator x plus 3 fraction"))
