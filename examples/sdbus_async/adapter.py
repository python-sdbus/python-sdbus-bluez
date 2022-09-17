# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2022  Shin'ichiro Kawasaki <kawasaki@juno.dti.ne.jp>

from asyncio import new_event_loop

from sdbus import sd_bus_open_system

from sdbus_async.bluez.adapter_api import AdapterInterfaceAsync

dbus = sd_bus_open_system()
adapter = AdapterInterfaceAsync()
adapter._connect('org.bluez', '/org/bluez/hci0', bus=dbus)


async def print_properties() -> None:
    print('address: ', await adapter.address)
    print('address type: ', await adapter.address_type)
    print('name: ', await adapter.name)
    print('alias: ', await adapter.alias)
    print('class: ', await adapter.device_class)
    print('powered: ', await adapter.powered)
    print('discoverable: ', await adapter.discoverable)
    print('pairable: ', await adapter.pairable)
    print('pairable timeout: ', await adapter.pairable_timeout)
    print('discoverable timeout: ', await adapter.discoverable_timeout)
    print('discovering: ', await adapter.discovering)
    print('UUIDs: ', await adapter.uuids)
    print('modalias: ', await adapter.modalias)
    print('roles: ', await adapter.roles)


async def call_get_discovery_filters() -> None:
    try:
        filters = await adapter.get_discovery_filters()
        print(f"discovery filters: {filters}")
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failed to get discover filters: {e}")

TEST_UUID = '5261da01-fa7e-42ab-850b-7c80220097cc'


async def call_set_discovery_filter() -> None:
    try:
        filters = ({
            'RSSI': ('n', 10),
            'Transport': ('s', 'le'),
            'DuplicateData': ('b', False),
            'Discoverable': ('b', False),
        })
        print(f"setting filters: {filters}")
        await adapter.set_discovery_filter(properties=filters)
        print("filters set")
    except NotImplementedError as e:
        print(e)
    except Exception as e:
        print(e)
        print(f"failed to get discover filters: {e}")

loop = new_event_loop()

task_get_discovery_filters = loop.create_task(call_get_discovery_filters())
task_set_discovery_filter = loop.create_task(call_set_discovery_filter())
task_print_properties = loop.create_task(print_properties())

loop.run_forever()
