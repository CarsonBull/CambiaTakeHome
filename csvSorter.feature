# Gherkins file to define the behavior of the csvSorter.py program
# Cases that shoudl be tested:
# Normal(input.csv is there and seemingly random), perfect order, backwards, duplicate words,
# Capitalization, weird chars, blank spots(ie ,,), no file, nothing in file, command line arguments
# are present, No line ending, output.csv is already present, spaces, failure while sorting

Feature: Normal Sorting (No file issues. Might have issues, or edge cases in the file)

  Scenario: File run with "this,is,a,test\n"
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on input.csv with "this,is,a,test\n"
    Then output.csv file contains "this,test,is,a\n"

  Scenario: Run on an already sorted csv
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "z,d,a\n"
    Then output.csv contains the exact same text

  Scenario: Run on a reverse sorted csv
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "a,d,z\n"
    Then output.csv contains "z,d,a\n"

  Scenario: Run on a csv with duplicates
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "a,f,d,f,z\n"
    Then output.csv contains "z,f,f,d,a\n"

  Scenario: Run on a csv with mixed capitalization
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "a,A,z\n"
    Then output.csv contains "z,A,a\n"

  Scenario: Run on a csv with unordinary unicode characters
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "a,℮,d,z\n"
    Then output.csv contains "z,d,a\n"

  Scenario: Run on a csv with no characters
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing ""
    Then output.csv contains "\n"

  Scenario: Run on a csv with no line ending
    Given user has built the docker container and is ready to run.
    When the user runs csvSorter.py on the input.csv containing "z,d,f,a,q"
    Then output.csv contains "\n"
