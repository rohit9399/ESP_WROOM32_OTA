import network
import time
import config

def connect():

    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if wlan.isconnected():
        print("Already Connected")
        print(wlan.ifconfig())
        return wlan

    print("Connecting...")

    wlan.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

    timeout = 20

    while timeout > 0:

        if wlan.isconnected():
            print("Connected")
            print("IP :", wlan.ifconfig()[0])
            return wlan

        timeout -= 1
        print(".", end="")
        time.sleep(1)

    print("WiFi Failed")

    return None
