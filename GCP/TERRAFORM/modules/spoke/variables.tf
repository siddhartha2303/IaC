variable "spoke_name" {
  type = string
}

variable "location" {
  type = string
}

variable "ncc_hub" {
  type    = string
  default = "ncc_hub"  
}

variable "project" {
  type    = string
  default = "my-project"
}

variable "instance_name" {
  type    = string
  default = "my-instance"
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "hubID" {
  type = string
}

variable "vm_selflink" {
  type = string
}

variable "cloud_router" {
  type = string
}

variable "network_name" {
  type    = string
  default = "my_network"
}

variable "subnetwork_name" {
  type    = string
  default = "my_network"
}

variable "asn" {
  type    = string
  default = "65001"
}

variable "peer_asn" {
  type    = string
  default = "65513"
}

variable "peer_ip_address1" {
  type = string
}

variable "peer_ip_address2" {
  type = string
}

variable "range" {
  type = string
}