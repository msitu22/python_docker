# # Set the working directory to /app, you can find the path when you type 'pwd' in the terminal
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask","run", "--host=0.0.0.0","--port=5000"]