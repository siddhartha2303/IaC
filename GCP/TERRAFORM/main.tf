data "terraform_remote_state" "localtfstate" {
  backend = "local"

  config = {
    path = "terraform.tfstate"
  }
  depends_on = [module.create_vpc]
}
resource "null_resource" "wait_for_output_ncchub" {
  triggers = {
    module_output_dependency_ncchub = data.terraform_remote_state.localtfstate.outputs.hubID
  }
  depends_on = [module.create_ncc]
}

module "create_vpc" {
  source          = "./modules/vpc"
  network_name    = var.vpc_name
  subnet_name     = var.vmx_subnet_name
  region          = var.vmx_hub_region
  subnet_ip_range = var.vmx_subnet_ip_range
}

module "create_workload_vpc" {
  source          = "./modules/vpc"
  network_name    = var.workload_vpc_name
  subnet_name     = var.workload_subnet_name
  region          = var.vmx_hub_region
  subnet_ip_range = var.workload_subnet_ip_range
}

module "create_vpc_peering" {
  source          = "./modules/network-peering"
  hub_network_name = var.vpc_name
  spoke_network_name = var.workload_vpc_name
  depends_on  = [module.create_vpc, module.create_workload_vpc]
}


module "create_compute" {
  source        = "./modules/computes"
  instance_name = var.vmx_instance_name
  machine_type  = var.vmx_machine_type
  zone          = var.vmx_zone
  network_name  = var.vpc_name
  subnet_name   = var.vmx_subnet_name
  project       = var.project_name
  region        = var.vmx_hub_region
  vm_auth_token = var.vmx_vm_auth_token
  depends_on    = [module.create_vpc_peering]
}

module "create_workload_compute" {
  source        = "./modules/workload_computes"
  instance_name = var.workload_instance_name
  machine_type  = var.workload_machine_type
  zone          = var.vmx_zone
  network_name  = var.workload_vpc_name
  subnet_name   = var.workload_subnet_name
  project       = var.project_name
  region        = var.vmx_hub_region
  depends_on    = [module.create_vpc_peering]
}


module "create_ncc" {
  source  = "./modules/ncc"
  project = var.project_name
  ncc_hub = var.ncc_hub
}

module "create_spoke" {
  source              = "./modules/spoke"
  spoke_name          = var.spoke
  location            = var.vmx_hub_region
  ncc_hub             = var.ncc_hub
  hubID               = module.create_ncc.hub_id
  project             = var.project_name
  network_name        = var.vpc_name
  subnetwork_name     = var.vmx_subnet_name
  asn                 = var.asn_number
  instance_name       = var.vmx_instance_name
  cloud_router        = var.cldrtr
  peer_asn            = var.peer_asn_number
  peer_ip_address1    = var.peer_ip1
  peer_ip_address2    = var.peer_ip2
  range               = var.advertised_ip_ranges
  vm_selflink         = "https://www.googleapis.com/compute/v1/projects/${var.project_id}/zones/${var.vmx_zone}/instances/${var.vmx_instance_name}"
  zone                = var.vmx_zone
  depends_on          = [module.create_vpc, module.create_compute, module.create_ncc, null_resource.wait_for_output_ncchub]
}

