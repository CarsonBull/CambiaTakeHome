
def main():
    print("This is a test")



def get_line(fileName):
    '''This function accepts a filename of a CSV file that has atleast one line ending in a newline. The first line is returned with the trailing newline otherwise it returns none. It also raises a type error if the filename is not a string or an IOerror if the file does not exist'''

    if type(fileName) != str:
        raise ValueError("This function accepts a string filename") 

    with open(fileName) as csvFile:
        line = csvFile.readline()

    if line[-1] == '\n':
        return line
    return none


def get_words(line):
    '''The get_words function takes a string that is seperated by commas and ends in a newline and returns a list of the words. This can then be processed in many different ways. It will throw a value error if the input is not a string'''

    runningList = []
    wordStart = 0
    badWord = False

    # i is the current position of the marker in the list. 
    # It increments through and will act as the end position(i because it doesnt include itself) for
    # a word as well as set the start position for a new word(i+1). 
    # This allows the entire string to be added to the list at once 
    # and not make new strings for every character

    for i in range(len(line)):
        currentChar = line[i]  
        if currentChar == ',' or currentChar == '\n':
            if wordStart == i or badWord:
                wordStart = i + 1
                badWord = False
                continue
            runningList.append(line[wordStart:i])
            wordStart = i + 1
        elif badWord:
            continue
        elif not (currentChar.isalpha() or currentChar.isdigit() or currentChar.isspace()):
            badWord = True

    return runningList


if __name__ == "__main__":
  main("input.csv")
