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


print(parse("V times W"))