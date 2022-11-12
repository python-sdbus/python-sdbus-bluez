# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2022  Shin'ichiro Kawasaki <kawasaki@juno.dti.ne.jp>

import sys
from asyncio import new_event_loop

from sdbus import sd_bus_open_system

from sdbus_async.bluez.device_api import DeviceInterfaceAsync


def usage() -> None:
    print(f"Usage: {sys.argv[0]} DEV_ADDR")
    print("Show properties of the device specified with DEV_ADDR")
    print("\tDEV_ADDR: e.g. 01:23:45:67:89:AB")
    exit(1)


if len(sys.argv) != 2:
    usage()

DEV_ADDR = sys.argv[1]
DEV_PATH = '/org/bluez/hci0/dev_' + DEV_ADDR.replace(":", "_")

print(DEV_PATH)

dbus = sd_bus_open_system()
device = DeviceInterfaceAsync()
device._connect('org.bluez', DEV_PATH, bus=dbus)

device_properties = {
    'device class': device.device_class,
    'address': device.address,
    'address type': device.address_type,
    'name': device.name,
    'icon': device.icon,
    'UUIDs': device.uuids,
    'paired': device.paired,
    'connected': device.connected,
    'trusted': device.trusted,
    'blocked': device.blocked,
    'wake allowed': device.wake_allowed,
    'alias': device.alias,
    'adapter': device.adapter,
    'legacy pairing': device.legacy_pairing,
    'modalias': device.modalias,
    'RSSI': device.rssi,
    'tx power': device.tx_power,
    'manufacturer data': device.manufacturer_data,
    'service data': device.service_data,
    'services resolved': device.services_resolved,
    'advertising flags': device.advertising_flags,
    'advertising data': device.advertising_data,
}
missing_properties = []


async def print_properties() -> None:
    for key in device_properties.keys():
        try:
            print(f"{key}: {await device_properties[key]}")
        except Exception:
            missing_properties.append(key)
    print("missing propeties:", missing_properties)

loop = new_event_loop()
task = loop.create_task(print_properties())
loop.run_until_complete(task)
