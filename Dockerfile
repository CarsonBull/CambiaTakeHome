# Python package to be used.
# See https://hub.docker.com/_/python/ for reference
FROM python:3.5

# Change the working dir
WORKDIR /usr/src/app

# For testing it can be handy to setup a mounted local drive for input.csv to allow for tests to be done rapidly
COPY ./src/ /usr/src/app

# Use ./ on the csv because it is the folder that our working dir is in
CMD ["python", "./csvSorter.py"]


#Testing CDM
#CMD [ "python3", "-m", "unittest", "test_csvSorter.py" ]

