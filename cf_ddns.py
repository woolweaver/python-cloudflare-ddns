#!/usr/bin/env python3
from requests import get, put
from config.tokens import headers, url

# We need to find our IP
ip = get('https://diagnostic.opendns.com/myip') # fetch our current IP address

# Find Current Cloudflare domain settins
check_cf = get(url, headers=headers) # GET Info for the exact domain we want to update
check = check_cf.json() # convert to json

if check["success"] == True: # check for success

    our_current_ip = ip.text # we only need the text on the page

    current_cf_ip = check["result"]["content"] # Find the IP that Cloudflare has right now

    # Logic to check our IP Addresses
    if current_cf_ip == our_current_ip: # Check if our current IP matches what CF has
        print ("IP address hasn't changed") # If it matches we don't need to change it
        print ("Date last modified: " + check["result"]["modified_on"] + "\n")

    else: # It has changed so we need to update it

        updated_ip = our_current_ip # The updated IP we need to send to CF
        fqdn = check["result"]["name"] # Get FQDN for domain we are changing. We don't chage it, we just have to send it back to CF.
        ttl = check["result"]["ttl"] # Get TTL. We don't chage it, we just have to send it back to CF.
        record_type = check["result"]["type"] # get record type. We don't chage it, we just have to send it back to CF.
        proxy = check["result"]["proxied"] # get proxy status. We don't chage it, we just have to send it back to CF.

        # Create the data we need to pass to Cloudflare API
        data = { # https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

            "type":record_type, # record type A or AAA. We just pass what we got from CF.
            "name":fqdn, # FQDN (subdomain). We just pass what we got from CF.
            "content":updated_ip, # The IP address we fetched from https://diagnostic.opendns.com/myip
            "ttl":ttl, # set to 1 for AUTO. We just pass what we got from CF.
            "proxied":proxy # whether or not to proxy site thru cloudflare. Depends on your needs. True or False. We just pass what is already set.
            # See here --> https://support.cloudflare.com/hc/en-us/articles/200169156-Identifying-network-ports-compatible-with-Cloudflare-s-proxy
        }

        response = put(url, headers=headers, json=data) # Send Updated IP Address
        res = response.json() # response to json

        if res["success"] == True: # check for update success
            print ("IP Address changed to: " + res["result"]["content"]) # Print updated IP
            print ("Date lats modified: " + res["result"]["modified_on"] + "\n")

        else:
            print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors")
            print (res["errors"])

else:
    print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors")
    print (check["errors"])
