
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



class OrgBluezAdapter1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Adapter1',
):

    @dbus_method_async(
    )
    async def start_discovery(
        self,
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
    )
    async def stop_discovery(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def remove_device(
        self,
        device: str,
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
        property_signature='u',
    )
    def discoverable_timeout(self) -> int:
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
        property_signature='b',
    )
    def discovering(self) -> bool:
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



class OrgBluezMedia1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.Media1',
):

    @dbus_method_async(
        input_signature='oa{sv}',
    )
    async def register_endpoint(
        self,
        endpoint: str,
        properties: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_endpoint(
        self,
        endpoint: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='oa{sv}',
    )
    async def register_player(
        self,
        player: str,
        properties: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_player(
        self,
        player: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='oa{sv}',
    )
    async def register_application(
        self,
        application: str,
        options: Dict[str, Tuple[str, Any]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='o',
    )
    async def unregister_application(
        self,
        application: str,
    ) -> None:
        raise NotImplementedError



class OrgBluezNetworkServer1Interface(
    DbusInterfaceCommonAsync,
    interface_name='org.bluez.NetworkServer1',
):

    @dbus_method_async(
        input_signature='ss',
    )
    async def register(
        self,
        uuid: str,
        bridge: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def unregister(
        self,
        uuid: str,
    ) -> None:
        raise NotImplementedError

