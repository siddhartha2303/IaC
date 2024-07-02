from django.db import models

class Device(models.Model):
    serial_no = models.CharField(primary_key=True, max_length=100, verbose_name="Serial No.")
    hostname = models.CharField(max_length=100, verbose_name="Hostname")
    warmspare = models.BooleanField(default=False, verbose_name="Warmspare")
    stp_root = models.BooleanField(default=False, verbose_name="Stp Root")

    class Meta:
        app_label = 'mcdmerakiapp'  # This ensures the model is associated with the correct app
        db_table = 'mcdmerakiapp_device'


class VLAN(models.Model):
    networkName = models.CharField(primary_key=True, max_length=100)
    vlan_id = models.IntegerField()
    vlan_name = models.CharField(max_length=100)
    subnet = models.CharField(max_length=100)
    gateway = models.CharField(max_length=100)
    enable_dhcp = models.BooleanField(default=False)
    lease_time = models.CharField(max_length=100)
    reserved_ip_start = models.CharField(max_length=100)
    reserved_ip_end = models.CharField(max_length=100)
    dns_nameservers = models.CharField(max_length=100)
    dhcp_option = models.CharField(max_length=100)
    dhcp_type = models.CharField(max_length=100)
    ntp_ip = models.CharField(max_length=100)

    class Meta:
        app_label = 'mcdmerakiapp'
        db_table = 'mcdmerakiapp_vlan'

class Wifi(models.Model):
    number = models.IntegerField(primary_key=True)
    ssid = models.CharField(max_length=100)
    authMode = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ipAssignmentMode = models.CharField(max_length=100)
    vlanId = models.IntegerField()
    visible = models.BooleanField(default=False)
    encryptionMode = models.CharField(max_length=100)

    class Meta:
        app_label = 'mcdmerakiapp'
        db_table = 'mcdmerakiapp_wifi'