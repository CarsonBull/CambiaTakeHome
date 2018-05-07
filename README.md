# Cambia Take Home Question
This project implements a CSV sorter that sorts a comma deliminated csv file in reverse alphabetic order.  
#### Name: Alex Carson Bull  
Email: Carson.Bull@gmail.com  
About: 
This project allows a user to build a Docker container
and then run a Python program that will sort a comma separated 
CSV file into descending alphabetical order. Along with the 
program there is a Gherkin test suite to outline the 
functionality of the program. The gherkin file does not 
actually run but should give a comprenhensive look at 
the functionality.  


#### DOCKER: 
To build the Dockerfile you could use a volume to 
allow for the input.csv to be modified and see the changes.  

##### Sample build and run:  
sudo docker build -t <containerName> .  
sudo docker run <containerName>  

##### Note: 
The docker container currently will contain the output file
in the container. I am not sure of a way to transfer it out because
a volume will make the output file exist when the container is run 
and after the container exits I'm unsure of a way to cp it out.
There are two lines in the python commented out to print the output  


#### Gherkins: 
The csvSorter.feature file defines the test cases and how they
should act. It does not provide actual running code.  

#### Testing:
The python portion on this project comes with a built-in unit test 
framework. It tests all the functions in the csvSorter.py file and 
makes sure that they will run according to the spec provided and 
handles all of the scenarios in the Gherkins feature file.

##### Running Tests:
To run the unit test change the docker CMD to be:  
'CMD ["python3" , "-m", "unittest", "test_csvSorter.py"]  


#### Files:  
README.md  
DockerFile  
csvSorter.feature  
.gitignore  
/src/  
&nbsp;&nbsp; csvSorter.py  
&nbsp;&nbsp; test_csvSorter.py  
&nbsp;&nbsp; testFile.csv  
&nbsp;&nbsp; testimput.csv  
  

