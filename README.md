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
2. **Create a Service Account:**
  * In GCP or your chosen cloud provider, create a service account with sufficient privileges. For GCP, the account should have permissions to manage artifacts in the Artifact Registry, create SQL instances, and manage Kubernetes clusters.
  * Follow the principle of least privilege when provisioning this account. This service account enables Terraform to perform all necessary actions in the cloud.

3. **Generate and Manage Service Account Key**
  * In the GCP console, go to IAM & Admin > Service Accounts. Select your service account, navigate to the Keys tab, and add a new key.
  * You may choose to download this key to your PC. Alternatively, consider using Google's Workload Identity Federation to securely manage this sensitive information. For simplicity, this guide assumes you download the key.
  * Obtain a JSON file containing the service account credentials.
4. **Update Terraform Configuration:**
  * In the main.tf script provided in this repository, update the credentials key with the path to your downloaded JSON file.

#### Setting Up Artifact Registry and Pushing Images

To utilize the microservices, an Artifact Registry needs to be set up in your cloud provider. Here's how to do it in GCP:

1. **Enable the Artifact Registry API:**
   * Navigate to the GCP console and enable the Artifact Registry API.
2. **Create an Artifact Repository:**
  * Go to the Artifact Registry section in the GCP console.
  * Create a new repository by specifying a name, region, and other required details.
3. **Authenticate Your Local Environment:**
    * Use the following command to configure Docker to authenticate with your GCP Artifact Registry:
    * gcloud auth configure-docker REGION-docker.pkg.dev
    * Ensure that the correct credentials are active in your gcloud CLI to allow image pushing.

4. **Build and Push Docker Images**
   * For each microservice, build Docker images using the Dockerfiles provided in their respective directories. For instance, to build the offers microservice:
   * docker build -t REGION-docker.pkg.dev/PROJECT_ID/ARTIFACT_REGISTRY/offers:1.0 ./offers
   * If using a Mac with an M1/M2 chip, include the --platform linux/amd64 flag:
   * docker build --platform linux/amd64 -t ...
   * push each of the imaget to the registry:
   * Once the image is built, push it to the configured Artifact Registry using the following command:
     ```bash
     docker push REGION-docker.pkg.dev/PROJECT_ID/ARTIFACT_REGISTRY/offers:1.0
     ```
## Running Terraform to Provision Infrastructure

To deploy the infrastructure necessary for hosting our Kubernetes-based application, follow these steps to use the provided Terraform scripts:

### Prerequisites
Ensure you have Terraform installed on your machine. If not, download and install Terraform from [terraform.io](https://www.terraform.io/downloads.html).

### Steps to Deploy Using Terraform

1. **Initialization**:
   Run the following command to initialize Terraform, which will download the necessary providers and initialize the backend.
   ```bash
   terraform init
   ```

