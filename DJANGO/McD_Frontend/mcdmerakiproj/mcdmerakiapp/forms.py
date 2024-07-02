from django import forms
from .models import Device
from .models import VLAN
from .models import Wifi
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['serial_no', 'hostname', 'warmspare', 'stp_root']

class VLANForm(forms.ModelForm):
    class Meta:
        model = VLAN
        fields = ['networkName', 'vlan_id', 'vlan_name', 'subnet', 'gateway', 'enable_dhcp', 'lease_time', 'reserved_ip_start', 'reserved_ip_end', 'dns_nameservers', 'dhcp_option', 'dhcp_type', 'ntp_ip']

class WifiForm(forms.ModelForm):
    class Meta:
        model = Wifi
        fields = ['number', 'ssid', 'authMode', 'password', 'ipAssignmentMode', 'vlanId', 'visible', 'encryptionMode']