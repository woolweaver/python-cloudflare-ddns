# Cloudflare Dynamic DNS
[Cloudflare Dynamic DNS](https://github.com/mwoolweaver/Cloudflare-Dynamic-DNS) in Python3

## How To Use 

At the top of the python script ([cf_ddns](https://github.com/mwoolweaver/Cloudflare_Dynamic_DNS/blob/master/cf_ddns.py)) you will see the following variables. Make sure you change these. I have included some information about how to get these

### Getting Zone ID's 

[https://api.cloudflare.com/#zone-list-zones](https://api.cloudflare.com/#zone-list-zones)

```
zoneID = 'Zone-ID-For-Domain'
```

### Getting DNS Record ID 

[https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

```
dnsID = 'DNS-ID-For-SubDomain'
```

### Getting API Tokens

[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

```
headers = {
    'X-Auth-Email': 'Your-Email-Address',
    'X-Auth-Key': 'Global-API-Key',
    'Content-Type': 'application/json'
}
```

### Setting Domain That Needs Changed

[https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record](https://api.cloudflare.com/#dns-records-for-a-zone-update-dns-record)

```
data = {
    "type":"A",
    "name":"FQDN-That-You-Want-Update",
    "content":new_ip,
    "ttl":'1',
    "proxied":'false'
}
```
