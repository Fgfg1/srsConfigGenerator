from config_item import ConfigItem
from common_conf import CommonConfig

class Log(CommonConfig):
    def __init__(self, name="LogConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.filename = ConfigItem(
            key="filename",
            value=None,
            comment="Log filename. If None, logs are output to console",
            used=False,
        )
        self.all_level = ConfigItem(
            key="all_level",
            value="warning",
            comment="Log level for all components",
            used=False,
        )
        self.lib_level = ConfigItem(
            key="lib_level",
            value="warning",
            comment="Log level for libraries",
            used=False,
        )
        self.e2ap_level = ConfigItem(
            key="e2ap_level",
            value="warning",
            comment="Log level for E2AP",
            used=False,
        )
        self.config_level = ConfigItem(
            key="config_level",
            value="none",
            comment="Log level for configuration changes",
            used=False,
        )
        self.tracing_filename = ConfigItem(
            key="tracing_filename",
            value=None,
            comment="Tracing log filename",
            used=False,
        )
        self.rrc_level = ConfigItem(
            key="rrc_level",
            value="warning",
            comment="Log level for RRC",
            used=False,
        )
        self.ngap_level = ConfigItem(
            key="ngap_level",
            value="warning",
            comment="Log level for NGAP",
            used=False,
        )
        self.sec_level = ConfigItem(
            key="sec_level",
            value="warning",
            comment="Log level for security components",
            used=False,
        )
        self.pdcp_level = ConfigItem(
            key="pdcp_level",
            value="warning",
            comment="Log level for PDCP",
            used=False,
        )
        self.sdap_level = ConfigItem(
            key="sdap_level",
            value="warning",
            comment="Log level for SDAP",
            used=False,
        )
        self.cu_level = ConfigItem(
            key="cu_level",
            value="warning",
            comment="Log level for CU",
            used=False,
        )
        self.mac_level = ConfigItem(
            key="mac_level",
            value="warning",
            comment="Log level for MAC",
            used=False,
        )
        self.rlc_level = ConfigItem(
            key="rlc_level",
            value="warning",
            comment="Log level for RLC",
            used=False,
        )
        self.f1ap_level = ConfigItem(
            key="f1ap_level",
            value="warning",
            comment="Log level for F1AP",
            used=False,
        )
        self.f1u_level = ConfigItem(
            key="f1u_level",
            value="warning",
            comment="Log level for F1U",
            used=False,
        )
        self.gtpu_level = ConfigItem(
            key="gtpu_level",
            value="warning",
            comment="Log level for GTPU",
            used=False,
        )
        self.du_level = ConfigItem(
            key="du_level",
            value="warning",
            comment="Log level for DU",
            used=False,
        )
        self.metrics_level = ConfigItem(
            key="metrics_level",
            value="none",
            comment="Log level for metrics",
            used=False,
        )
        self.f1ap_json_enabled = ConfigItem(
            key="f1ap_json_enabled",
            value=False,
            comment="Enable JSON logging for F1AP",
            used=False,
        )
        self.hal_level = ConfigItem(
            key="hal_level",
            value="warning",
            comment="Log level for HAL",
            used=False,
        )
        self.broadcast_enabled = ConfigItem(
            key="broadcast_enabled",
            value=False,
            comment="Enable broadcast logs",
            used=False,
        )
        self.phy_rx_symbols_filename = ConfigItem(
            key="phy_rx_symbols_filename",
            value=None,
            comment="Filename for PHY RX symbols logs",
            used=False,
        )
        self.phy_rx_symbols_port = ConfigItem(
            key="phy_rx_symbols_port",
            value=0,
            comment="Port for PHY RX symbols logs",
            used=False,
        )
        self.phy_rx_symbols_prach = ConfigItem(
            key="phy_rx_symbols_prach",
            value=False,
            comment="Enable PRACH symbols logging for PHY RX",
            used=False,
        )
        self.hex_max_size = ConfigItem(
            key="hex_max_size",
            value=0,
            comment="Maximum size for hex logs",
            used=False,
        )
        self.fapi_level = ConfigItem(
            key="fapi_level",
            value="warning",
            comment="Log level for FAPI",
            used=False,
        )
        self.ofh_level = ConfigItem(
            key="ofh_level",
            value="warning",
            comment="Log level for OFH",
            used=False,
        )
        self.radio_level = ConfigItem(
            key="radio_level",
            value="info",
            comment="Log level for radio components",
            used=False,
        )
        self.phy_level = ConfigItem(
            key="phy_level",
            value="warning",
            comment="Log level for PHY",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def filename(self):
        return self.filename.value

    @filename.setter
    def filename(self, value):
        self.filename.set_value(value)

    @property
    def all_level(self):
        return self.all_level.value

    @all_level.setter
    def all_level(self, value):
        self.all_level.set_value(value)

    @property
    def lib_level(self):
        return self.lib_level.value

    @lib_level.setter
    def lib_level(self, value):
        self.lib_level.set_value(value)

    @property
    def e2ap_level(self):
        return self.e2ap_level.value

    @e2ap_level.setter
    def e2ap_level(self, value):
        self.e2ap_level.set_value(value)

    @property
    def config_level(self):
        return self.config_level.value

    @config_level.setter
    def config_level(self, value):
        self.config_level.set_value(value)

    @property
    def tracing_filename(self):
        return self.tracing_filename.value

    @tracing_filename.setter
    def tracing_filename(self, value):
        self.tracing_filename.set_value(value)

    @property
    def rrc_level(self):
        return self.rrc_level.value

    @rrc_level.setter
    def rrc_level(self, value):
        self.rrc_level.set_value(value)

    @property
    def ngap_level(self):
        return self.ngap_level.value

    @ngap_level.setter
    def ngap_level(self, value):
        self.ngap_level.set_value(value)

    @property
    def sec_level(self):
        return self.sec_level.value

    @sec_level.setter
    def sec_level(self, value):
        self.sec_level.set_value(value)

    @property
    def pdcp_level(self):
        return self.pdcp_level.value

    @pdcp_level.setter
    def pdcp_level(self, value):
        self.pdcp_level.set_value(value)

    @property
    def sdap_level(self):
        return self.sdap_level.value

    @sdap_level.setter
    def sdap_level(self, value):
        self.sdap_level.set_value(value)

    @property
    def cu_level(self):
        return self.cu_level.value

    @cu_level.setter
    def cu_level(self, value):
        self.cu_level.set_value(value)

    @property
    def mac_level(self):
        return self.mac_level.value

    @mac_level.setter
    def mac_level(self, value):
        self.mac_level.set_value(value)

    @property
    def rlc_level(self):
        return self.rlc_level.value

    @rlc_level.setter
    def rlc_level(self, value):
        self.rlc_level.set_value(value)

    @property
    def f1ap_level(self):
        return self.f1ap_level.value

    @f1ap_level.setter
    def f1ap_level(self, value):
        self.f1ap_level.set_value(value)

    @property
    def f1u_level(self):
        return self.f1u_level.value

    @f1u_level.setter
    def f1u_level(self, value):
        self.f1u_level.set_value(value)

    @property
    def gtpu_level(self):
        return self.gtpu_level.value

    @gtpu_level.setter
    def gtpu_level(self, value):
        self.gtpu_level.set_value(value)

    @property
    def du_level(self):
        return self.du_level.value

    @du_level.setter
    def du_level(self, value):
        self.du_level.set_value(value)

    @property
    def metrics_level(self):
        return self.metrics_level.value

    @metrics_level.setter
    def metrics_level(self, value):
        self.metrics_level.set_value(value)

    @property
    def f1ap_json_enabled(self):
        return self.f1ap_json_enabled.value

    @f1ap_json_enabled.setter
    def f1ap_json_enabled(self, value):
        self.f1ap_json_enabled.set_value(value)

    @property
    def hal_level(self):
        return self.hal_level.value

    @hal_level.setter
    def hal_level(self, value):
        self.hal_level.set_value(value)

    @property
    def broadcast_enabled(self):
        return self.broadcast_enabled.value

    @broadcast_enabled.setter
    def broadcast_enabled(self, value):
        self.broadcast_enabled.set_value(value)

    @property
    def phy_rx_symbols_filename(self):
        return self.phy_rx_symbols_filename.value

    @phy_rx_symbols_filename.setter
    def phy_rx_symbols_filename(self, value):
        self.phy_rx_symbols_filename.set_value(value)

    @property
    def phy_rx_symbols_port(self):
        return self.phy_rx_symbols_port.value

    @phy_rx_symbols_port.setter
    def phy_rx_symbols_port(self, value):
        self.phy_rx_symbols_port.set_value(value)

    @property
    def phy_rx_symbols_prach(self):
        return self.phy_rx_symbols_prach.value

    @phy_rx_symbols_prach.setter
    def phy_rx_symbols_prach(self, value):
        self.phy_rx_symbols_prach.set_value(value)

    @property
    def hex_max_size(self):
        return self.hex_max_size.value

    @hex_max_size.setter
    def hex_max_size(self, value):
        self.hex_max_size.set_value(value)

    @property
    def fapi_level(self):
        return self.fapi_level.value

    @fapi_level.setter
    def fapi_level(self, value):
        self.fapi_level.set_value(value)

    @property
    def ofh_level(self):
        return self.ofh_level.value

    @ofh_level.setter
    def ofh_level(self, value):
        self.ofh_level.set_value(value)

    @property
    def radio_level(self):
        return self.radio_level.value

    @radio_level.setter
    def radio_level(self, value):
        self.radio_level.set_value(value)

    @property
    def phy_level(self):
        return self.phy_level.value

    @phy_level.setter
    def phy_level(self, value):
        self.phy_level.set_value(value)
