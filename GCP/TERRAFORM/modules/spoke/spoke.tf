data "google_compute_instance" "instance" {
  name = var.instance_name
  zone = var.zone
}

data "google_compute_network" "spoke_network" {
  name = var.network_name
}

data "google_compute_subnetwork" "hub-subnetwork" {
  name   = var.subnetwork_name
  region = var.location
}

resource "google_network_connectivity_spoke" "primary" {
  name      = var.spoke_name
  location  = var.location
  description = "A sample spoke with a linked router appliance instance"
  hub =  var.hubID
  linked_router_appliance_instances {
    instances {
        virtual_machine = var.vm_selflink
        ip_address = data.google_compute_instance.instance.network_interface[0].network_ip
    }
    site_to_site_data_transfer = true
  }
}

# Create a Google Cloud Router and associate it with the NCC hub
resource "google_compute_router" "cloud_router" {
  name    = var.cloud_router
  network = data.google_compute_network.spoke_network.self_link
  region  = var.location  # Replace with your desired region

  bgp {
    asn = var.asn  # Replace with your desired ASN
  }
}

resource "google_compute_router_interface" "interface_1" {
  name       = "interface-1"
  router     = var.cloud_router
  ip_range   = "169.254.1.1/30"
  subnetwork = data.google_compute_subnetwork.hub-subnetwork.self_link
  private_ip_address = var.peer_ip_address1
  depends_on = [ google_compute_router.cloud_router ]
}

resource "google_compute_router_interface" "interface_2" {
  name       = "interface-2"
  router     = var.cloud_router
  ip_range   = "169.254.4.1/30"
  subnetwork = data.google_compute_subnetwork.hub-subnetwork.self_link
  private_ip_address = var.peer_ip_address2
  redundant_interface = google_compute_router_interface.interface_1.name
  depends_on = [ google_compute_router.cloud_router ]
}


resource "google_compute_router_peer" "cldrtr_peer1" {
  name                      = "peer-1"
  router                    = var.cloud_router
  region                    = var.location
  router_appliance_instance = var.vm_selflink
  peer_ip_address           = data.google_compute_instance.instance.network_interface[0].network_ip
  peer_asn                  = var.peer_asn
//  advertised_route_priority = 100
  interface                 = google_compute_router_interface.interface_1.name
  advertise_mode            = "CUSTOM"
  advertised_groups         = ["ALL_SUBNETS"]
  advertised_ip_ranges {
      range = var.range
      } 
  depends_on = [ google_compute_router.cloud_router, google_compute_router_interface.interface_1, google_compute_router_interface.interface_2 ]
}

resource "google_compute_router_peer" "cldrtr_peer2" {
  name                      = "peer-2"
  router                    = var.cloud_router
  region                    = var.location
  router_appliance_instance = var.vm_selflink
  advertise_mode            = "CUSTOM"
  advertised_groups         = ["ALL_SUBNETS"]
  advertised_ip_ranges {
    range = var.range
    } 
  peer_ip_address           = data.google_compute_instance.instance.network_interface[0].network_ip
  peer_asn                  = var.peer_asn
//  advertised_route_priority = 100
  interface                 = google_compute_router_interface.interface_2.name
  depends_on = [ google_compute_router.cloud_router, google_compute_router_interface.interface_1, google_compute_router_interface.interface_2 ]
}