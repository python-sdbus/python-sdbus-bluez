# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2022 igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (
    DbusInterfaceCommonAsync,
    dbus_method_async,
    dbus_property_async,
)


class GattServiceInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.GattService1',
):

    @dbus_property_async(
        property_signature='s',
        property_name='UUID',
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
        property_name='Device',
    )
    def device_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def primary(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ao',
        property_name='Includes',
    )
    def includes_paths(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
    )
    def handle(self) -> int:
        raise NotImplementedError


class GattCharacteristicInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.GattCharacteristic1',
):

    @dbus_method_async(
        input_signature='a{sv}',
        result_signature='ay',
    )
    async def read_value(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> bytes:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='aya{sv}',
    )
    async def write_value(
        self,
        value: bytes,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{sv}',
        result_signature='hq',
    )
    async def acquire_write(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> Tuple[int, int]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{sv}',
        result_signature='hq',
    )
    async def acquire_notify(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> Tuple[int, int]:
        raise NotImplementedError

    @dbus_method_async()
    async def start_notify(self) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def stop_notify(self) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def confirm(self) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        property_name='UUID',
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
        property_name='Service',
    )
    def service_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def value(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def write_acquired(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def notify_acquired(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def notifying(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def flags(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
    )
    def handle(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
        property_name='MTU',
    )
    def mtu(self) -> int:
        raise NotImplementedError


class GattDescriptorInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.GattDescriptor1',
):

    @dbus_method_async(
        input_signature='a{sv}',
        result_signature='ay',
    )
    async def read_value(
        self,
        options: Dict[str, Tuple[str, Any]],
    ) -> bytes:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='aya{sv}',
    )
    async def write_value(
        self,
        value: bytes,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        property_name='UUID',
    )
    def uuid(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
        property_name='Characteristic',
    )
    def characteristic_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def value(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def flags(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
    )
    def handle(self) -> int:
        raise NotImplementedError
