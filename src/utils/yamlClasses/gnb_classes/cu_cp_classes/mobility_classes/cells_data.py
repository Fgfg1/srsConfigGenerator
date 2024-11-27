from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .cells_classes.ncells import Ncells

 # Optional TEXT. Sets the list of cells known to the CU-CP, their configs (if not provided over F1) and their respective neighbor cells.

class CellsData(CommonConfig):
    def __init__(self, name="CellsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required UINT. The ID of this serving cell.
        self._nr_cell_id = ConfigItem(
            key="nr_cell_id",
            value=None,
            comment="NR Cell ID",
            used=True,
        )

        # Optional UINT. The periodical report configuration to use for this serving cell.
        self._periodic_report_cfg_id = ConfigItem(
            key="periodic_report_cfg_id",
            value=None,
            comment="Periodic report configuration ID",
            used=False,
        )

        # Optional UINT. The ID of this gNB.
        self._gnb_id = ConfigItem(
            key="gnb_id",
            value=None,
            comment="gNB ID for the cell",
            used=False,
        )

        # Optional UINT. The SSB ARFCN of this serving cell. Must be present if not provided over F1.
        self._ssb_arfcn = ConfigItem(
            key="ssb_arfcn",
            value=None,
            comment="SSB ARFCN (Absolute Radio Frequency Channel Number)",
            used=False,
        )

        # Optional UINT. The NR band of this serving cell cell. Must be present if not provided over F1.
        self._band = ConfigItem(
            key="band",
            value=None,
            comment="Frequency band for the cell",
            used=False,
        )

        # Optional UINT. The SSB subcarrier spacing of this serving cell in KHz. Must be present if not provided over F1.
        self._ssb_scs = ConfigItem(
            key="ssb_scs",
            value=None,
            comment="Subcarrier spacing for SSB",
            used=False,
        )

        # Optional UINT. The SSB period of this serving cell in ms.  Must be present if not provided over F1.
        self._ssb_period = ConfigItem(
            key="ssb_period",
            value=None,
            comment="Periodicity of SSB transmission",
            used=False,
        )

        # Optional UINT. The SSB offset of this serving cell. Must be present if not provided over F1.
        self._ssb_offset = ConfigItem(
            key="ssb_offset",
            value=None,
            comment="Offset for SSB transmission",
            used=False,
        )

        # Optional UINT. The SSB duration of this serving cell in subframes. Must be present if not provided over F1.
        self._ssb_duration = ConfigItem(
            key="ssb_duration",
            value=None,
            comment="Duration of the SSB transmission",
            used=False,
        )

        # Sub-configuration
        self._ncells = Ncells()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._nr_cell_id,
            self._periodic_report_cfg_id,
            self._ncells,
            self._gnb_id,
            self._ssb_arfcn,
            self._band,
            self._ssb_scs,
            self._ssb_period,
            self._ssb_offset,
            self._ssb_duration
        ]

        

    # Getters and setters for ConfigItems
    @property
    def nr_cell_id(self):
        return self._nr_cell_id.value

    @nr_cell_id.setter
    def nr_cell_id(self, value):
        self._nr_cell_id.set_value(value)

    @property
    def periodic_report_cfg_id(self):
        return self._periodic_report_cfg_id.value

    @periodic_report_cfg_id.setter
    def periodic_report_cfg_id(self, value):
        self._periodic_report_cfg_id.set_value(value)

    @property
    def gnb_id(self):
        return self._gnb_id.value

    @gnb_id.setter
    def gnb_id(self, value):
        self._gnb_id.set_value(value)

    @property
    def ssb_arfcn(self):
        return self._ssb_arfcn.value

    @ssb_arfcn.setter
    def ssb_arfcn(self, value):
        self._ssb_arfcn.set_value(value)

    @property
    def band(self):
        return self._band.value

    @band.setter
    def band(self, value):
        self._band.set_value(value)

    @property
    def ssb_scs(self):
        return self._ssb_scs.value

    @ssb_scs.setter
    def ssb_scs(self, value):
        self._ssb_scs.set_value(value)

    @property
    def ssb_period(self):
        return self._ssb_period.value

    @ssb_period.setter
    def ssb_period(self, value):
        self._ssb_period.set_value(value)

    @property
    def ssb_offset(self):
        return self._ssb_offset.value

    @ssb_offset.setter
    def ssb_offset(self, value):
        self._ssb_offset.set_value(value)

    @property
    def ssb_duration(self):
        return self._ssb_duration.value

    @ssb_duration.setter
    def ssb_duration(self, value):
        self._ssb_duration.set_value(value)
