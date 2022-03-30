FROM python:3.8-slim-buster

#Create/switch to src dir in the image
WORKDIR /src

#Copy the requirements.txt from /src dir into the image
COPY src/requirements.txt requirements.txt

#Install dependencies for the python app using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Copy all the contents of current dir into the image
COPY . .

#Set environement variables needed for the flask app to run
ENV  FLASK_APP=src/main
ENV FLASK_ENV=development

CMD [ "flask", "run"]