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
  

Questions:

Tools
1.	Pros: Git is an amazing way to manage projects from several 
	different perspectives. It allow multiple people to be 
	working on functioning versions of a project at once and 
	still keep the older versions. By branching it creates a 
	workflow that can all build back into a central deployment branch.
	Cons: Pros: Git is an amazing way to manage projects from 
	several different perspectives. It allow multiple people to 
	be working on functioning versions of a project at once and 
	still keep the older versions. By branching it creates a 
	workflow that can all build back into a central deployment branch.
2. 	Pros: Docker make deployment of project seamless and easy. 
	It builds containers that have the core modules that you 
	need for your project. It also works on the kernel level 
	so it is ultra fast. When you use this for multiple 
	different employees you also get added benefits. All the 
	employees are running their code in the exact same Docker 
	environment so they won’t have issues running like 
	they are different machines. 
3.	Choosing a language can depend on a lot of different things. 
	In the owrk enviroment it can be dictated by having people 
	work on a more common language that the entire team knows or 
	something that is good for the project. Languages often end 
	up being heavily used for specific tasks(Python for science 
	stuff, Java for entaprise, C for embedded, etc) and so you 
	have teams built around knowledge sets. This increases 
	collaboration and knowledge of the codebase in general. For 
	this project I picked Python because of the fact that I am 
	learning new skills in other areas. I feel super confident 
	in Python but have a limited knowledge of Docker and no 
	knowledge of Cucumber Gherkin. I plan to spend more time on 
	those areas and use python to save time.

Methodologies
1.	TODO: Compose my thoughts and come back to this.
2.	As a QA person I would most likely evaluate someone else's 
	code so I am going to want to spend those two weeks becoming 
	familiar with it. I would probably break my time down into 
	chunks. Day 1 is going to be based around finding the tools 
	that the team is using to develop the project and doing light 
	research. The following few days are going to be diving into 
	code and seeing where the critical failures are going to be...
	TODO: Fisnish my thoughts here.
3. 	TODO
4.	TODO

