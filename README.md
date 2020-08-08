Cloudflare Dynamic DNS via Python 3

[https://github.com/mwoolweaver/Cloudflare-Dynamic-DNS](https://github.com/mwoolweaver/Cloudflare-Dynamic-DNS)

## How To Use 

In [config/config.py](https://github.com/mwoolweaver/Cloudflare_Dynamic_DNS/blob/master/config/config.py) you will see the following variables. Make sure you change these. I have included some information about how to get these

### 1. Install dependencies
```
pip3 install requests
```

### 2. Getting API Tokens

[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

```
headers = {
    'X-Auth-Email': 'Your-Email-Address',
    'X-Auth-Key': 'Global-API-Key',
    'Content-Type': 'application/json'
}
```

### 3. Getting Zone ID's 

[https://api.cloudflare.com/#zone-list-zones](https://api.cloudflare.com/#zone-list-zones)

```
zoneID = 'Zone-ID-For-Domain'
```

### 4. Getting DNS Record ID 

[https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

```
dnsID = 'DNS-ID-For-SubDomain'
```
