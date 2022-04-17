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


class AdapterInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Adapter1',
):

    @dbus_method_async()
    async def start_discovery(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def stop_discovery(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def remove_device(
        self,
        device_path: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='a{sv}',
    )
    async def set_discovery_filter(
        self,
        properties: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='as',
    )
    async def get_discovery_filters(
        self,
    ) -> List[str]:
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
    def alias(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        property_name='Class'
    )
    def device_class(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def powered(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def discoverable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def pairable(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def pairable_timeout(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def discoverable_timeout(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def discovering(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        property_name='UUIDs',
    )
    def uuids(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def modalias(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as'
    )
    def roles(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as'
    )
    def experimental_features(self) -> List[str]:
        raise NotImplementedError
