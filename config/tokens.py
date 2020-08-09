#!/usr/bin/env python3

# Change these as you need. 

# Please see included links for more details.

headers = { # Put together the Header we send to CF.

    'Authorization': 'Your-API-Token', # Get/Create API token here ---> https://dash.cloudflare.com/profile/api-tokens

    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}

# Getting Zone ID's       ---> https://api.cloudflare.com/#getting-started-resource-ids
zoneID = 'Zone-ID-For-Domain'

# Getting DNS Record ID's ---> https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records
dnsID = 'DNS-ID-For-SubDomain'

# <----- DO NOT CHANGE ----->
# Put together our CF URL with our zoneID and our dnsID --> https://api.cloudflare.com/#dns-records-for-a-zone-dns-record-details
url = "https://api.cloudflare.com/client/v4/zones/" + zoneID + "/dns_records/" + dnsID