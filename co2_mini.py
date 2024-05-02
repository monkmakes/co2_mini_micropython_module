from microbit import uart, pin0, pin1, display
from time import sleep

class CO2Mini:
    """A module for the MonkMakes CO2 Mini."""
    def __send_message(self, command):
        uart.write(command)
        sleep(0.1)
        
    def __get_sensor_value(self, command):
        self.__send_message(command)
        response_str = uart.readline()
        if response_str != None:
            response = response_str.decode()
            # e.g. c=4999 or t=12.34
            if len(response) > 2:
                c_str = response[2:]
                #display.show(c_str)
                return float(c_str)
        return -1
    
    def start(self):
        """Redirect the uart to pins 0 and 1"""
        uart.init(baudrate=9600, tx=pin0, rx=pin1)

    def co2(self):
        """Return the CO2 concentration in parts per million (ppm)"""
        return int(self.__get_sensor_value('c'))

    def temp(self):
        """Return the temperature in degrees C"""
        return self.__get_sensor_value('t')

    def humidity(self):
        """Relative humidity as a percentage"""
        return self.__get_sensor_value('h')
        
    def led_on(self):
        """Turn the built-in RGB LED on to show the CO2 status"""
        self.__send_message('L')

    def led_off(self):
        """Turn the built-in RGB LED off"""
        self.__send_message('l')

    def set_altitude(self, altitude_m):
        """Set the altitude in metres, for more accurate CO2 measurement"""
        self.__send_message('m=' + str(altitude_m))

    def calibrate400(self):
        """Manually callibrate to 400 ppm"""
        self.__send_message('k')

    def factory_reset(self):
        """Factory reset of all sensor settings"""
        self.__send_message('f')

    def firmware_version(self):
        """Return the firmware version of the MonkMakes CO2 Mini"""
        return int(self.__get_sensor_value('v'))
        