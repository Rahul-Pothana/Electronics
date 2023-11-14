# Import the required libraries
from machine import Pin, I2C
import sh1106

'''
there are two ways in which you can pass your i2c pins to initialise the i2c bus,
have used one here and other while initialising channel 1 (notice the difference)
'''
sda = machine.Pin(8)
scl = machine.Pin(9)

# Initialize the first I2C bus
i2c = I2C(0, scl=scl, sda=sda, freq=400000)

# Create an instance of SH1106 OLED display for the first bus
oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)


# Initialize the second I2C bus
i2c1 = I2C(1, scl=machine.Pin(7), sda=machine.Pin(6), freq=400000)

# Create an instance of SH1106 OLED display for the second bus
oled1 = sh1106.SH1106_I2C(128, 64, i2c1, Pin(4), 0x3c)

# Configure and display content on the first OLED display
oled.sleep(False)
oled.rotate(True)
oled.fill(0) # Fills the display with black color. Use oled.fill(1) for white color. Adjust text color accordingly.
oled.text('test.....', 0, 0)
oled.show() 

# Configure and display content on the second OLED display
oled1.sleep(False)
oled1.rotate(True)
oled1.fill(0)  
oled1.text('testing display 2.......', 5, 5)
oled1.show()  # Update the display
