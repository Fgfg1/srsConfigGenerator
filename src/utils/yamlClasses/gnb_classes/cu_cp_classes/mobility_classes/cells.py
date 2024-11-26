from config_item import ConfigItem
from common_conf import CommonConfig
from .cells_classes.ncells import Ncells

class Cells(CommonConfig):
    def __init__(self, name="CellsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.nr_cell_id = ConfigItem(
            key="nr_cell_id",
            value=None,
            comment="NR Cell ID",
            used=False,
        )
        self.periodic_report_cfg_id = ConfigItem(
            key="periodic_report_cfg_id",
            value=None,
            comment="Periodic report configuration ID",
            used=False,
        )
        self.gnb_id = ConfigItem(
            key="gnb_id",
            value=None,
            comment="gNB ID for the cell",
            used=False,
        )
        self.ssb_arfcn = ConfigItem(
            key="ssb_arfcn",
            value=None,
            comment="SSB ARFCN (Absolute Radio Frequency Channel Number)",
            used=False,
        )
        self.band = ConfigItem(
            key="band",
            value=None,
            comment="Frequency band for the cell",
            used=False,
        )
        self.ssb_scs = ConfigItem(
            key="ssb_scs",
            value=None,
            comment="Subcarrier spacing for SSB",
            used=False,
        )
        self.ssb_period = ConfigItem(
            key="ssb_period",
            value=None,
            comment="Periodicity of SSB transmission",
            used=False,
        )
        self.ssb_offset = ConfigItem(
            key="ssb_offset",
            value=None,
            comment="Offset for SSB transmission",
            used=False,
        )
        self.ssb_duration = ConfigItem(
            key="ssb_duration",
            value=None,
            comment="Duration of the SSB transmission",
            used=False,
        )

        # Sub-configuration
        self.ncells = Ncells()

    # Getters and setters for ConfigItems
    @property
    def nr_cell_id(self):
        return self.nr_cell_id.value

    @nr_cell_id.setter
    def nr_cell_id(self, value):
        self.nr_cell_id.set_value(value)

    @property
    def periodic_report_cfg_id(self):
        return self.periodic_report_cfg_id.value

    @periodic_report_cfg_id.setter
    def periodic_report_cfg_id(self, value):
        self.periodic_report_cfg_id.set_value(value)

    @property
    def gnb_id(self):
        return self.gnb_id.value

    @gnb_id.setter
    def gnb_id(self, value):
        self.gnb_id.set_value(value)

    @property
    def ssb_arfcn(self):
        return self.ssb_arfcn.value

    @ssb_arfcn.setter
    def ssb_arfcn(self, value):
        self.ssb_arfcn.set_value(value)

    @property
    def band(self):
        return self.band.value

    @band.setter
    def band(self, value):
        self.band.set_value(value)

    @property
    def ssb_scs(self):
        return self.ssb_scs.value

    @ssb_scs.setter
    def ssb_scs(self, value):
        self.ssb_scs.set_value(value)

    @property
    def ssb_period(self):
        return self.ssb_period.value

    @ssb_period.setter
    def ssb_period(self, value):
        self.ssb_period.set_value(value)

    @property
    def ssb_offset(self):
        return self.ssb_offset.value

    @ssb_offset.setter
    def ssb_offset(self, value):
        self.ssb_offset.set_value(value)

    @property
    def ssb_duration(self):
        return self.ssb_duration.value

    @ssb_duration.setter
    def ssb_duration(self, value):
        self.ssb_duration.set_value(value)
