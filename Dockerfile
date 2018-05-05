FROM python:3

ADD /src/csvSorter.py /

CMD [ "python3", "./csvSorter.py" ]
