from config_item import ConfigItem
from common_conf import CommonConfig

class Cells(CommonConfig):
    def __init__(self, name="CellsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.network_interface = ConfigItem(
            key="network_interface",
            value="enp1s0f0",
            comment="Network interface name for the cell",
            used=False,
        )
        self.ru_mac_address = ConfigItem(
            key="ru_mac_address",
            value="70:b3:d5:e1:5b:06",
            comment="MAC address of the RU",
            used=False,
        )
        self.du_mac_address = ConfigItem(
            key="du_mac_address",
            value="00:11:22:33:00:77",
            comment="MAC address of the DU",
            used=False,
        )
        self.vlan_tag_cp = ConfigItem(
            key="vlan_tag_cp",
            value=1,
            comment="VLAN tag for control plane",
            used=False,
        )
        self.vlan_tag_up = ConfigItem(
            key="vlan_tag_up",
            value=1,
            comment="VLAN tag for user plane",
            used=False,
        )

        # Changed from class attributes to normal variables
        self.ru_prach_port_id = ConfigItem(
            key="ru_prach_port_id",
            value=4,
            comment="Optional UINT (4). Sets the RU PRACH eAxC port ID. Supported: [0 - 65535].",
            used=False,
        )
        self.ru_dl_port_id = ConfigItem(
            key="ru_dl_port_id",
            value=[0],
            comment="Optional UINT (0, 1). Sets the RU downlink eAxC port ID. Format: vector containing all DL eXaC ports, e.g. [0, ..., N].",
            used=False,
        )
        self.ru_ul_port_id = ConfigItem(
            key="ru_ul_port_id",
            value=0,
            comment="Optional UINT (0). Sets the RU uplink eAxC port ID. Supported: [0 - 65535].",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def network_interface(self):
        return self.network_interface.value

    @network_interface.setter
    def network_interface(self, value):
        self.network_interface.set_value(value)

    @property
    def ru_mac_address(self):
        return self.ru_mac_address.value

    @ru_mac_address.setter
    def ru_mac_address(self, value):
        self.ru_mac_address.set_value(value)

    @property
    def du_mac_address(self):
        return self.du_mac_address.value

    @du_mac_address.setter
    def du_mac_address(self, value):
        self.du_mac_address.set_value(value)

    @property
    def vlan_tag_cp(self):
        return self.vlan_tag_cp.value

    @vlan_tag_cp.setter
    def vlan_tag_cp(self, value):
        self.vlan_tag_cp.set_value(value)

    @property
    def vlan_tag_up(self):
        return self.vlan_tag_up.value

    @vlan_tag_up.setter
    def vlan_tag_up(self, value):
        self.vlan_tag_up.set_value(value)

    # Getters and setters for new normal variables
    @property
    def ru_prach_port_id(self):
        return self.ru_prach_port_id.value

    @ru_prach_port_id.setter
    def ru_prach_port_id(self, value):
        self.ru_prach_port_id.set_value(value)

    @property
    def ru_dl_port_id(self):
        return self.ru_dl_port_id.value

    @ru_dl_port_id.setter
    def ru_dl_port_id(self, value):
        self.ru_dl_port_id.set_value(value)

    @property
    def ru_ul_port_id(self):
        return self.ru_ul_port_id.value

    @ru_ul_port_id.setter
    def ru_ul_port_id(self, value):
        self.ru_ul_port_id.set_value(value)
