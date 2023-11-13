**SH1106 OLED Display Integration for Multiple Devices with the Same I2C Address**
**Overview**
This repository provides code snippets and methods for effectively using two SH1106 OLED displays that share the same I2C address. The challenge of handling devices with identical addresses is a common scenario in electronics projects, and I tried variety of solutions to address this issue.

Effective Methods I Came Across:
1. I2C Multiplexer (Using TCA9548A)
Utilize an I2C multiplexer, such as the TCA9548A, to manage up to 8 I2C devices with unique/same addresses. This method allows for integration of multiple SH1106 OLED displays without conflicts.

2. Dual I2C Buses (Raspberry Pi Pico W)
Taking advantage of the dual I2C buses available on the Raspberry Pi Pico W. By utilizing both Channel 0 and Channel 1, you can independently connect each SH1106 OLED display, overcoming address conflicts.

3. Manual Address Modification(For those comfortable with hardware adjustments):
This involves desoldering and soldering resistors located behind the display.

NOTE: Kindly download the required libraries available across the Github community and use these codes with them. 
