provider "google" {
  credentials = file("i3schoolproject-a409eac16bfd.json")
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
    ip_cidr_range = "192.168.64.0/21"
  }

  secondary_ip_range {
    range_name    = "services"
    ip_cidr_range = "192.168.72.0/21"
  }

}

resource "google_compute_global_address" "dbs_net_terraform" {
  name          = "dbs-net-terraform"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 24
  address       = "192.168.0.0"
  network       = google_compute_network.vpc.self_link
}


resource "google_compute_firewall" "allow_db_ingress" {
  name        = "allow-db-ingress-terraform"
  network     = google_compute_network.vpc.self_link
  priority    = 1000
  direction   = "INGRESS"

  allow {
    protocol = "tcp"
    ports    = ["5432"]
  }

  source_ranges = ["192.168.1.0/24"]
  target_tags   = ["basesdedatos-terraform"]
}


// Creation of PostgreSQL instance

resource "google_sql_database_instance" "postgres" {
  name             = "apps-db-terraform"
  region           = "us-central1"
  database_version = "POSTGRES_14"
  

  settings {
    tier              = "db-f1-micro"
    availability_type = "ZONAL"
    disk_size         = 10
    disk_type         = "PD_HDD"
    disk_autoresize   = false

    ip_configuration {
      ipv4_enabled    = false
      private_network = google_compute_network.vpc.self_link
    }

    backup_configuration {
      enabled = false
    }

    location_preference {
      zone = "us-central1-a"
    }

    user_labels = {
      "basesdedatos-terraform" = ""
    }
  }
  
}

resource "google_project_service" "service_networking" {
  service = "servicenetworking.googleapis.com"
}

resource "random_password" "password" {
  length  = 16
  special = true
}

resource "google_secret_manager_secret" "db_password" {
  secret_id = "db-password-secret"

    replication {
    user_managed {
      replicas {
        location = "us-central1"  // Specify an allowed region here
      }
    }
  }
}

resource "google_secret_manager_secret_version" "password" {
  secret      = google_secret_manager_secret.db_password.id
  secret_data = random_password.password.result
}

resource "google_sql_user" "default" {
  name     = "postgres"
  instance = google_sql_database_instance.postgres.name
  password = random_password.password.result
}

resource "google_service_networking_connection" "private_vpc_connection" {
  network       = google_compute_network.vpc.self_link
  service       = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.dbs_net_terraform.name]
}

resource "google_project_service" "secret_manager" {
  service = "secretmanager.googleapis.com"
}

resource "google_compute_global_address" "private_ip_range" {
  name          = "sql-private-ip-range"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 24
  network       = google_compute_network.vpc.self_link
}


