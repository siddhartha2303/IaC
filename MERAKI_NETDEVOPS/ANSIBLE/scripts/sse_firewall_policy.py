import requests
import json
import csv

print("****************** Start ********************")

#MCD POC LAB2 
url = "https://api.meraki.com/api/secureConnect/v1/organizations/698057942242432629/policy/rulesets/220689/rules"
headers = {
    'Content-Type': 'application/json',
#MCD POC LAB2     
    'Authorization': 'Bearer 4f0e556bd9fab1397cf3a44a17e986d75d5bc4aa'
   }

def create_app(applicationName,destinationAddr,protocolPorts):
    
    # Endpoint URL
    url = "https://api.meraki.com/api/v1/organizations/698057942242432629/secureConnect/privateApplications"

    # Payload for creating a private application

    payload = {
        "name": applicationName,
        "description": applicationName,
        "destinations": [
            {
                "destinationAddr": destinationAddr,
                "protocolPorts": protocolPorts,
                "accessType": "network"
            }
        ],
        "appProtocol": "https",
        "sni": "xyz123.jira.com",
        "externalFQDN": "https://jira-5001.ztna.ciscoplus.com",
        "sslVerificationEnabled": True,
        "applicationGroupIds": []
    }

    # Send POST request to create the private application
    response = requests.post(url, json=payload, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("##Private application created successfully.##")
        print("Application Name:", response.json().get("data").get("name"))
        print("Application ID:", response.json().get("data").get("applicationId"))
        return response.json().get("data").get("applicationId")

    else:
        print("Failed to create private application. Status code:", response.status_code)
        print("Response:", response.text)
        return (response.json().get("errors")[0])

print("Fetching details from csv")

with open('sserules2.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        try:
            dstaddr = row[4]
            dstaddrlst = dstaddr.split(",")
            srcaddr = row[3]
            srcaddlst = srcaddr.split(",")
            tcp_ports = row[5]
            tcp_ports = tcp_ports.split(",")
            print(tcp_ports)
            if tcp_ports == ['']:
                tcp_ports = []
            udp_ports = row[6]
            udp_ports = udp_ports.split(",")
            if udp_ports == ['']:
                print(2)
                udp_ports = []
            if row[7]:
                icmp_port = ""
            else:
                icmp_port = []
                
            protocolPorts = []
            protocolports= [
                {
                "protocol": "TCP",
                "ports": tcp_ports
                },
                {
                "protocol": "UDP",
                "ports": udp_ports
                },
                {
                "protocol": "ANY",
                "ports": []
                },
                {
                "protocol": "ICMP",
                "ports": icmp_port
                }
            ]

            #Format ports
            for protoport in protocolports:
                if protoport.get("ports"):
                    protoport["ports"] = ','.join([str(elem) for elem in (protoport.get("ports"))])
                    protocolPorts.append(protoport)

            applicationName = row[8]

            #create policy
            print("Creating Application...")
            DestAttributeValue = create_app(applicationName=applicationName,destinationAddr=dstaddrlst,protocolPorts=protocolPorts)
            DestAttributeValue = [int(DestAttributeValue)]
            
            payload = json.dumps({
                "ruleAction": row[2],
                "ruleName": row[1],
                "rulePriority": 1,
                "ruleIsEnabled": True,
                "ruleDescription": row[0],
                "ruleConditions": [
                        {
                            "attributeName": "config.schedule.timezone",
                            "attributeOperator": "=",
                            "attributeValue": "America/New_York"
                        },
                        {
                            "attributeName": "umbrella.source.ip_address",
                            "attributeOperator": "IN",
                            "attributeValue": srcaddlst
                        },
                        {
                            "attributeName": "umbrella.destination.private_application_ids",
                            "attributeOperator": "IN",
                            "attributeValue": DestAttributeValue
                        },
                        {
                            "attributeName": "umbrella.firewall.traffic_type",
                            "attributeOperator": "=",
                            "attributeValue": "PRIVATE_NETWORK"
                        }
                    ],
                "ruleSettings": [
                        {
                            "settingName": "umbrella.logLevel",
                            "settingValue": "LOG_ALL",
                        }
                    ],
                "ruleMetadata": {
                "hitCountIntervalId": 3,
                "hitCountResetAt": 12345678901
                }
            })

            print("Creating policy")            
            response = requests.request("POST", url, headers=headers, data=payload)
            print("## Ruleset created successfully. ###")
            print("Rule Name:", response.json().get("ruleName"))
        except ( Exception) as ex:
            print("Exception:" ,ex)
