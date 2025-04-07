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

from sdbus import DbusInterfaceCommonAsync, dbus_method_async


class AgentManagerInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.AgentManager1',
):

    @dbus_method_async(
        input_signature='os',
    )
    async def register_agent(
        self,
        agent_path: str,
        capability: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_agent(
        self,
        agent_path: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def request_default_agent(
        self,
        agent_path: str,
    ) -> None:
        raise NotImplementedError


class AgentInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Agent1',
):
    @dbus_method_async()
    async def cancel(self) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def release(self) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='os',
    )
    async def authorize_service(self, device: str, uuid: str) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def request_authorization(self, device: str) -> None:
        raise NotImplementedError
