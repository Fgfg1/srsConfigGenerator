from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Csi(CommonConfig):
    def __init__(self, name="csi", data=None, used=False):
        super().__init__(name, data or {}, used)

        # CSI Configuration

        # Optional BOOLEAN (true). Enables CSI-RS resources and CSI reporting. Supported: [false, true].
        self._csi_rs_enabled = ConfigItem(
            key="csi_rs_enabled",
            value=True,
            comment="Enables or disables CSI-RS reporting.",
            used=False
        )

        # Optional UINT (20). Sets the CSI-RS period in milliseconds. Supported: [10, 20, 40, 80].
        self._csi_rs_period = ConfigItem(
            key="csi_rs_period",
            value=20,
            comment="Sets the period of CSI-RS in slots. Supported: [10, 20, 40, 80, 160].",
            used=False
        )

        # Optional TEXT Sets the slot offset of first CSI-RS resource used for measurement.
        self._meas_csi_rs_slot_offset = ConfigItem(
            key="meas_csi_rs_slot_offset",
            value=None,
            comment="Slot offset for Measurement CSI-RS reporting.",
            used=False
        )

        # Optional TEXT. Sets the slot offset of the first CSI-RS slot used for tracking.
        self._tracking_csi_rs_slot_offset = ConfigItem(
            key="tracking_csi_rs_slot_offset",
            value=None,
            comment="Slot offset for Tracking CSI-RS reporting.",
            used=False
        )

        # Optional TEXT. Sets the slot offset of the ZP CSI-RS resources.
        self._zp_csi_rs_slot_offset = ConfigItem(
            key="zp_csi_rs_slot_offset",
            value=None,
            comment="Slot offset for Zero Power CSI-RS.",
            used=False
        )

        # Optional INT (0). Sets the power offset of PDSCH RE to NZP CSI-RS RE in dB. Supported: [-8 - 15].
        self._pwr_ctrl_offset = ConfigItem(
            key="pwr_ctrl_offset",
            value=0,
            comment="Sets the power control offset for CSI-RS.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._csi_rs_enabled,
            self._csi_rs_period,
            self._meas_csi_rs_slot_offset,
            self._tracking_csi_rs_slot_offset,
            self._zp_csi_rs_slot_offset,
            self._pwr_ctrl_offset
        ]

    # Getters and setters for each ConfigItem
    @property
    def csi_rs_enabled(self):
        return self._csi_rs_enabled.value

    @csi_rs_enabled.setter
    def csi_rs_enabled(self, value):
        self._csi_rs_enabled.value = value

    @property
    def csi_rs_period(self):
        return self._csi_rs_period.value

    @csi_rs_period.setter
    def csi_rs_period(self, value):
        self._csi_rs_period.value = value

    @property
    def meas_csi_rs_slot_offset(self):
        return self._meas_csi_rs_slot_offset.value

    @meas_csi_rs_slot_offset.setter
    def meas_csi_rs_slot_offset(self, value):
        self._meas_csi_rs_slot_offset.value = value

    @property
    def tracking_csi_rs_slot_offset(self):
        return self._tracking_csi_rs_slot_offset.value

    @tracking_csi_rs_slot_offset.setter
    def tracking_csi_rs_slot_offset(self, value):
        self._tracking_csi_rs_slot_offset.value = value

    @property
    def zp_csi_rs_slot_offset(self):
        return self._zp_csi_rs_slot_offset.value

    @zp_csi_rs_slot_offset.setter
    def zp_csi_rs_slot_offset(self, value):
        self._zp_csi_rs_slot_offset.value = value

    @property
    def pwr_ctrl_offset(self):
        return self._pwr_ctrl_offset.value

    @pwr_ctrl_offset.setter
    def pwr_ctrl_offset(self, value):
        self._pwr_ctrl_offset.value = value
