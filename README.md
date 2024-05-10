# Terraform Use Case for a Kubernetes-based Web App in the Cloud

This project enables the deployment of a web application in a cloud provider using Terraform to provision the required infrastructure.

The application consists of 8 microservices: offers, posts, rf003, rf004, rf005, routes, users, and scores. Each microservice includes basic API calls built using Flask. Within each folder in this repository, you can find all the requirements needed to build each microservice, along with Dockerfiles that facilitate the creation of images and the spinning up of containers.

## Local Test using Docker-Compose:

For a straightforward local test, a Docker-compose file is provided. To check the functionality of the app locally, simply clone this repository, navigate to the project's root directory, and run:

$ docker-compose up --build

This command sets up 4 of the 8 microservices, along with PostgreSQL instances for each.

Then, you can use this Postman collection to test a few use cases:

https://raw.githubusercontent.com/MISW-4301-Desarrollo-Apps-en-la-Nube/proyecto-monitor/main/entrega1/entrega1.json

Simply import this collection into Postman, and run the full collection or select tests to check that the endpoints are working correctly.

## About the App

This simple yet innovative app facilitates the creation of offers on user posts. It connects individuals who need to ship items with travelers who have spare luggage space. Acting as a broker, the platform enables 'senders' to post available space in their luggage, and 'travelers' to match these postings based on their shipping needs. This approach not only optimizes unused luggage space but also offers a cost-effective, community-driven alternative to traditional shipping methods. The platform is designed to transform the landscape of national and international parcel delivery, fostering trust and community participation.

Additionally, the app includes a service that scores each offer, allowing the user who creates the post to determine which offer is most profitable.

For more insights, feel free to review the code.

## Transitioning from Docker-Compose to Cloud
### Cloud-Native Architecture of the App

![Screenshot 2024-05-09 at 10 49 44 PM](https://github.com/ofgarzon2662/I2-Project/assets/5341117/2266ff5b-58bd-4c96-9d78-3075dfe641f6)

The architecture diagram above illustrates how the app is deployed using Kubernetes infrastructure. Each microservice is deployed in a pod within a single deployment and each deployment is accessed through a service.

There is an Ingress/API Gateway that serves as a single point of entry to our app, simplifying communication with each of the backend services. You only need the public IP address of the ingress to make calls to the endpoints exposed by the microservices.

The microservices also communicate amongst themselves in complex ways. For example, the RF003 component interacts with the Post and Route components, as well as the app's client, managing a basic yet sufficiently complex orchestration. Fortunately, the Ingress component manages these intricate communications effortlessly.

Each microservice also has a persistence layer that isn’t shown in the architecture diagram, which is conveniently managed by Kubernetes as well.


### Infrastructure as Code (IaC) and Terraform

To efficiently orchestrate all these microservices, we leverage Terraform scripts. These scripts enable rapid and convenient provisioning of the necessary infrastructure, significantly speeding up deployments and testing.

Here are the steps to utilize the provided Terraform scripts to set up the Kubernetes cluster:

1. Access to a Public Cloud Provider: Ensure you have access to a public cloud provider. Although the scripts are designed primarily for Google Cloud Platform (GCP), they are adaptable to other public cloud environments.
2.You need to create a service account with sufficient privileges to enable handling of the artifacts in the cloud provider you're using. In the case of GCP, a service account that allows managing artifacts in artifacts registry, creation of SQL instances, managing of Kubernets cluster is good enough to get you started. Always remember to guide provision this account following the least amount of permissions principle. This service account will be used to allow terraform perform all the necesary steps in the cloud. 
4. If your are in GCP, go to the console. Select the IAM service, and go to Service accounts. Select the account you just created. Go to the keys tab, and add a new key.
5. You can download the key into your pc, but you can also use the Workload Identity federetion services provided by google to safely store this sensitive file. For simplicity, we assume that you download this file into your local pc.You should get a JSON file with the credentials for this service account.
6. Now, in the main.tf script provided in this repo, you need to add the file location into the credentials key (line 2). Paste the location of the file.

#### Artifact Registry and pushing of images

For the kubernets deployment to be able to use the microservices in this repo, you need to create an artifact Registry in your cloud provider. In the case of GCP, in the console enable the Artifact Registry API . 

Go to Artifact registry. Create repo in the console. Add a name, region, description, all. 

Authenticate through the gcloud cli: gcloud auth configure-docker us-central1-docker.pkg.dev. Ensure that you're using the right credentials in gcloud in order to be able to push the images. 

Then, build each of the images using this:

docker build -t REGION-docker.pkg.dev/PROJECT_ID/ARTIFACT_REGISTRY/offers:1.0 ./offers

that will create the image for the offers microservice, based on the docker file that is located in ./offers

If you're using a mac with an m1,2 chip, you need to add this flag:

docker build --platform linux/amd64 -t ...


