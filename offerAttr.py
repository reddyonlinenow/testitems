#!/usr/bin/python
import sys
import requests
import json
import datetime

i = datetime.datetime.now()
ignoreAttr = ["align_channel_price", "availability_msg_flag"]
 
postApi_Prod='http://itemstoresetup.prod.itemstore.catdev.glb.prod.walmart.com/itemstore-item-setup-app/services/offer/'
input_url="http://itemstoresetup.prod.itemstore.catdev.glb.prod.walmart.com/itemstore-item-setup-app/services/offer/%s" % offer_id

postApi_Headers={"Content-Type":"application/json","Accept":"application/json","x-iso-ingestion-seller-id":"0","replace":"true"}
line=sys.argv[1]
offer_id=line.rstrip('\n')
# offer_id='00009F5DBB404FA6A7AF140ABDD3ACB6'
response = requests.request("GET",input_url)
json_response=json.loads(response.text)
json_response["payload"]["offerType"] = "ONLINE_AND_STORE"
marketAttributes=json_response["payload"]["marketAttributes"]
latestMA = [];

for i in xrange(len(marketAttributes)):
	if((marketAttributes[i]["attributeDefinition"]["attrName"]) not in ignoreAttr):
		latestMA.append(marketAttributes[i])
json_response["payload"]["marketAttributes"] = latestMA
postPayload=json.dumps(json_response['payload'])

#postPayload="{\"payload\":{\"offers\":["+payload.replace("\"marketAttributes\":[",stringToAppend)+"]}}"
# postPayload="{\"payload\":{\"offers\":["+payload.replace("\"offerType\": \"ONLINE_ONLY\",","\"offerType\": \"ONLINE_AND_STORE\",")+"]}}"

# postPayload="{\"payload\":{\"offers\":["+payload.replace("\"offerType\": \"ONLINE_ONLY\",","\"offerTypes\": \"ONLINE_AND_STORE\",").replace("\"marketAttributes\":[",stringToAppend)+"]}}"
print(postPayload)
# responsePost=requests.post(postApi_Prod,headers=postApi_Headers,data=postPayload)
# print(responsePost)

