# Cloudflare Dynamic DNS
Cloudflare Dynamic DNS in Python3

[https://github.com/mwoolweaver/Cloudflare-Dynamic-DNS](https://github.com/mwoolweaver/Cloudflare-Dynamic-DNS)

## How To Use 

At the top of the python script ([cf_ddns.py](https://github.com/mwoolweaver/Cloudflare_Dynamic_DNS/blob/master/cf_ddns.py)) you will see the following variables. Make sure you change these. I have included some information about how to get these

### 1. Getting API Tokens

[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

```
headers = {
    'X-Auth-Email': 'Your-Email-Address',
    'X-Auth-Key': 'Global-API-Key',
    'Content-Type': 'application/json'
}
```

### 2. Getting Zone ID's 

[https://api.cloudflare.com/#zone-list-zones](https://api.cloudflare.com/#zone-list-zones)

```
zoneID = 'Zone-ID-For-Domain'
```

### 3. Getting DNS Record ID 

[https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

```
dnsID = 'DNS-ID-For-SubDomain'
```

### 4. Setting Domain That Needs Changed

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
