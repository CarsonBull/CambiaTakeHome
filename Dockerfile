# Python package to be used.
# See https://hub.docker.com/_/python/ for reference
FROM python:3.5

# Change the working dir
WORKDIR /usr/src/app

COPY ./src/ /usr/src/app

# Use ./ on the csv because it is the folder that our working dir is in
CMD [ "python3", "./csvSorter.py" ]
