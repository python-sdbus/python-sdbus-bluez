
from __future__ import annotations

from typing import Any, Dict, List, Tuple

from sdbus import (DbusDeprecatedFlag, DbusInterfaceCommonAsync,
                   DbusNoReplyFlag, DbusPropertyConstFlag,
                   DbusPropertyEmitsChangeFlag,
                   DbusPropertyEmitsInvalidationFlag, DbusPropertyExplicitFlag,
                   DbusUnprivilegedFlag, dbus_method_async,
                   dbus_property_async, dbus_signal_async)


class OrgFreedesktopDBusIntrospectableInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.DBus.Introspectable',
):

    @dbus_method_async(
        result_signature='s',
    )
    async def introspect(
        self,
    ) -> str:
        raise NotImplementedError



class OrgBluezAgentManager1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.AgentManager1',
):

    @dbus_method_async(
        input_signature='os',
    )
    async def register_agent(
        self,
        agent: str,
        capability: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_agent(
        self,
        agent: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def request_default_agent(
        self,
        agent: str,
    ) -> None:
        raise NotImplementedError



class OrgBluezProfileManager1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.ProfileManager1',
):

    @dbus_method_async(
        input_signature='osa{sv}',
    )
    async def register_profile(
        self,
        profile: str,
        u_u_i_d: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_profile(
        self,
        profile: str,
    ) -> None:
        raise NotImplementedError

