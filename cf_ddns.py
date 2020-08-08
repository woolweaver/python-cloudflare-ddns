#!/usr/bin/env python3
from requests import get, put
# change these as you need please see included links for more details
zoneID = 'Zone-ID-For-Domain' # Getting Zone ID's https://api.cloudflare.com/#zone-list-zones
dnsID = 'DNS-ID-For-SubDomain' # Getting DNS Record ID's https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records
# Put together our Header
headers = {
    'X-Auth-Email': 'Your-Email-Address', # The email you use to login into Cloudflare
    'X-Auth-Key': 'Global-API-Key', # The Global API Key found here --> https://dash.cloudflare.com/profile/api-tokens
    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}

# We need to find our IP
ip = get('https://diagnostic.opendns.com/myip') # fetch our current IP address
current_ip = ip.text # we only need the text on the page

# Put together our Cloudflare URL with our zoneID and our dnsID
url = "https://api.cloudflare.com/client/v4/zones/" + zoneID + "/dns_records/" + dnsID

# Find Current Cloudflare IP address
check_cf_IP = get(url, headers=headers) # GET Info for the exact domain we want to update
check = check_cf_IP.json() # convert to json

if check["success"] == True: # check for success 
    current_cf_ip = check["result"]["content"] # Find the IP that Cloudflare has right now
    fqdn = check["result"]["name"] # Get FQDN for domain we are changing
    ttl = check["result"]["ttl"] # Get TTL
    record_type = check["result"]["type"] # get record type 
    proxy = check["result"]["proxied"] # get proxy status
    data = {
        # https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record
        "type":record_type, # record type A or AAA. We just pass what is alreay set.
        "name":fqdn, # We just pass what is alreay set.
        "content":current_ip, # The IP address we fetched from https://diagnostic.opendns.com/myip
        "ttl":ttl, # set to 1 for AUTO. We just pass what is alreay set.
        "proxied":proxy # whether or not to proxy site thru cloudflare. Depends on your needs. True or False. We just pass what is already set.
        # See here --> https://support.cloudflare.com/hc/en-us/articles/200169156-Identifying-network-ports-compatible-with-Cloudflare-s-proxy
    }
    # Show Our Current IP Addresses
    print ("Current Cloudflare IP: " + current_cf_ip + "\n")
    print ("Your Current IP  : " + current_ip + "\n")
    # Logic to check our IP Addresses
    if current_cf_ip == current_ip: # Check if our current IP matches what Cloudflare has
        print ("IP address hasn't changed") # If it matches we don't need to change it
    else: # If it has changed update it
        response = put(url, headers=headers, json=data) # Send Updated IP Address
        res = response.json() # response to json
        if res["success"] == True: # check for success
            print ("IP Address changed to: " + res["result"]["content"]) # Print updated IP
        else:
            print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors")
            print (res["errors"])
else:
    print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors")
    print (check["errors"])