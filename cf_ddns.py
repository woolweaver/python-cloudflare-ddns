#!/usr/bin/env python3
from requests import get, put

# change these as you need please see icluded links for more details
zoneID = 'Zone-ID-For-Domain' # Getting Zone ID's https://api.cloudflare.com/#zone-list-zones
dnsID = 'DNS-ID-For-SubDomain' # Getting DNS record ID https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records
# Put together our Header
headers = {
    'X-Auth-Email': 'Your-Email-Address', # The email you use to login into Cloudflare
    'X-Auth-Key': 'Global-API-Key', # The Global API Key found here --> https://dash.cloudflare.com/profile/api-tokens
    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}
# We need to find our IP
ip = get('https://diagnostic.opendns.com/myip') # fetch our current IP address
current_ip = ip.text # we only need the text on the page
# Put together the data we need to send so we can update our IP address
data = {
    # https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record
    "type":"A", # record type A or AAA
    "name":"FQDN-That-You-Want-Update", # example.com
    "content":current_ip, # The IP address we fetched from https://diagnostic.opendns.com/myip
    "ttl":'1', # set to 1 for AUTO 
    "proxied":'false' # whether or not to proxy site thru cloudflare
}
# Put together our Cloudflare URL with zoneID and dnsID
url = "https://api.cloudflare.com/client/v4/zones/" + zoneID + "/dns_records/" + dnsID
# Find Current Cloudflare IP address
check_cf_IP = get(url, headers=headers) # GET Info for the exact domain we want to update
check = check_cf_IP.json() # convert to json
current_cf_ip = check["result"]["content"] # Find the IP Cloudflare has right now
# Show Our Current IP Addresses
print ("Current Cloudflare IP: " + current_cf_ip + "\n")
print ("Your Current IP  : " + current_ip + "\n")
# Logic to check our IP Addresses
if current_cf_ip == current_ip: # Check if our current IP matches what Cloudflare has
    print ("IP address hasn't changed")
else: # If it has Changed Update it
    response = put(url, headers=headers, json=data) # Send Updated IP Address
    res = response.json() # Get response to make sure update was succesful
    print ("IP Address changed to: " + res["result"]["content"]) # Print updated IP
