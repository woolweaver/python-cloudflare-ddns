#!/usr/bin/env python3

import requests

# change these as you need please see here for more deatils

# Getting Zone ID's https://api.cloudflare.com/#zone-list-zones

zoneID = 'Zone-ID-For-Domain'

# Getting DNS record ID https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records

dnsID = 'DNS-ID-For-SubDomain'

# Do Not Change This
url = "https://api.cloudflare.com/client/v4/zones/" + zoneID + "/dns_records/" + dnsID

# change these as you need please see here for more details

# https://dash.cloudflare.com/profile/api-tokens

# X-Auth-Key is your Global API Key

headers = {
    'X-Auth-Email': 'Your-Email-Address',
    'X-Auth-Key': 'Global-API-Key',
    'Content-Type': 'application/json'
}

ip = requests.get('https://diagnostic.opendns.com/myip')
new_ip = ip.text

# change these as you need please see here for more details

# https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

data = {
    "type":"A",
    "name":"FQDN-That-You-Want-Update",
    "content":new_ip,
    "ttl":'1',
    "proxied":'false'
}

check_cf_IP = requests.get(url, headers=headers)

check = check_cf_IP.json()

old_cf_ip = check["result"]["content"]

if old_cf_ip == new_ip:

    print ("Cloudflare IP: " + old_cf_ip + "\n")

    print ("Your IP: " + new_ip + "\n")

    print ("IP address hasn't changed")

else:
    response = requests.put(url, headers=headers, json=data)

    res = response.json()

    print ("Cloudflare IP: " + old_cf_ip + "\n")

    print ("Your IP: " + new_ip + "\n")

    print ("IP Address changed to: " + res["result"]["content"])
