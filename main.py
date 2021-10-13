#!/usr/local/bin/python3

import paho.mqtt.client as mqtt
from grocy_api import grocy_api
from secrets import grocy_api_key, grocy_domain

class GrocyToThermalPrinter:
    def __init__(self):
        self.grocy = grocy_api(grocy_domain, grocy_api_key)
        self.grocy.sync()
        self.get_shopping_list()

    def get_shopping_list(self):
        sl = list(self.grocy.get_shopping_list())
        print(sl)


if __name__ == "__main__":
    gttp = GrocyToThermalPrinter()
