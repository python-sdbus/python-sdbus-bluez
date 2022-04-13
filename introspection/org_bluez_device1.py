
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



class OrgBluezDevice1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Device1',
):

    @dbus_method_async(
    )
    async def disconnect(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
    )
    async def connect(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def connect_profile(
        self,
        u_u_i_d: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def disconnect_profile(
        self,
        u_u_i_d: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
    )
    async def pair(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
    )
    async def cancel_pairing(
        self,
    ) -> None:
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
        property_signature='q',
    )
    def appearance(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def icon(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def paired(self) -> bool:
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
    def legacy_pairing(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='n',
    )
    def r_s_s_i(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def connected(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def u_u_i_ds(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def modalias(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='o',
    )
    def adapter(self) -> str:
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
        property_signature='n',
    )
    def tx_power(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def services_resolved(self) -> bool:
        raise NotImplementedError



class OrgBluezBattery1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Battery1',
):

    @dbus_property_async(
        property_signature='y',
    )
    def percentage(self) -> int:
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

