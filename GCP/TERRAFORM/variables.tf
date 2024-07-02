variable "project_name" {
  type    = string
  default = "my-project"
}

variable "project_id" {
  type    = string
  default = "my-project-id"
}

variable "organization_id" {
  type    = string
  default = "your-organization-id" # Optional: Replace with your organization ID
}

variable "vpc_name" {
  type    = string
  default = "my-network"
}

variable "workload_vpc_name" {
  type    = string
  default = "my-network"
}

variable "vmx_subnet_name" {
  type    = string
  default = "my-subnet"
}

variable "workload_subnet_name" {
  type    = string
  default = "my-subnet"
}

variable "vmx_hub_region" {
  type    = string
  default = "us-central1"
}

variable "vmx_subnet_ip_range" {
  type    = string
  default = "10.0.0.0/24"
}

variable "workload_subnet_ip_range" {
  type    = string
  default = "10.0.0.0/24"
}

variable "vmx_instance_name" {
  type    = string
  default = "my-instance"
}

variable "vmx_machine_type" {
  type    = string
  default = "n1-standard-1"
}

variable "vmx_zone" {
  type    = string
  default = "us-central1-a"
}

variable "credentials_file" {
  type    = string
  default = "path/to/your/credentials.json"
}

variable "vmx_vm_auth_token" {
  type    = string
  default = "your-vm-auth-token"
}

variable "ncc_hub" {
  type    = string
  default = "ncc_hub"
}

variable "cldrtr" {
  type    = string
  default = "cloud_router"
}

variable "spoke" {
  type = string
}

variable "asn_number" {
  type = string
}

variable "peer_asn_number" {
  type = string
}

variable "peer_ip1" {
  type = string
}

variable "peer_ip2" {
  type = string
}

variable "workload_instance_name" {
  type = string
}

variable "workload_machine_type" {
  type = string
}

variable "advertised_ip_ranges" {
  type = string
}