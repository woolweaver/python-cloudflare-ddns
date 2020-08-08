#!/usr/bin/env python3

from requests import get, put

# change these as you need please see here for more deatils

zoneID = 'Zone-ID-For-Domain' # Getting Zone ID's https://api.cloudflare.com/#zone-list-zones

dnsID = 'DNS-ID-For-SubDomain' # Getting DNS record ID https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records

headers = {
    'X-Auth-Email': 'Your-Email-Address', # The email you use to login into Cloudflare
    'X-Auth-Key': 'Global-API-Key', # The Global API Key found here --> https://dash.cloudflare.com/profile/api-tokens
    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}

ip = get('https://diagnostic.opendns.com/myip') # fetch our current IP address
current_ip = ip.text

# https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

data = {
    "type":"A", # record type A or AAA
    "name":"FQDN-That-You-Want-Update", # example.com
    "content":current_ip, # The IP address we just fetched from opendns.com
    "ttl":'1', # set to 1 for AUTO 
    "proxied":'false' # whether or not to proxy site thru cloudflare
}

# Put together Cloudflare URL with zoneID and dnsID
url = "https://api.cloudflare.com/client/v4/zones/" + zoneID + "/dns_records/" + dnsID

check_cf_IP = get(url, headers=headers) # GET Info for the exact domain we want to update
check = check_cf_IP.json() # convert to json
old_cf_ip = check["result"]["content"] # Find the IP Cloudflare has right now

print ("Old Cloudflare IP: " + old_cf_ip + "\n")
print ("Your Current IP  : " + current_ip + "\n")

if old_cf_ip == current_ip: # Check if our current IP matches what Cloudflare has
    print ("IP address hasn't changed")

else:
    response = put(url, headers=headers, json=data) # Send Updated IP Address
    res = response.json()
    print ("IP Address changed to: " + res["result"]["content"])
