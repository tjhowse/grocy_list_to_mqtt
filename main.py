#!/usr/local/bin/python3

import time
import paho.mqtt.client as mqtt
from grocy_api import grocy_api
try:
    from secrets_real import *
except ImportError:
    from secrets import *
class GrocyToThermalPrinter:
    def __init__(self):
        self.grocy = grocy_api(grocy_api_key, grocy_domain)
        self.grocy.sync()
        # print(self.grocy.get_shopping_list_sorted_by_aisleOrder())
        # return

        self.mqtt = mqtt.Client()
        self.mqtt.username_pw_set(mqtt_user, password=mqtt_pw)
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_message = self.on_message
        self.mqtt.connect(mqtt_host, mqtt_port, 60)
        # self.mqtt.loop_start()
        # self.mainloop()
        self.mqtt.loop_forever()

    def mainloop(self):
        print("Starting main loop")
        while True:
            time.sleep(1)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.mqtt.subscribe(mqtt_topic_button)

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        if msg.topic == mqtt_topic_button:
            self.button_pressed(msg.payload)

    def button_pressed(self, payload):
        self.grocy.sync()
        for line in self.get_shopping_list():
            self.mqtt.publish(mqtt_topic_print, line)

    def get_shopping_list(self):
        sl = list(self.grocy.get_shopping_list_sorted_by_aisleOrder())
        print(sl)
        return sl


if __name__ == "__main__":
    gttp = GrocyToThermalPrinter()
