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


print(poly_str("2 x to the fourth plus x squared minus x"))