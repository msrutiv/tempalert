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
        temp = float(point)
        if  (temp > 78):
            i=0
            print temp
            call = client.calls.create(    
            to="19162206131",              
            from_="+15303874678",          
            url="http://demo.twilio.com/docs/voice.xml",
            method="GET",                               
            fallback_method="GET",                      
            status_callback_method="GET",               
            record="false"                              
            )                                           
            print call.sid 
            while(i < 15):
                point = p.stdout.readline()
                time.sleep(1)
                i+=1 

        elif (temp > 74):
            print temp 
            i=0 
            client.messages.create(                                                
            to="916-220-6131",                                                   
            from_="+15303874678",                                                
            body="URGENT: Your car's temperature is %.2f. Come back NOW!" % temp,
            )
            while(i < 30):                                                      
                point = p.stdout.readline()                                     
                time.sleep(1)                                                   
                i+=1

        elif (temp > 70):
            print temp
            i=0
	    client.messages.create(
            to="916-220-6131",
            from_="+15303874678",
            body="ALERT: Your car's temperature is %.2f. Come back quickly!" % temp,
            )
            while(i < 40):                                                      
                point = p.stdout.readline()                                     
                time.sleep(1)                                                   
                i+=1   
    except:
        pass
data.close()
