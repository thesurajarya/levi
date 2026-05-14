import network
import time
import secrets

def connectToServer(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    
    while not wlan.isconnected():
        print(f"Connecting to {ssid}...")
        time.sleep(1)
        
    print(f"Connected to {ssid}!")
    print(wlan.ifconfig())
    try:
        webServer()
    except Exception as e:
        print(f"Error occured while trying to request webserver: {e}")
    
def webServer():
    print("Requesting to web service")
    
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
    main()