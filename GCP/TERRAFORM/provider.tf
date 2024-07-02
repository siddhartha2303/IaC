# Initialize the Terraform Google Cloud provider
provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project_id
  region      = var.vmx_hub_region
}
