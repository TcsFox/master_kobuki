#!/usr/bin/env python3

""" Advertises a BLE beacon for 15 seconds """

import time

from bluetooth.ble import BeaconService

service = BeaconService()

service.start_advertising("")
