from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class CellsData(CommonConfig):
    def __init__(self, name=None, data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional TEXT (enp1s0f0). Sets the ethernet network interface name for the RU or PCIe identifier when using DPDK. Format: a string, e.g. [interface_name].
        self._network_interface = ConfigItem(
            key="network_interface",
            value="enp1s0f0",
            comment="Network interface name for the cell",
            used=False,
        )

        # Optional TEXT (70:b3:d5:e1:5b:06). Sets the RU MAC address. Format: a string, e.g. [AA:BB:CC:DD:11:22:33].
        self._ru_mac_address = ConfigItem(
            key="ru_mac_address",
            value="70:b3:d5:e1:5b:06",
            comment="MAC address of the RU",
            used=False,
        )

        # Optional TEXT (00:11:22:33:00:77). Sets the DU MAC address. Format: a string, e.g. [AA:BB:CC:DD:11:22:33].
        self._du_mac_address = ConfigItem(
            key="du_mac_address",
            value="00:11:22:33:00:77",
            comment="MAC address of the DU",
            used=False,
        )

        # Optional UINT (1). Sets the VLAN tag value for C-Plane.
        self._vlan_tag_cp = ConfigItem(
            key="vlan_tag_cp",
            value=1,
            comment="VLAN tag for control plane",
            used=False,
        )

        # Optional UINT (1). Sets the VLAN tag value for U-Plane.
        self._vlan_tag_up = ConfigItem(
            key="vlan_tag_up",
            value=1,
            comment="VLAN tag for user plane",
            used=False,
        )

        # Optional UINT (4). Sets the RU PRACH eAxC port ID. Supported: [0 - 65535].
        self._ru_prach_port_id = ConfigItem(
            key="ru_prach_port_id",
            value=4,
            comment="Optional UINT (4). Sets the RU PRACH eAxC port ID. Supported: [0 - 65535].",
            used=False,
        )

        # Optional UINT (0, 1). Sets the RU downlink eAxC port ID. Format: vector containing all DL eXaC ports, e.g. [0, ...\ , N].
        self._ru_dl_port_id = ConfigItem(
            key="ru_dl_port_id",
            value=[0, 1],
            comment="Optional UINT (0, 1). Sets the RU downlink eAxC port ID. Format: vector containing all DL eXaC ports, e.g. [0, ..., N].",
            used=False,
        )

        # Optional UINT (0). Sets the RU uplink eAxC port ID. Supported: [0 - 65535].
        self._ru_ul_port_id = ConfigItem(
            key="ru_ul_port_id",
            value=0,
            comment="Optional UINT (0). Sets the RU uplink eAxC port ID. Supported: [0 - 65535].",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._network_interface,
            self._ru_mac_address,
            self._du_mac_address,
            self._vlan_tag_cp,
            self._vlan_tag_up,
            self._ru_prach_port_id,
            self._ru_dl_port_id,
            self._ru_ul_port_id
        ]

    # Getters and setters for ConfigItems
    @property
    def network_interface(self):
        return self._network_interface.value

    @network_interface.setter
    def network_interface(self, value):
        self._network_interface.set_value(value)

    @property
    def ru_mac_address(self):
        return self._ru_mac_address.value

    @ru_mac_address.setter
    def ru_mac_address(self, value):
        self._ru_mac_address.set_value(value)

    @property
    def du_mac_address(self):
        return self._du_mac_address.value

    @du_mac_address.setter
    def du_mac_address(self, value):
        self._du_mac_address.set_value(value)

    @property
    def vlan_tag_cp(self):
        return self._vlan_tag_cp.value

    @vlan_tag_cp.setter
    def vlan_tag_cp(self, value):
        self._vlan_tag_cp.set_value(value)

    @property
    def vlan_tag_up(self):
        return self._vlan_tag_up.value

    @vlan_tag_up.setter
    def vlan_tag_up(self, value):
        self._vlan_tag_up.set_value(value)

    # Getters and setters for new normal variables
    @property
    def ru_prach_port_id(self):
        return self._ru_prach_port_id.value

    @ru_prach_port_id.setter
    def ru_prach_port_id(self, value):
        self._ru_prach_port_id.set_value(value)

    @property
    def ru_dl_port_id(self):
        return self._ru_dl_port_id.value

    @ru_dl_port_id.setter
    def ru_dl_port_id(self, value):
        self._ru_dl_port_id.set_value(value)

    @property
    def ru_ul_port_id(self):
        return self._ru_ul_port_id.value

    @ru_ul_port_id.setter
    def ru_ul_port_id(self, value):
        self._ru_ul_port_id.set_value(value)
