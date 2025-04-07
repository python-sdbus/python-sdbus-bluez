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

from typing import Any, Dict, Tuple

from sdbus import DbusInterfaceCommon, dbus_method


class ProfileManagerInterface(
    DbusInterfaceCommon,
    interface_name='org.bluez.ProfileManager1',
):

    @dbus_method(
        input_signature='osa{sv}',
    )
    def register_profile(
        self,
        profile_path: str,
        uuid: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method(
        input_signature='o',
    )
    def unregister_profile(
        self,
        profile_path: str,
    ) -> None:
        raise NotImplementedError

class ProfileInterface(
    DbusInterfaceCommon,
    interface_name='org.bluez.Profile1',
):

    @dbus_method()
    def release(self) -> None:
        raise NotImplementedError

    @dbus_method(
        input_signature='oha{sv}',
    )
    def new_connection(
        self,
        device: str,
        fd: int,
        fd_properties: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method(
        input_signature='o',
    )
    def request_disconnection(
        self,
        device: str,
    ) -> None:
        raise NotImplementedError
