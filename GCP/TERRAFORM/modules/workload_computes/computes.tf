data "google_compute_network" "my_network" {
  name = var.network_name
#  project = var.project
}

data "google_compute_subnetwork" "my_subnet" {
  name          = var.subnet_name
#  project = var.project
  region = var.region
}

resource "google_compute_firewall" "allow_ssh" {
  name          = "allow-ssh"
  network       = data.google_compute_network.my_network.name
  target_tags   = ["allow-ssh"] // this targets our tagged VM
  source_ranges = ["0.0.0.0/0"]

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
    
  allow {
    protocol = "icmp"
  }
}

# Create a Google Compute Engine instance
resource "google_compute_instance" "my_instance" {
  name         = var.instance_name
  machine_type = var.machine_type
  zone         = var.zone
  tags         = ["allow-ssh"] 

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = data.google_compute_network.my_network.self_link
    subnetwork = data.google_compute_subnetwork.my_subnet.self_link

    access_config {
    }
  }
}
