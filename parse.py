## implementation plan:
## - make a dictionary of common commands/implementation functions for them
## - multiple word functions, functions that involve brackets will require a separate function

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
        