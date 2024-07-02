data "google_compute_network" "my_network" {
  name = var.network_name
#  project = var.project
}

data "google_compute_subnetwork" "my_subnet" {
  name          = var.subnet_name
#  project = var.project
  region = var.region
}

# Create a Google Compute Engine instance
resource "google_compute_instance" "my_instance" {
  name         = var.instance_name
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "projects/cisco-public/global/images/meraki-vmx-16-10"
    }
  }

  network_interface {
    network = data.google_compute_network.my_network.self_link
    subnetwork = data.google_compute_subnetwork.my_subnet.self_link
    nic_type = "GVNIC"

    access_config {
      network_tier = "STANDARD"
    }
  }

  tags = ["http-server", "https-server"]
  
  can_ip_forward = true
  enable_display = true
  
  metadata = {
    token = var.vm_auth_token
  }
}
