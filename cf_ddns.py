#!/usr/bin/env python3
from requests import get, put
from config.tokens import headers, url
from config.convert_DT import con_DT # used to print date/time in local format

# Find Current CF domain settings
check_cf = get(url, headers=headers) # GET Info for the exact domain we want to update.
check = check_cf.json() # convert to json

if check["success"] == True: # check for success

    # We need to find our IP
    ip = get('https://diagnostic.opendns.com/myip') # fetch our current IP address
    our_current_ip = ip.text # we only need the text on the page

    current_cf_ip = check["result"]["content"] # Find the IP that Cloudflare has right now

    # Logic to check our IP Addresses
    if current_cf_ip == our_current_ip: # Check if our current IP matches what CF has.
        print ("IP address hasn't changed") # If it matches we don't need to change it.
        print ("Date last modified: " + con_DT(check["result"]["modified_on"]) + "\n") # Print the date it was last modified.


    else: # It has changed so we need to update it

        updated_ip = our_current_ip # The updated IP we need to send to CF

        fqdn = check["result"]["name"] # Get FQDN for domain we are changing. We don't chage it, we just have to send it back to CF.
        ttl = check["result"]["ttl"] # Get TTL. We don't chage it, we just have to send it back to CF.
        record_type = check["result"]["type"] # get record type. We don't chage it, we just have to send it back to CF.
        proxy = check["result"]["proxied"] # get proxy status. We don't chage it, we just have to send it back to CF.

        # Create the data we need to pass to CF API
        data = { # https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record

            "type":record_type, # record type A or AAA. We just pass what we got from CF.
            "name":fqdn, # FQDN (subdomain). We just pass what we got from CF.
            "content":updated_ip, # The IP address we fetched from https://diagnostic.opendns.com/myip
            "ttl":ttl, # set to 1 for AUTO. We just pass what we got from CF.
            "proxied":proxy # whether or not to proxy site thru cloudflare. Depends on your needs. True or False. We just pass what is already set.
            # See here --> https://support.cloudflare.com/hc/en-us/articles/200169156-Identifying-network-ports-compatible-with-Cloudflare-s-proxy
        }

        update = put(url, headers=headers, json=data) # Send Updated IP Address
        upD = update.json() # response to json

        if upD["success"] == True: # check for update success

            # Print data returned to us by CF API
            print ("IP Address changed to: " + upD["result"]["content"]) # Print updated IP
            print ("Date lats modified: " + con_DT(upD["result"]["modified_on"]) + "\n") # Print the date it was last modified.

        else: 
            print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors") # Give CF API info about errors.
            print (upD["errors"]) # Print error returned to us by CF API.

else:
    print ("Check your data.\nPlease see https://api.cloudflare.com/#dns-records-for-a-zone-errors") # Give CF API info about errors.
    print (check["errors"]) # Print error returned to us by CF API.
