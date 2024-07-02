data "google_compute_network" "hub_network" {
  name = var.hub_network_name
#  project = var.project
}

data "google_compute_network" "spoke_network" {
  name = var.spoke_network_name
#  project = var.project
}

resource "google_compute_network_peering" "peering1" {
  name         = "peering1"
  network      = data.google_compute_network.hub_network.self_link
  peer_network = data.google_compute_network.spoke_network.self_link
  import_custom_routes = true
  export_custom_routes = true
}

resource "google_compute_network_peering" "peering2" {
  name         = "peering2"
  network      = data.google_compute_network.spoke_network.self_link
  peer_network = data.google_compute_network.hub_network.self_link
  import_custom_routes = true
  export_custom_routes = true
}