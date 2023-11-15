import machine
from machine import Pin, UART
import time

rx_pin = Pin(1)
tx_pin = Pin(0)

# Initialize UART with specified baudrate and pins
uart = UART(0, baudrate=9600, tx=tx_pin, rx=rx_pin)


while True:
    # Read data from UART
    received_data = uart.read()

    # Check if data is received
    if received_data:
        # Decode received data from bytes to UTF-8 string
        decoded_data = received_data.decode('utf-8')

        # Print the decoded data
        print("Received data:", decoded_data)

    # Delay for 1 second before the next iteration
    time.sleep(1)

