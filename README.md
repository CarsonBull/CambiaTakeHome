Name: Alex Carson Bull  
Email: Carson.Bull@gmail.com  
About: This project allows a user to build a Docker container
and then run a Python program that will sort a comma separated 
CSV file into descending alphabetical order. Along with the 
program there is a Gherkin test suite to outline the 
functionality of the program. The gherkin file does not 
actually run but should give a comprenhensive look at 
the functionality.  


DOCKER: To build the Dockerfile you could use a volume to 
allow for the input.csv to be modified and see the changes.  

Sample build and run:  
sudo docker build -t <containerName> .  
sudo docker run <containerName>  

Note: The docker container currently will contain the output file
in the container. I am not sure of a way to transfer it out because
a volume will make the output file exist when the container is run 
and after the container exits I'm unsure of a way to cp it out.
There are two lines in the python commented out to print the output  


Gherkins: The csvSorter.feature file defines the test cases and how they
should act. It does not provide actual running code.  


Files:  
README.md  
DockerFile  
csvSorter.feature  
.gitignore  
/src/  
  csvSorter.py  
  test_csvSorter.py  
  testFile.csv  
  testimput.csv  
  

