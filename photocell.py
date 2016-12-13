import time
import readadc

# temperature sensor middle pin connected channel 0 of mcp3008
photocell_pin = 1
readadc.initialize()

#the main sensor reading and plotting loop
while True:
    sensor_data = readadc.readadc(photocell_pin,
                                  readadc.PINS.SPICLK,
                                  readadc.PINS.SPIMOSI,
                                  readadc.PINS.SPIMISO,
                                  readadc.PINS.SPICS)

	photocell = sensor_data
	photocell = 1023 - photocell

    time.sleep(0.5)