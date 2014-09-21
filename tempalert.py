import time
import subprocess
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACd83301036cdec2851c4ef3e5e81bf855" 
AUTH_TOKEN = "295395bb3120356dab819872e65d9bd6" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
data = open("/home/root/tempdata.txt", "r")
p = subprocess.Popen(["tail", "-f", "/home/root/tempdata.txt"], stdout=subprocess.PIPE)
   
while True:
    point = p.stdout.readline()
    try:
        if (float(point) > 70):
            print point
	    client.messages.create(
              to="916-220-6131",
              from_="+15303874678",
              body="ALERT: Your car's temperature is %.2f. Come back quickly!" % float(point),
            )
            time.sleep(30) 


    except:
        pass
data.close()
