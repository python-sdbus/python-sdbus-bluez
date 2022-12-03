# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2022  Shin'ichiro Kawasaki <kawasaki@juno.dti.ne.jp>

# This example shows how to connect to Bluetooth devices using BlueZ D-Bus
# Profile API [*]. The API provides Profile Manager interface and Profile
# interface. When the application request BlueZ to connect to a device, BlueZ
# open a file descriptor to send and receive to the device and pass the file
# descriptor to the application. To receive the file descriptor, the
# application prepares a D-Bus object with Profile interface. Steps to take
# are as follows:
#
# 1) Create Profile object with new_connection() call back
# 2) Register the Profile object through Profile Manager
# 3) Request connect to the Bluetooth device with Device API
# 4) BlueZ calls new_connect() for the Profile object with a file descriptor
# 5) In new_connect(), duplicate the file descriptor for communication
# 6) Write the file descriptor to send data to the Bluetooth device, or
#    read the file descriptor to receive data from the Bluetooth device
#
# In this example, connect to a Bluetooth RFCOMM device with Serial Port
# service.

from __future__ import annotations

import sys
from asyncio import run, sleep
from os import dup, fdopen
from typing import Any, Dict, Tuple

from sdbus import dbus_method_async_override, sd_bus_open_system

from sdbus_async.bluez.device_api import DeviceInterfaceAsync
from sdbus_async.bluez.profile_api import (
    ProfileInterfaceAsync,
    ProfileManagerInterfaceAsync,
)


def usage() -> None:
    print(f"Usage: {sys.argv[0]} DEV_ADDR BYTE1 [BYTE2...]")
    print("\tConnect to serial port service of the Bluetooth RFCOMM device")
    print("\tspecified with DEV_ADDR and send specified bytes to the device.")
    print("\t\tDEV_ADDR: e.g. 01:23:45:67:89:AB")
    print("\t\tBYTE1 [BYTE2...]: e.g. 0x02 0x00 0x01 0x9B")
    exit(1)


if len(sys.argv) < 3:
    usage()

DEV_ADDR = sys.argv[1]
DEV_PATH = '/org/bluez/hci0/dev_' + DEV_ADDR.replace(":", "_")
BYTES_TO_SEND = [int(x, 0) for x in sys.argv[2:]]
# Serial port service UUID
SERVICE_UUID = '00001101-0000-1000-8000-00805f9b34fb'


class RFCOMMProfileAsync(ProfileInterfaceAsync):

    @dbus_method_async_override()
    async def release(
            self,
    ) -> None:
        return

    @dbus_method_async_override()
    async def new_connection(
            self,
            device: str,
            fd: int,
            fd_properties: Dict[str, Tuple[str, Any]],
    ) -> None:
        """Receive the file descriptor that BlueZ prepared to communicate with
        the Serial Port service of the RFCOMM Bluetooth Device. Duplicate the
        file descriptor since it will not be valid after this function call."""
        print(f"Connecting to device: {device}")
        self.fd = dup(fd)

    @dbus_method_async_override()
    async def request_disconnection(
            self,
            device: str,
    ) -> None:
        print(f"Disconnecting device: {device}")


async def main() -> None:

    # connect to D-Bus
    dbus = sd_bus_open_system()
    profile_manager = ProfileManagerInterfaceAsync()
    profile_manager._connect('org.bluez', '/org/bluez', bus=dbus)
    device = DeviceInterfaceAsync()
    device._connect('org.bluez', DEV_PATH, bus=dbus)

    # Create RFCOMM profile object
    export_object = RFCOMMProfileAsync()
    export_object.export_to_dbus('/org/test', dbus)

    # Register the RFCOMM profile object
    await profile_manager.register_profile('/org/test',
                                           SERVICE_UUID,
                                           {'Name': ('s', 'foo'),
                                            'Role': ('s', "client"),
                                            'Service': ('s', SERVICE_UUID),
                                            'Channel': ('i', 0),
                                            'AutoConnect': ('b', True),
                                            })

    # Connect to serial port service
    try:
        await device.connect_profile(SERVICE_UUID)
    except NotImplementedError as e:
        print(e)
        return
    except Exception as e:
        print(e)
        print(f"failed to connect: {e}")
        return

    # Send and receive data
    fp = fdopen(export_object.fd, mode='r+b', buffering=0, newline=None)

    msg = bytes(BYTES_TO_SEND)
    print("Sending bytes: ", msg)
    fp.write(msg)

    await sleep(1)

    received_bytes = fp.read()
    print("Received bytes: ", received_bytes)

    # Clean up
    await device.disconnect()
    await profile_manager.unregister_profile('/org/test')

run(main())
