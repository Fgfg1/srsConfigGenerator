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

class Cell_cfg(CommonConfig):
    def __init__(self, name="cell_cfg", data=None, used=True):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required UINT (1). Sets the Physical Cell ID. Supported: [0-1007].
        self._pci = ConfigItem(
            key="pci",
            value=1,
            comment="Physical Cell ID (PCI)",
            used=True,
        )

        # Optional UINT (0). Sets the Sector ID (4-14 bits). This value is concatenated with the gNB Id to form the NR Cell Identity (NCI). 
        # If not specified, a unique value for the DU is automatically derived. Supported: [0 - 16383].
        self._sector_id = ConfigItem(
            key="sector_id",
            value=0,
            comment="Sector ID of the cell",
            used=False,
        )

        # Required UINT (536020). Sets the Downlink ARFCN.
        self._dl_arfcn = ConfigItem(
            key="dl_arfcn",
            value=536020,
            comment="Downlink ARFCN of the cell",
            used=True,
        )

        # Optional TEXT (auto). Sets the NR band being used for the cell. If not specified, will be set automatically based on ARFCN. Supported: all release 17 bands.
        self._band = ConfigItem(
            key="band",
            value="auto",
            comment="Operating band of the cell",
            used=True,
        )

        # Required UINT (15). Sets the subcarrier spacing in KHz to be used by the cell. Supported: [15, 30].
        self._common_scs = ConfigItem(
            key="common_scs",
            value=15,
            comment="Subcarrier spacing for common channels",
            used=True,
        )

        # Required UINT (20). Sets the channel Bandwidth in MHz, the number of PRBs will be derived from this. Supported: [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100].
        self._channel_bandwidth_MHz = ConfigItem(
            key="channel_bandwidth_MHz",
            value=20,
            comment="Channel bandwidth in MHz",
            used=True,
        )

        # Optional UINT (1). Sets the number of antennas for downlink transmission. Supported: [1, 2, 4].
        self._nof_antennas_dl = ConfigItem(
            key="nof_antennas_dl",
            value=1,
            comment="Number of downlink antennas",
            used=False,
        )

        # Optional UINT (1). Sets the number of antennas for uplink transmission. Supported: [1, 2, 4].
        self._nof_antennas_ul = ConfigItem(
            key="nof_antennas_ul",
            value=1,
            comment="Number of uplink antennas",
            used=False,
        )

        # Required TEXT (00101). Sets the Public Land Mobile Network code. Format: 7-digit PLMN code containing MCC & MNC.
        self._plmn = ConfigItem(
            key="plmn",
            value=65,
            comment="Public Land Mobile Network (PLMN) ID",
            used=True,
        )

        # Required UINT (7). Sets the Tracking Area Code.
        self._tac = ConfigItem(
            key="tac",
            value=7,
            comment="Tracking Area Code (TAC)",
            used=True,
        )

        # Optional INT (-70). Sets the required minimum received RSRP level for cell selection/re-selection, in dBm. Supported: [-70 - -22].
        self._q_rx_lev_min = ConfigItem(
            key="q_rx_lev_min",
            value=-70,
            comment="Minimum received signal level",
            used=False,
        )

        # Optional INT (-20). Sets the required minimum received RSRQ level for cell selection/re-selection, in dB. Supported: [-43 - -12].
        self._q_qual_min = ConfigItem(
            key="q_qual_min",
            value=-20,
            comment="Minimum received signal quality",
            used=False,
        )

        # Optional INT (10). Sets the maximum total TX power to be used by the UE in this NR cell group across in FR1. Supported: [-30 - +23].
        self._pcg_p_nr_fr1 = ConfigItem(
            key="pcg_p_nr_fr1",
            value=10,
            comment="PCG for NR FR1 configuration",
            used=False,
        )

        # Sub-modules
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

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._pci,
            self._sector_id,
            self._dl_arfcn,
            self._band,
            self._common_scs,
            self._channel_bandwidth_MHz,
            self._nof_antennas_dl,
            self._nof_antennas_ul,
            self._plmn,
            self._tac,
            self._q_rx_lev_min,
            self._q_qual_min,
            self._pcg_p_nr_fr1,
            self._slicing,
            self._mac_cell_group,
            self._ssb,
            self._sib,
            self._ul_common,
            self._pdcch,
            self._pdsch,
            self._pusch,
            self._pucch,
            self._srs,
            self._prach,
            self._tdd_ul_dl_cfg,
            self._paging,
            self._csi,
            self._sched_expert_cfg
        ]

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
