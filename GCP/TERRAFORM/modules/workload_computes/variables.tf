variable "instance_name" {
  type    = string
  default = "my-instance"
}

variable "machine_type" {
  type    = string
  default = "n1-standard-1"
}

variable "workload_instance_name" {
  type    = string
  default = "my-instance"
}

variable "workload_machine_type" {
  type    = string
  default = "f1-micro"
}

variable "zone" {
  type    = string
  default = "us-central1-a"
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