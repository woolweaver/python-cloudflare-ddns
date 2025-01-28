Cloudflare Dynamic DNS via Python 3

[https://github.com/woolweaver-bid/python-cloudflare-ddns](https://github.com/woolweaver-bid/python-cloudflare-ddns)

## How To Use 

### 1. Get Code
```
git clone https://github.com/mwoolweaver/python-cloudflare-ddns.git
```

### 2. Install dependencies
```
cd python-cloudflare-ddns
pip3 install -r requirements.txt
```

-------

### 3. Getting/Creating API Tokens

In [config/tokens.py](https://github.com/woolweaver-bid/python-cloudflare-ddns/blob/master/config/tokens.py) you will see the following variables. Make sure you change these.     
I have included some information about [how to get these](https://dash.cloudflare.com/profile/api-tokens).

```
headers = {

    'Authorization': 'Your-API-Token', # Get/Create API token here ---> https://dash.cloudflare.com/profile/api-tokens

    'Content-Type': 'application/json' # Type of data to be passed must be application/json
}
```

### 4. Getting Zone ID's 

[https://api.cloudflare.com/#getting-started-resource-ids](https://api.cloudflare.com/#getting-started-resource-ids)

```
zoneID = 'Zone-ID-For-Domain' # Zone ID for domain we need to change
```

### 5. Getting DNS Record ID 

[https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records](https://api.cloudflare.com/#dns-records-for-a-zone-list-dns-records)

```
dnsID = 'DNS-ID-For-SubDomain' # DNS ID for subdomain we want to change
```

### 6. Runnig
```
./cf_ddns.py
```
