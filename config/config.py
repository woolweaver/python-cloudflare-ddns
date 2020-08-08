#!/usr/bin/env python3

# change these as you need please see included links for more details

zoneID = 'Zone-ID-For-Domain' # Getting Zone ID's https://api.cloudflare.com/#zone-list-zones

dnsID = 'DNS-ID-For-SubDomain' # Getting DNS Record ID's https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records

# Put together our Header

headers = {
    'X-Auth-Email': 'Your-Email-Address', # The email you use to login into Cloudflare.

    'X-Auth-Key': 'Global-API-Key', # The Global API Key found here --> https://dash.cloudflare.com/profile/api-tokens

    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}
