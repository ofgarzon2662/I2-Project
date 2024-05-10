provider "google" {
  credentials = file("class-adv2024-vueibaezis13-a85367528445.json")
  project     = var.project_id
  region      = var.region
}

resource "google_project_service" "compute_api" {
  service = "compute.googleapis.com"
}

resource "google_project_service" "container_api" {
  service = "container.googleapis.com"
}


resource "google_project_service" "service_usage" {
  service = "serviceusage.googleapis.com"
  disable_on_destroy = false  # Ensures the API is not disabled when the Terraform resource is destroyed
}

resource "google_container_cluster" "primary" {
  name     = "terraform-cluster"
  location = var.region

  network    = google_compute_network.vpc.name
  subnetwork = google_compute_subnetwork.subnet.name

  ip_allocation_policy {
    cluster_secondary_range_name  = "pods"
    services_secondary_range_name = "services"
  }

  enable_autopilot = true
}

resource "google_compute_network" "vpc" {
  name                    = "terraform-vpc"
  auto_create_subnetworks = false
  routing_mode            = "REGIONAL"
  mtu                     = 1460
}

resource "google_compute_subnetwork" "subnet" {
  name          = "terraform-subnet"
  ip_cidr_range = "192.168.96.0/19"
  region        = var.region
  network       = google_compute_network.vpc.name

  secondary_ip_range {
    range_name    = "pods"
    ip_cidr_range = "192.168.128.0/21"
  }

  secondary_ip_range {
    range_name    = "services"
    ip_cidr_range = "192.168.136.0/21"
  }

}

resource "google_compute_global_address" "dbs_net_terraform" {
  name          = "dbs-net-terraform"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 24
  address       = "192.168.1.0"
  network       = google_compute_network.terraform_vpc.self_link
}
