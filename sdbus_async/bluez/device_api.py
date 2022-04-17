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


class DeviceInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Device1',
):

    @dbus_method_async()
    async def connect(self) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def disconnect(self) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def connect_profile(
        self,
        uuid: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def disconnect_profile(
        self,
        uuid: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def pair(self) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def cancel_pairing(self) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def address(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def address_type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def icon(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def device_class(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='q',
    )
    def appearance(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        property_name='UUIDs'
    )
    def uuids(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def paired(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def connected(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def trusted(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def blocked(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def wake_allowed(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def alias(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
    )
    def adapter(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def legacy_pairing(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def modalias(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='n',
        property_name='RSSI',
    )
    def rssi(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='n',
    )
    def tx_power(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a{qv}',
    )
    def manufacturer_data(self) -> Dict[int, Tuple[str, Any]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a{sv}',
    )
    def service_data(self) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def services_resolved(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def advertising_flags(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a{sv}',
    )
    def advertising_data(self) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError
