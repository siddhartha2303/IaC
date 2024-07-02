import csv
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import DeviceForm, VLANForm, WifiForm
from .models import Device, VLAN, Wifi

def success_view(request):
    return render(request, 'success.html')

def index(request):
    return render(request, 'index.html')

def claim_devices(request):
    success_message = None
    devices = Device.objects.all()
    
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Devices claimed successfully!"
            devices = Device.objects.all()
    else:
        form = DeviceForm()
    
    return render(request, 'claim_devices.html', {'form': form, 'success_message': success_message, 'devices': devices})

def delete_device(request, pk):
    device = Device.objects.get(pk=pk)
    device.delete()
    return redirect('claim_devices')

def vlan(request):
    success_message = None
    vlans = VLAN.objects.all()
    form = VLANForm()  # Initialize form here

    if request.method == 'POST':
        if 'csvFile' in request.FILES:
            csv_file = request.FILES['csvFile']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                try:
                    # Convert 'enable_dhcp' field to boolean
                    enable_dhcp = True if row['enable_dhcp'].lower() in ['true', 'yes', '1'] else False

                    VLAN.objects.create(
                        networkName=row['networkName'],
                        vlan_name=row['vlan_name'],
                        vlan_id=row['vlan_id'],
                        subnet=row['subnet'],
                        gateway=row['gateway'],
                        enable_dhcp=enable_dhcp,
                        lease_time=row['lease_time'],
                        reserved_ip_start=row['reserved_ip_start'],
                        reserved_ip_end=row['reserved_ip_end'],
                        dns_nameservers=row['dns_nameservers'],
                        dhcp_option=row['dhcp_option'],
                        dhcp_type=row['dhcp_type'],
                        ntp_ip=row['ntp_ip']
                    )
                except KeyError as e:
                    error_message = f"KeyError: {str(e)}"
                    return JsonResponse({'error': error_message}, status=400)

            success_message = "CSV data processed successfully."
        else:
            form = VLANForm(request.POST)
            if form.is_valid():
                form.save()
                success_message = "VLAN entry added successfully!"
                vlans = VLAN.objects.all()

    return render(request, 'vlan.html', {'form': form, 'success_message': success_message, 'vlans': vlans})


def delete_vlan(request, pk):
    vlan = VLAN.objects.get(pk=pk)
    vlan.delete()
    return redirect('vlan')

def wifi(request):
    success_message = None
    ssids = Wifi.objects.all()
    
    if request.method == 'POST':
        form = WifiForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Wifi entry added successfully!"
            ssids = Wifi.objects.all()
    else:
        form = WifiForm()
    print(form.errors)

    return render(request, 'wifi.html', {'form': form, 'success_message': success_message, 'ssids': ssids})

def delete_wifi(request, pk):
    ssid = Wifi.objects.get(pk=pk)
    ssid.delete()
    return redirect('wifi')

def process_csv(request):
    if request.method == 'POST' and request.FILES['csvFile']:
        csv_file = request.FILES['csvFile']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        for row in reader:
            # Convert 'visible' field to boolean
            visible = True if row['visible'].lower() in ['true', 'yes', '1'] else False

            Wifi.objects.create(
                number=row['number'],
                ssid=row['ssid'],
                authMode=row['authMode'],
                password=row['password'],
                ipAssignmentMode=row['ipAssignmentMode'],
                vlanId=row['vlanId'],
                visible=visible,
                encryptionMode=row['encryptionMode']
            )

        return JsonResponse({'message': 'CSV data processed successfully.'})
    else:
        return JsonResponse({'error': 'No file uploaded or invalid request.'}, status=400)
