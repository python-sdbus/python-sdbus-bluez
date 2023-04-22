# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2023  Shin'ichiro Kawasaki <kawasaki@juno.dti.ne.jp>

# This example shows how to get properties of GATT services and characteristics
# of a BLE device.
# It does:
# - Discover the specified BLE device with BlueZ D-Bus Adapter API [1]
# - Connect to the device with BlueZ D-Bus Device API [2]
# - Get services and characteristics of the device with D-Bus introspection
# - Get properties of services and characteristics with BlueZ D-Bus GATT API [3]
# - Also read the characteristics if it has "read" flag.

# [1] https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/adapter-api.txt
# [2] https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/device-api.txt
# [3] https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/doc/gatt-api.txt

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from asyncio import run, sleep
from typing import Any

from sdbus import DbusInterfaceCommonAsync, SdBus, sd_bus_open_system

from sdbus_async.bluez.adapter_api import AdapterInterfaceAsync
from sdbus_async.bluez.device_api import DeviceInterfaceAsync
from sdbus_async.bluez.gatt_api import (
    GattCharacteristicInterfaceAsync,
    GattServiceInterfaceAsync,
)


def usage() -> None:
    print(f"Usage: {sys.argv[0]} DEV_ADDR")
    print("\tDEV_ADDR: Address of BLE device in fomrat XX:XX:XX:XX:XX:XX")
    exit(1)


DISCOVERY_SECONDS = 5


async def discover(dbus: SdBus) -> None:
    adapter = AdapterInterfaceAsync()
    adapter._connect('org.bluez', '/org/bluez/hci0', bus=dbus)
    try:
        await adapter.start_discovery()
        print(f"Wait discovery for {DISCOVERY_SECONDS} seconds")
        await sleep(DISCOVERY_SECONDS)
        await adapter.stop_discovery()
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failure in discovery: {e}")


async def print_props(prop_dict: dict[str, Any], indent: str) -> None:
    missing_properties = []
    for key in prop_dict.keys():
        try:
            print(f"{indent}{key}: {await prop_dict[key]}")
        except Exception:
            missing_properties.append(key)
    print("missing propeties:", missing_properties)


async def print_char_props(dbus: SdBus, dev_path: str,
                           service: str, char_str: str) -> None:
    path = dev_path + '/' + service + '/' + char_str
    char = GattCharacteristicInterfaceAsync()
    char._connect('org.bluez', path, bus=dbus)
    char_properties = {
        'UUID': char.uuid,
        'service': char.service_path,
        'value': char.value,
        'flags': char.flags,
        'write acquired': char.write_acquired,
        'notify acquired': char.notify_acquired,
        'notifying': char.notifying,
        'handle': char.handle,
        'MTU': char.mtu,
    }
    await print_props(char_properties, "    ")
    flags: list[str] = await char.flags
    for flag in flags:
        if flag == 'read':
            value = await char.read_value({})
            print(f"read value: {str(value)}")


async def print_service_props(dbus: SdBus, dev_path: str,
                              service_name: str) -> None:
    path = dev_path + '/' + service_name
    print('=============================================')
    print(f"service: {service_name}")
    service = GattServiceInterfaceAsync()
    service._connect('org.bluez', path, bus=dbus)
    service_properties = {
        'UUID': service.uuid,
        'device': service.device_path,
        'primary': service.primary,
        'includes paths': service.includes_paths,
        'handle': service.handle,
    }
    await print_props(service_properties, "")

    chars = await find_chars(dbus, path)
    if chars:
        for char in chars:
            print(f" {char}")
            await print_char_props(dbus, dev_path, service_name, char)
    return None


async def find_chars(dbus: SdBus, path: str) -> list[str]:
    # do D-Bus introspect to the service path and get characteristic paths
    adapter_introspect = DbusInterfaceCommonAsync()
    adapter_introspect._connect('org.bluez', path, bus=dbus)
    s = await adapter_introspect.dbus_introspect()
    parser = ET.fromstring(s)
    nodes = parser.findall("./node")
    if not nodes:
        print("characteristic not found")
        return []

    chars = []
    for node in nodes:
        chars.append(node.attrib['name'])
    return chars


async def find_service(dbus: SdBus, dev_path: str) -> list[str]:
    # do D-Bus introspect to the device path and get service paths under it
    adapter_introspect = DbusInterfaceCommonAsync()
    adapter_introspect._connect('org.bluez', dev_path, bus=dbus)
    s = await adapter_introspect.dbus_introspect()
    parser = ET.fromstring(s)
    nodes = parser.findall("./node")
    if not nodes:
        print("service not found")
        return []

    services = []
    for node in nodes:
        print(f" {node.attrib['name']}")
        services.append(node.attrib['name'])
    return services


async def main(dev_path: str) -> None:

    # connect to D-Bus
    dbus = sd_bus_open_system()
    device = DeviceInterfaceAsync()
    device._connect('org.bluez', dev_path, bus=dbus)

    # discover the specified BLE device
    await discover(dbus)

    # connect to the device
    print(f"Conneting to {dev_path}...")
    try:
        await device.connect()
    except NotImplementedError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        print(f"failed to connect: {e}")
        return
    print("Conneted")

    # Get services and characteristics and print their properties
    await sleep(2)
    for i in range(3):
        print("Find services...")
        services = await find_service(dbus, dev_path)
        if services:
            for service in services:
                await print_service_props(dbus, dev_path, service)
            break
            await sleep(1)

    # Clean up
    await device.disconnect()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    dev_path = '/org/bluez/hci0/dev_' + sys.argv[1].replace(":", "_")
    run(main(dev_path))
