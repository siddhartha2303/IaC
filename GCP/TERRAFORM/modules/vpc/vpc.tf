# Create a VPC network
resource "google_compute_network" "my_network" {
  name = var.network_name
  auto_create_subnetworks = false
}

# Create a subnet within the VPC
resource "google_compute_subnetwork" "my_subnet" {
  name          = var.subnet_name
  region        = var.region
  network       = google_compute_network.my_network.self_link
  ip_cidr_range = var.subnet_ip_range
}