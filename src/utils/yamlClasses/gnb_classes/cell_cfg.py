from .cell_cfg_classes.slicing import Slicing
from .cell_cfg_classes.mac_cell_group import Mac_cell_group
from .cell_cfg_classes.ssb import Ssb
from .cell_cfg_classes.sib import Sib
from .cell_cfg_classes.ul_common import Ul_common
from .cell_cfg_classes.pdcch import Pdcch
from .cell_cfg_classes.pdsch import Pdsch
from .cell_cfg_classes.pusch import Pusch
from .cell_cfg_classes.pucch import Pucch
from .cell_cfg_classes.srs import Srs
from .cell_cfg_classes.prach import Prach
from .cell_cfg_classes.tdd_ul_dl_cfg import Tdd_ul_dl_cfg
from .cell_cfg_classes.paging import Paging
from .cell_cfg_classes.csi import Csi
from .cell_cfg_classes.sched_expert_cfg import Sched_expert_cfg
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

# TODO update with comments all classes and subclasses
# TODO add variable list item for initalizer function in parent class

class Cell_cfg(CommonConfig):
    def __init__(self, name="cell_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._pci = ConfigItem(
            key="pci",
            value=1,
            comment="Physical Cell ID (PCI)",
            used=False,
        )
        self._sector_id = ConfigItem(
            key="sector_id",
            value=0,
            comment="Sector ID of the cell",
            used=False,
        )
        self._dl_arfcn = ConfigItem(
            key="dl_arfcn",
            value=536020,
            comment="Downlink ARFCN of the cell",
            used=False,
        )
        self._band = ConfigItem(
            key="band",
            value="auto",
            comment="Operating band of the cell",
            used=False,
        )
        self._common_scs = ConfigItem(
            key="common_scs",
            value=15,
            comment="Subcarrier spacing for common channels",
            used=False,
        )
        self._channel_bandwidth_MHz = ConfigItem(
            key="channel_bandwidth_MHz",
            value=20,
            comment="Channel bandwidth in MHz",
            used=False,
        )
        self._nof_antennas_dl = ConfigItem(
            key="nof_antennas_dl",
            value=1,
            comment="Number of downlink antennas",
            used=False,
        )
        self._nof_antennas_ul = ConfigItem(
            key="nof_antennas_ul",
            value=1,
            comment="Number of uplink antennas",
            used=False,
        )
        self._plmn = ConfigItem(
            key="plmn",
            value=65,
            comment="Public Land Mobile Network (PLMN) ID",
            used=False,
        )
        self._tac = ConfigItem(
            key="tac",
            value=7,
            comment="Tracking Area Code (TAC)",
            used=False,
        )
        self._q_rx_lev_min = ConfigItem(
            key="q_rx_lev_min",
            value=-70,
            comment="Minimum received signal level",
            used=False,
        )
        self._q_qual_min = ConfigItem(
            key="q_qual_min",
            value=-20,
            comment="Minimum received signal quality",
            used=False,
        )
        self._pcg_p_nr_fr1 = ConfigItem(
            key="pcg_p_nr_fr1",
            value=10,
            comment="PCG for NR FR1 configuration",
            used=False,
        )

        # Sub-configurations
        self._slicing = Slicing()
        self._mac_cell_group = Mac_cell_group()
        self._ssb = Ssb()
        self._sib = Sib()
        self._ul_common = Ul_common()
        self._pdcch = Pdcch()
        self._pdsch = Pdsch()
        self._pusch = Pusch()
        self._pucch = Pucch()
        self._srs = Srs()
        self._prach = Prach()
        self._tdd_ul_dl_cfg = Tdd_ul_dl_cfg()
        self._paging = Paging()
        self._csi = Csi()
        self._sched_expert_cfg = Sched_expert_cfg()

    # Getters and setters for ConfigItems
    @property
    def pci(self):
        return self._pci.value

    @pci.setter
    def pci(self, value):
        self._pci.set_value(value)

    @property
    def sector_id(self):
        return self._sector_id.value

    @sector_id.setter
    def sector_id(self, value):
        self._sector_id.set_value(value)

    @property
    def dl_arfcn(self):
        return self._dl_arfcn.value

    @dl_arfcn.setter
    def dl_arfcn(self, value):
        self._dl_arfcn.set_value(value)

    @property
    def band(self):
        return self._band.value

    @band.setter
    def band(self, value):
        self._band.set_value(value)

    @property
    def common_scs(self):
        return self._common_scs.value

    @common_scs.setter
    def common_scs(self, value):
        self._common_scs.set_value(value)

    @property
    def channel_bandwidth_MHz(self):
        return self._channel_bandwidth_MHz.value

    @channel_bandwidth_MHz.setter
    def channel_bandwidth_MHz(self, value):
        self._channel_bandwidth_MHz.set_value(value)

    @property
    def nof_antennas_dl(self):
        return self._nof_antennas_dl.value

    @nof_antennas_dl.setter
    def nof_antennas_dl(self, value):
        self._nof_antennas_dl.set_value(value)

    @property
    def nof_antennas_ul(self):
        return self._nof_antennas_ul.value

    @nof_antennas_ul.setter
    def nof_antennas_ul(self, value):
        self._nof_antennas_ul.set_value(value)

    @property
    def plmn(self):
        return self._plmn.value

    @plmn.setter
    def plmn(self, value):
        self._plmn.set_value(value)

    @property
    def tac(self):
        return self._tac.value

    @tac.setter
    def tac(self, value):
        self._tac.set_value(value)

    @property
    def q_rx_lev_min(self):
        return self._q_rx_lev_min.value

    @q_rx_lev_min.setter
    def q_rx_lev_min(self, value):
        self._q_rx_lev_min.set_value(value)

    @property
    def q_qual_min(self):
        return self._q_qual_min.value

    @q_qual_min.setter
    def q_qual_min(self, value):
        self._q_qual_min.set_value(value)

    @property
    def pcg_p_nr_fr1(self):
        return self._pcg_p_nr_fr1.value

    @pcg_p_nr_fr1.setter
    def pcg_p_nr_fr1(self, value):
        self._pcg_p_nr_fr1.set_value(value)
