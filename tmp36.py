import time
import readadc

# temperature sensor middle pin connected channel 0 of mcp3008
sensor_pin = 0
readadc.initialize()

#the main sensor reading and plotting loop
while True:
    sensor_data = readadc.readadc(sensor_pin,
                                  readadc.PINS.SPICLK,
                                  readadc.PINS.SPIMOSI,
                                  readadc.PINS.SPIMISO,
                                  readadc.PINS.SPICS)

    millivolts = sensor_data * (3300.0 / 1024.0)
    # 10 mv per degree
    temp_C = ((millivolts - 100.0) / 10.0) - 40.0
    # show only one decimal place for temprature and voltage readings
    temp_C = "%.1f" % temp_C
    print(temp_C)

    time.sleep(0.5)