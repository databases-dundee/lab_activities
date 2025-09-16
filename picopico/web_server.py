import network
import socket
from machine import Pin, ADC
from time import sleep
import machine
import rp2
import sys

ssid = 'Galaxy A20e5604'
password = 'ndja1086'

led = Pin(13,Pin.OUT)
temp_sensor = ADC(4)

def read_internal_temperature():
    # Read the raw ADC value
    adc_value = temp_sensor.read_u16()

    # Convert ADC value to voltage
    voltage = adc_value * (3.3 / 65535.0)

    # Temperature calculation based on sensor characteristics
    temperature_celsius = 27 - (voltage - 0.706) / 0.001721

    return temperature_celsius

def connect():
    seconds = 0
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(0.5)
        led.on()
        sleep(0.5)
        led.off()
        seconds +=1
        if seconds == 10:
            print('Timeout, failed to connect')
            sys.exit()
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(address)
    connection.listen(1)
    print(connection)
    print('Listening on port 80')
    return connection

def webpage(temperature,state):
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="./lighton">
    <input type="submit" value="Light on" />
    </form>
    <form action="./lightoff">
    <input type="submit" value="Light off" />
    </form>
    <p>LED is {state}</p>
    <p>Temperature is {temperature}</p>
    <form action="./close">
    <input type="submit" value="Close connection" />
    </form>
</body>
</html>
"""
    return str(html)

def serve(connection):
    #Start a web server
    state = 'OFF'
    
    led.off()
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        temperature = read_internal_temperature()
        html = webpage(temperature,state)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            led.on()
            state = "ON"
        elif request =='/lightoff?':
            led.off()
            state = "OFF"
        elif request == '/close?':
            client.close()
            connection.close()
            sys.exit()
        html = webpage(temperature,state)
        client.send(html)
        client.close()

ip = connect()
connection = open_socket(ip)
serve(connection)
