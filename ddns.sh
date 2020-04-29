#!/bin/bash

# change these 
zoneID=<Zone_ID>
dnsID=<DNS_ID>
email="<email_used_for_login>"
key=<Global_API_Key>
domain=<URL_of_Domain_whos_IP_Needs_Changing>

# fetch IP address
getIP=$(wget https://myip.dnsomatic.com/ -q -O -)
ip=`cat ip.txt`

if [ "$getIP" != "$ip" ]
  echo $getIP > ip.txt
  curl -X PUT "https://api.cloudflare.com/client/v4/zones/$zoneID/dns_records/$dnsID" -H "X-Auth-Email: $email" -H "X-Auth-Key: $key" -H "Content-Type: application/json" --data '{"type":"A","name":"'$domain'","content":"'$getIP'","ttl":120,"proxied":true}'
elif [ "$getIP = "$ip" ]
  echo "IP address hasn't changed since we ran last."
else
  echo "something is broken"
