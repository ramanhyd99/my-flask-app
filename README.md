# my-flask-app
Basic python app with dockerfile

The dockerfile can be built using:

* docker build --tag my-flask-app .


The dockerfile will then be added to your local docker images. You can check using:

* docker images | grep my-flask-app


Run the docker image using:

* docker run --publish 5000:5000 my-flask-app

(5000:5000 implies your port:container port)
