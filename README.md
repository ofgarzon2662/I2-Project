# Terraform use case for a k8s-based web App in cloud
This is a project where you will be able to deploy an App in a cloud provider using terraform to provision the infrastructure needed. 

The application consists of 8 microservices: offers, posts, rf003, rf004, rf005, routes, users and scores. 

Each microservices consists of basic API calls built using Flask. On each folder in this repo you will be able to find all the requirements needed to build each microservice, as well as Dockerfiles that can be easily used to create images and spin up containers. 

## Local Test using Docker-Compose:

For a basic local easy test, a Docker-compose file is provided. To check the functionality of this app locally, simply clone this repo, go to the root directory of this project and run:

$ docker-compose up --build

That will set up 4 of the 8 microservices, along with postgres instances for each of them. 

Then you can use this postman collection to test a few use cases:

https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Simply import that collection in postman, and run the full collection or just a few tests to check that the endpoints work. 

## What is this app about?

You may discover that this is a very simple app that could be used to create offers on a user's post. This innovative service connects individuals who need to ship items with travelers who have spare luggage space. As a broker, the platform facilitates the exchange, allowing 'senders' to post available space in their luggage, and 'travellers' to match with these postings based on their shipping needs. This approach not only optimizes unused luggage space but also provides a cost-effective, community-driven alternative to traditional shipping methods. The platform aims to reshape the landscape of national and international parcel delivery, capitalizing on trust and community participation. 

There is also a service that provides a score on each of the offers, allowing the user who creates the post to see which offer is more profitable. 

The reader is welcome to check the code to gain more insight on it. 

## Going from docker-compose to Cloud
### Cloud Native Architecture of the
App:

For our practical purposes of bringin up a k8s deployment that can handle the orchestration of all of these microservices, we will use a terraform script to provide the infrastructure in a timely and convenient way, in order to make deployments and tests faster. 
