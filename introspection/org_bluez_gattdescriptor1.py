
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



class OrgBluezGattDescriptor1Interface(
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
    )
    def u_u_i_d(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
    )
    def characteristic(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def value(self) -> bytes:
        raise NotImplementedError



class OrgFreedesktopDBusPropertiesInterface(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.DBus.Properties',
):

    @dbus_method_async(
        input_signature='ss',
        result_signature='v',
    )
    async def get(
        self,
        interface: str,
        name: str,
    ) -> Tuple[str, Any]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ssv',
    )
    async def set(
        self,
        interface: str,
        name: str,
        value: Tuple[str, Any],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='a{sv}',
    )
    async def get_all(
        self,
        interface: str,
    ) -> Dict[str, Tuple[str, Any]]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='sa{sv}as',
    )
    def properties_changed(self) -> Tuple[str, Dict[str, Tuple[str, Any]], List[str]]:
        raise NotImplementedError

