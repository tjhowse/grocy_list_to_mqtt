#!/usr/local/bin/python3

import paho.mqtt.client as mqtt
from grocy_api import grocy_api
try:
    from secrets_real import grocy_api_key, grocy_domain
except ImportError:
    from secrets import grocy_api_key, grocy_domain
class GrocyToThermalPrinter:
    def __init__(self):
        self.grocy = grocy_api(grocy_api_key, grocy_domain)
        self.grocy.sync()
        self.get_shopping_list()

    def get_shopping_list(self):
        sl = list(self.grocy.get_shopping_list())
        print(sl)


if __name__ == "__main__":
    gttp = GrocyToThermalPrinter()
