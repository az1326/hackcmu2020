# TO DO LIST
# nesting multiple of the same functions -- frac inside frac, for example
# do we want to get rid of fraction/single-bracket-things and just let the user specify where to put brackets?
# test with more functions -- not sure what else is required?
# start thinking about text and math mode

from dictionary import search


# lower bound is inclusive, upper bound is exclusive
def process(word_array, start_index, end_index):
    result = ""
    i = start_index
    while i < end_index:
        #raw_arr = dictionary.get(word_array[i], [word_array[i]])
        raw_arr = search(word_array[i])
        word_flag = False
        for raw_str in raw_arr:
            if isinstance(raw_str, list):
                flag = True
                for j in range(0, len(raw_str) - 1):
                    if i + j + 1 >= end_index or word_array[i + j + 1] != raw_str[j]:
                        flag = False
                        break
                if flag:
                    result += raw_str[len(raw_str) - 1]
                    i += len(raw_str) - 1
                    word_flag = True
                    break
            elif raw_str == "fraction":
                j = i + 1
                while j < len(word_array) and word_array[j] != "fraction":
                    j += 1
                result += fraction(word_array, i, j)
                i = j
                word_flag = True
                break
            elif raw_str == "matrix":
                j = i + 1
                while j < len(word_array) and word_array[j] != "matrix":
                    j += 1
                result += matrix(word_array, i+1, j)
                i = j
                word_flag = True
                break
            else:
                result += raw_str
                if len(raw_str) > 2:
                    result += ' '
                word_flag = True
        if not word_flag:
            result += word_array[i]
            if len(word_array[i]) > 2:
                result += ' '
        i += 1
    return result


# word_array[start_index] == "fraction"; end_index = "fraction"
def fraction(word_array, start_index, end_index):
    result = "\\frac{"
    i = start_index
    while i < end_index and word_array[i] != "denominator":
        i += 1
    result += process(word_array, start_index + 1, i) + "}"
    result += "{" + process(word_array, i + 1, end_index) + "}"
    return result


def matrix(word_array, start_index, end_index):
    result = "\n\\begin{pmatrix}\n"
    newRow = True

    i = start_index
    while i < end_index:
        if (word_array[i].lower() == "element"):
            if (newRow):
                result += "    "
                newRow = False
            else:
                result += " & "

            j = i + 1
            while (j < end_index and word_array[j].lower() != "element" and word_array[j].lower() != "row" and word_array[j].lower() != "roll"):
                j += 1
            result += process(word_array, i+1, j)
            i = j
        elif (word_array[i].lower() == "row" or word_array[i].lower() == "roll"):
            result += "\\\\\n"
            newRow = True
            i += 1
        else:
            result += word_array[i]
            i+=1
    
    result += "\n\\end{pmatrix}"

    return result


def parse(arg_str):
    word_array = arg_str.split()
    return process(word_array, 0, len(word_array))


print(parse("4 times square root 2 square close"))
