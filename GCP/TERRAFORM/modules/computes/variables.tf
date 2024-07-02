variable "instance_name" {
  type    = string
  default = "my-instance"
}

variable "machine_type" {
  type    = string
  default = "n1-standard-1"
}

variable "zone" {
  type    = string
  default = "us-central1-a"
}

variable "vm_auth_token" {
  type    = string
  default = "your-vm-auth-token"
}

variable "network_name" {
  type    = string
  default = "my_network"
}

variable "subnet_name" {
  type    = string
  default = "my_subnet"  
}

variable "project" {
  type    = string
  default = "my-project"
}

variable "region" {
  type    = string
  default = "us-central1"
}