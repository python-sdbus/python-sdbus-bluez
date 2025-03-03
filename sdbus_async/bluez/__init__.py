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

from .adapter_api import AdapterInterfaceAsync
from .agent_api import AgentInterfaceAsync, AgentManagerInterfaceAsync
from .battery_api import BatteryInterfaceAsync
from .device_api import DeviceInterfaceAsync
from .gatt_api import (
    GattCharacteristicInterfaceAsync,
    GattDescriptorInterfaceAsync,
    GattServiceInterfaceAsync,
)
from .media_api import MediaInterfaceAsync
from .network_api import NetworkServerInterfaceAsync
from .profile_api import ProfileInterfaceAsync, ProfileManagerInterfaceAsync

__all__ = (
    'AdapterInterfaceAsync',

    'AgentInterfaceAsync',
    'AgentManagerInterfaceAsync',

    'BatteryInterfaceAsync',

    'DeviceInterfaceAsync',

    'GattServiceInterfaceAsync',
    'GattCharacteristicInterfaceAsync',
    'GattDescriptorInterfaceAsync',

    'MediaInterfaceAsync',

    'NetworkServerInterfaceAsync',

    'ProfileInterfaceAsync',
    'ProfileManagerInterfaceAsync',
)
