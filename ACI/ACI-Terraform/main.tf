terraform {
  required_providers {
    aci = {
      source = "CiscoDevNet/aci"
    }
  }
}

# Configure the provider with your Cisco APIC credentials.
provider "aci" {
  # APIC Username
  username = var.user.username
  # APIC Password
  password = var.user.password
  # APIC URL
  url      = var.user.url
  insecure = true
}

# Define an ACI Tenant Resource.
resource "aci_tenant" "terraform_tenant" {
    name        =  var.tenant
    description = "This tenant is created by terraform"
}

# Define an ACI Tenant VRF Resource.
resource "aci_vrf" "terraform_vrf" {
    tenant_dn   = aci_tenant.terraform_tenant.id
    description = "VRF Created Using Terraform"
    name        = var.vrf
}

# Define an ACI Tenant BD Resource1
resource "aci_bridge_domain" "terraform_bd1" {
    tenant_dn          = aci_tenant.terraform_tenant.id
    relation_fv_rs_ctx = aci_vrf.terraform_vrf.id
    description        = "BD Created Using Terraform"
    name               = var.bd1
}


# Define an ACI Tenant BD Subnet Resource1.
resource "aci_subnet" "terraform_bd_subnet1" {
    parent_dn   = aci_bridge_domain.terraform_bd1.id
    description = "Subnet Created Using Terraform"
    ip          = var.subnet1
    scope       = ["public"]
}

# Define an ACI Tenant BD Resource2
resource "aci_bridge_domain" "terraform_bd2" {
    tenant_dn          = aci_tenant.terraform_tenant.id
    relation_fv_rs_ctx = aci_vrf.terraform_vrf.id
    description        = "BD Created Using Terraform"
    name               = var.bd2
}


# Define an ACI Tenant BD Subnet Resource2.
resource "aci_subnet" "terraform_bd_subnet2" {
    parent_dn   = aci_bridge_domain.terraform_bd2.id
    description = "Subnet Created Using Terraform"
    ip          = var.subnet2
    scope       = ["public"]
}

# Define an ACI filter Resource.
   resource "aci_filter" "terraform_filter" {
       for_each    = var.filters
       tenant_dn   = aci_tenant.terraform_tenant.id
       description = "This is filter ${each.key} created by terraform"
       name        = each.value.filter
   }

# Define an ACI filter entry resource.
resource "aci_filter_entry" "terraform_filter_entry" {
    for_each      = var.filters
    filter_dn     = aci_filter.terraform_filter[each.key].id
    name          = each.value.entry
    ether_t       = "ipv4"
    prot          = each.value.protocol
    d_from_port   = each.value.port
    d_to_port     = each.value.port
}

# Define an ACI Contract Resource.
resource "aci_contract" "terraform_contract" {
    for_each      = var.contracts
    tenant_dn     = aci_tenant.terraform_tenant.id
    name          = each.value.contract
    description   = "Contract created using Terraform"
    scope         = "context"
}

# Define an ACI Contract Subject Resource.
resource "aci_contract_subject" "terraform_contract_subject" {
    for_each                      = var.contracts
    contract_dn                   = aci_contract.terraform_contract[each.key].id
    name                          = each.value.subject
    relation_vz_rs_subj_filt_att  = [aci_filter.terraform_filter[each.value.filter].id]
}

# Define an ACI Application Profile Resource.
resource "aci_application_profile" "terraform_ap" {
    tenant_dn  = aci_tenant.terraform_tenant.id
    name       = var.ap
    description = "App Profile Created Using Terraform"
}
resource "aci_application_epg" "terraform_epg" {
    for_each                = var.epgs
    application_profile_dn  = aci_application_profile.terraform_ap.id
    name                    = each.value.epg
    relation_fv_rs_bd       = aci_bridge_domain.terraform_bd1.id
    description             = "EPG Created Using Terraform"
}

# Associate the EPGs with the contracts
resource "aci_epg_to_contract" "terraform_epg_contract" {
    for_each           = var.epg_contracts
    application_epg_dn = aci_application_epg.terraform_epg[each.value.epg].id
    contract_dn        = aci_contract.terraform_contract[each.value.contract].id
    contract_type      = each.value.contract_type
}