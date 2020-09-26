# implementation plan:
# - make a dictionary of common commands/implementation functions for them
# - multiple word functions, functions that involve brackets will require a separate function

poly_dict = {
    "square": "^2",
    "squared": "^2",
    "cube": "^3",
    "cubed": "^3",
    "plus": "+",
    "minus": "-",
    "the": "^",
    "second": "2",
    "third": "3",
    "fourth": "4",
    "fifth": "5"
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
}

def polynomial(word_array):
    result = ""
    for i in range(0, len(word_array)):
        raw_str = poly_dict.get(word_array[i], word_array[i])
        if raw_str == "to":
            i += 1
        elif raw_str == "the":
            result += raw_str
        else:
            result += raw_str
    return result

def poly_str(str):
    return polynomial(str.split())

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
        
print(poly_str("2 x to the fourth plus x squared minus x"))
