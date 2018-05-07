import sys


def order_CSV(inputFileName, outputFileName):
    '''This function reads a comme delinated file of words with a newline at the end of the first line. It takes all of the words up to the first line and orders them before outputting them to the outputFileself.
    If the output file already exists it will exit after printing to standard error. Any words that contain nonaplhanumeric characters or spaces will be dropped for the output file. If there are any errors they will be raised as IOErrors or ValueErrors.'''

    line = get_line(inputFileName)
    if line == None:
        exit()

    words = get_words(line)

    sortedWords = sort_words(words)

    output_CSV(outputFileName, sortedWords)




def get_line(fileName):
    '''This function accepts a filename of a CSV file that has atleast one line ending in a newline. The first line is returned with the trailing newline otherwise it returns none. It also raises a type error if the filename is not a string or an IOerror if the file does not exist'''

    if type(fileName) != str:
        raise ValueError("This function accepts a string filename")

    with open(fileName) as csvFile:
        line = csvFile.readline()
        if csvFile.readline() != '':
            print("Multiline file. Please Try again with a single line file.", file=sys.stderr)
            return None


    if line[-1] == '\n':
        return line
    print("No carriage return", file=sys.stderr)
    return None


def get_words(line):
    '''The get_words function takes a string that is seperated by commas and ends in a newline and returns a list of the words. This can then be processed in many different ways. It will throw a value error if the input is not a string'''

    if type(line) != str:
        raise ValueError("The input to get_words should be a string")

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


def sort_words(wordList):
    '''sort_words takes a list of words that have been taken from a file and does a simple decending alphabetic merge sort on them'''
    if type(wordList) != list:
        raise ValueError("A list is requird for this function to work")

    # the first two if and elif statements are base cases and stop the recursive program eventually
    if len(wordList) < 2:
        return wordList
    elif len(wordList) == 2:
        if compare_words(wordList[0],wordList[1]):
            return wordList
        else:
            return [wordList[1],wordList[0]]

    else:
        # This section takes a list and divides it in half then passes it down to be sorted
        middlePos = len(wordList)//2
        leftHalf = sort_words(wordList[:middlePos])
        rightHalf = sort_words(wordList[middlePos:])

        sortedWords = []
        leftPos = 0
        leftLen = len(leftHalf)
        rightPos = 0
        rightLen = len(rightHalf)


        # once both sides of the sorted list come back it goes through and figures 
        # out which word at the front of the list should go in which position and adds it to sortedWords
        # If one list has been emptied then if automatically takes the word 
        # from the other list.
        for i in range(len(wordList)):
            if leftPos >= leftLen:
                sortedWords.append(rightHalf[rightPos])
                rightPos += 1
            elif rightPos >= rightLen:
                sortedWords.append(leftHalf[leftPos])
                leftPos += 1
            elif compare_words(leftHalf[leftPos],rightHalf[rightPos]):
                sortedWords.append(leftHalf[leftPos])
                leftPos += 1
            else:
                sortedWords.append(rightHalf[rightPos])
                rightPos += 1

        return sortedWords

def compare_words(leftWord, rightWord):
    '''This function returns True if the leftWord should be before the right word in a reverse alphabetic order. Otherwise it returns False and ther rightWord sould come first'''
    # I made the choice to use pythins builtin min function for comparing words
    # This is a very complicated issue that will allow the system to handle
    # more advanced unicode words in the future if necessary

    if type(leftWord) != str or type(rightWord) != str:
        raise ValueError("Both words need to be strings")

    if min(leftWord, rightWord) == leftWord:
        return False
    else:
        return True

def output_CSV(outputFileName, outputList):
    '''The output_CSV function takes a list of words and outputs them to a file with commas seperating each word. The end of the line will be signified by a newline character. No other content should exist beyond this. If the file already exists an IOError will be raised and nothing will be writte to the outout file. If a list contains something other than strign the behavior is undefined.'''

    if type(outputFileName) != str:
        raise ValueError("File name is not of type str")

    if type(outputList) != list:
        raise ValueError("outputList should be of type list")

    # Tries to open the file for reading. If it exists then we escape the try except and raise an IOException.
    # If the file does not exist we have an IOError runs the exception block. In the exception block we write
    # the contents to the file and return before the IOError is raised from the prior read.
    try:
        readFile = open(outputFileName, 'r')
        readFile.close()
    except:
        with open(outputFileName, 'w') as outputFile:
            for i in range(len(outputList)):
                outputFile.write(outputList[i])
                if i < len(outputList)-1:
                    outputFile.write(',')

            outputFile.write('\n')
        return

    raise IOError("Output file already exists")

if __name__ == "__main__":
    try:
        order_CSV("input.csv","output.csv")
        # Uncomment the lower two lines if you would like the output to be printed to the screen
        # with open("output.csv") as out:
        #     print(out.readline())
    except Exception as e:
        print(e, file=sys.strerr)
