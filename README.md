# Terraform use case for a k8s-based web App in cloud
This is a project where you will be able to deploy an App in a cloud provider using terraform to provision the infrastructure needed. 

The application consists of 8 microservices: offers, posts, rf003, rf004, rf005, routes, users and scores. 

Each microservices consists of basic API calls built using Flask. On each folder in this repo you will be able to find all the requirements needed to build each microservice, as well as Dockerfiles that can be easily used to create images and spin up containers. 

For a basic local easy test, a Docker-compose file is provided. To check the functionality of this app locally, simply clone this repo, go to the root directory of this project and run:

$ docker-compose up --build

That will set up 4 of the 8 microservices, along with postgres instances for each of them. 

Then you can use this postman collection to test a few use cases:

https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Simply import that collection in postman, and run the full collection or just a few tests to check that the endpoints work. 

You may discover that this is a very simple app that could be used to create offers on a user post. 
