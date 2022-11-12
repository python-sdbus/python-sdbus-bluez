# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2022  Shin'ichiro Kawasaki <kawasaki@juno.dti.ne.jp>

import sys
import xml.etree.ElementTree as ET
from asyncio import new_event_loop, sleep

from sdbus import sd_bus_open_system
from sdbus.dbus_proxy_async_interfaces import DbusIntrospectableAsync

from sdbus_async.bluez.adapter_api import AdapterInterfaceAsync

dbus = sd_bus_open_system()
adapter = AdapterInterfaceAsync()
adapter._connect('org.bluez', '/org/bluez/hci0', bus=dbus)
adapter_introspect = DbusIntrospectableAsync()
adapter_introspect._connect('org.bluez', '/org/bluez/hci0', bus=dbus)


async def call_start_discovery() -> None:
    try:
        await adapter.start_discovery()
        print(f"Wait discovery for {DISCOVERY_SECONDS} seconds")
        await sleep(DISCOVERY_SECONDS)
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failed to start discovery: {e}")


async def call_stop_discovery() -> None:
    try:
        await adapter.stop_discovery()
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failed to stop discovery: {e}")


async def call_introspect() -> None:
    try:
        s = await adapter_introspect.dbus_introspect()
        parser = ET.fromstring(s)
        nodes = parser.findall("./node")
        if not nodes:
            print("device not found")
        else:
            print(f"{len(nodes)} device(s) found")
            for node in nodes:
                print(f"  {node.attrib['name']}")
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failed to stop discovery: {e}")


def usage() -> None:
    print(f"Usage: {sys.argv[0]} [OPTIONS]")
    print("Call bluez adapter dicovery API and list found devices")
    print("\tOPTIONS: -h:\t\tshow this help")
    print("\t         -t TIME:\trun disvoery for TIME seconds")
    exit(1)


DISCOVERY_SECONDS = 5
argv = sys.argv
if len(argv) == 2 and argv[1] == '-h':
    usage()
elif len(argv) == 3 and argv[1] == '-t':
    DISCOVERY_SECONDS = int(argv[2])
elif len(argv) != 1:
    usage()

loop = new_event_loop()

print("Starting discovery...")
task = loop.create_task(call_start_discovery())
loop.run_until_complete(task)

task = loop.create_task(call_introspect())
loop.run_until_complete(task)

task = loop.create_task(call_stop_discovery())
loop.run_until_complete(task)

print("Discovery stopped")
