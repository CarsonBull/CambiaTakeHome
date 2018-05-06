# Gherkins file to define the behavior of the csvSorter.py program
# Cases that shoudl be tested:
# Normal(input.csv is there and seemingly random), perfect order, backwards, duplicate words,
# Capitalization, weird chars, blank spots(ie ,,), no file, nothing in file, command line arguments
# are present, No line ending, output.csv is already present, spaces, failure while sorting

Feature: Normal Sorting (No file issues. Might have issues, or edge cases in the file)

  Background: The user has built the docker container and is ready to run with an imput.csv

  Scenario: File run with normal constraints
    Given the csv contains "this,is,a,test\n"
    When the user runs csvSorter.py
    Then output.csv file contains "this,test,is,a\n"

  Scenario: Run on an already sorted csv
    Given the csv contains "z,d,a\n"
    When the user runs csvSorter.py
    Then output.csv contains the exact same text

  Scenario: Run on a reverse sorted csv
    Given the csv contains "a,d,z\n"
    When the user runs csvSorter.py
    Then output.csv contains "z,d,a\n"

  Scenario: Run on a csv with duplicates
    Given the csv contains "a,f,d,f,z\n"
    When the user runs csvSorter.py
    Then output.csv contains "z,f,f,d,a\n"

  Scenario: Run on a csv with mixed capitalization
    Given the csv contains "a,A,z\n"
    When the user runs csvSorter.py
    Then output.csv contains "z,a,A\n"

  Scenario: Run on a csv with unordinary unicode characters
    Given the csv contains "a,℮,d,z\n"
    When the user runs csvSorter.py
    Then all words with nonalphabetic characters will be dropped
    And the output.csv contains "z,d,a\n"

    Examples:
    TODO: decide whether to remove anything that has a non alpha numeric char or just if its sorted based on it

  Scenario: Run on a csv with no characters
    Given the csv contains ""
    When the user runs csvSorter.py
    Then output.csv contains "\n"
    But print "No words to sort" to standard err

  Scenario: Run on a csv with no line ending
    Given the csv contains "z,d,f,a,q"
    When the user runs csvSorter.py
    Then output.csv contains "\n"
    But print "No line ending" to stderr

  Scenario: Run on a csv with spaces in words
    Given the csv contains "a,z,d a,p, x\n"
    When the user runs csvSorter.py
    Then the output will remove leading spaces and treat words with spaces as one word

    Examples:
    |Keyword       |Result       |
    |" a,b a,b,z\n"|"z,b a,b,a\n"|
    |"ab c,abd\n"  |"abd,ab c\n" |

  Scenario: Run on a csv with numbers in words
    Given the csv contains "1,z,a1,a\n"
    When the user runs csvSorter.py
    Then numerics will be given the highest priority
    And the output will be "z,a1,a,1\n"

  Scenario: Run on a csv with puncuation in words, excluding commas
    Given the csv contains "z,a,.,a.,A!\n"
    When the user runs csvSorter.py
    Then all words containing punctuation will be dropped



