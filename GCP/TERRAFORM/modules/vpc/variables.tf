variable "network_name" {
  type    = string
  default = "my-network"
}

variable "subnet_name" {
  type    = string
  default = "my-subnet"
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "subnet_ip_range" {
  type    = string
  default = "10.0.0.0/24"
}
