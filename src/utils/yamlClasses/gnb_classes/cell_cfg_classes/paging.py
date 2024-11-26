from common_conf import CommonConfig
from config_item import ConfigItem

class Paging(CommonConfig):
    def __init__(self, name="PagingConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        self.pg_search_space_id = ConfigItem(
            key="pg_search_space_id",
            value=1,
            comment="Sets the SearchSpace to use for Paging. Supported: [1].",
            used=False
        )
        self.default_pg_cycle_in_rf = ConfigItem(
            key="default_pg_cycle_in_rf",
            value=128,
            comment="Sets the default Paging cycle in number of Radio Frames. Supported: [32, 64, 128, 256].",
            used=False
        )
        self.nof_pf_per_paging_cycle = ConfigItem(
            key="nof_pf_per_paging_cycle",
            value="oneT",
            comment="Sets the number of paging frames per DRX cycle. Supported: [oneT, halfT, quarterT, oneEighthT, oneSixteethT].",
            used=False
        )
        self.pf_offset = ConfigItem(
            key="pf_offset",
            value=0,
            comment="Sets the paging frame offset. Supported: [0 - (nof_pf_per_paging_cycle - 1)].",
            used=False
        )
        self.nof_po_per_pf = ConfigItem(
            key="nof_po_per_pf",
            value=1,
            comment="Sets the number of paging occasions per paging frame. Supported: [1, 2, 4].",
            used=False
        )

    # Getters and setters for each ConfigItem
    @property
    def pg_search_space_id(self):
        return self.pg_search_space_id.value

    @pg_search_space_id.setter
    def pg_search_space_id(self, value):
        self.pg_search_space_id.value = value

    @property
    def default_pg_cycle_in_rf(self):
        return self.default_pg_cycle_in_rf.value

    @default_pg_cycle_in_rf.setter
    def default_pg_cycle_in_rf(self, value):
        self.default_pg_cycle_in_rf.value = value

    @property
    def nof_pf_per_paging_cycle(self):
        return self.nof_pf_per_paging_cycle.value

    @nof_pf_per_paging_cycle.setter
    def nof_pf_per_paging_cycle(self, value):
        self.nof_pf_per_paging_cycle.value = value

    @property
    def pf_offset(self):
        return self.pf_offset.value

    @pf_offset.setter
    def pf_offset(self, value):
        self.pf_offset.value = value

    @property
    def nof_po_per_pf(self):
        return self.nof_po_per_pf.value

    @nof_po_per_pf.setter
    def nof_po_per_pf(self, value):
        self.nof_po_per_pf.value = value
