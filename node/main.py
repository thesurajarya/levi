import network
import time
import secrets
import urequests

def connectToServer(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    
    while not wlan.isconnected():
        print(f"Connecting to {ssid}...")
        time.sleep(1)
        
    print(f"Connected to {ssid}!")
    print(wlan.ifconfig())
    time.sleep(3)
    try:
        webServer(url)
    except Exception as e:
        print(f"Error occured while trying to request webserver: {e}")
    
def webServer(url):
    print(f"Requesting to web service on {url}...")
    time.sleep(3)
    response = urequests.get(url)
    print(response.text)
    response.close()
    
   
def login(max_attempts=3):

    for attempt in range(max_attempts):

        user = input("User: ")
        password = input("Password: ")

        if user == secrets.user and password == secrets.loginPassword:
            connectToServer(secrets.ssid,secrets.password)
            return 0

        remaining = max_attempts - attempt - 1

        if remaining > 0:
            print(f"Wrong credentials! {remaining} chances left")

    print("Access denied")
    return 1

def main():
    login()

if __name__ == "__main__":
    url = "http://192.168.1.2:8000/"
    main()