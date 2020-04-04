FROM python:2
COPY . /app
WORKDIR /app
RUN pip install requests bs4
CMD python ./script.py