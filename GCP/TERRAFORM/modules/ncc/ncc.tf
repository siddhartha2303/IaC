# Create the NCC Cloud Router
resource "google_network_connectivity_hub" "my_hub" {
  name         = var.ncc_hub
#  project      = var.project
  description  = "My NCC Hub"
}