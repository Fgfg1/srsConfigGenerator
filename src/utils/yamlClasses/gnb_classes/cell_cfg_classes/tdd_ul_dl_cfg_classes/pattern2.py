from common_conf import CommonConfig
from config_item import ConfigItem

class Pattern2(CommonConfig):
    def __init__(self, name="Pattern2Config", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items for Pattern2
        self.dl_ul_tx_period = ConfigItem(
            key="dl_ul_tx_period",
            value=10,
            comment="Sets the DL-UL transmission period in slots. Supported: [2, 5, 10, 20, 40, 80, 160].",
            used=False
        )
        self.nof_dl_slots = ConfigItem(
            key="nof_dl_slots",
            value=6,
            comment="Sets the number of DL slots in the transmission period.",
            used=False
        )
        self.nof_dl_symbols = ConfigItem(
            key="nof_dl_symbols",
            value=8,
            comment="Sets the number of DL symbols in the flex slot.",
            used=False
        )
        self.nof_ul_slots = ConfigItem(
            key="nof_ul_slots",
            value=3,
            comment="Sets the number of UL slots in the transmission period.",
            used=False
        )
        self.nof_ul_symbols = ConfigItem(
            key="nof_ul_symbols",
            value=0,
            comment="Sets the number of UL symbols in the flex slot.",
            used=False
        )

    # Getters and setters for each ConfigItem
    @property
    def dl_ul_tx_period(self):
        """Get or set the DL-UL transmission period."""
        return self.dl_ul_tx_period.value

    @dl_ul_tx_period.setter
    def dl_ul_tx_period(self, value):
        self.dl_ul_tx_period.value = value

    @property
    def nof_dl_slots(self):
        """Get or set the number of DL slots."""
        return self.nof_dl_slots.value

    @nof_dl_slots.setter
    def nof_dl_slots(self, value):
        self.nof_dl_slots.value = value

    @property
    def nof_dl_symbols(self):
        """Get or set the number of DL symbols in the flex slot."""
        return self.nof_dl_symbols.value

    @nof_dl_symbols.setter
    def nof_dl_symbols(self, value):
        self.nof_dl_symbols.value = value

    @property
    def nof_ul_slots(self):
        """Get or set the number of UL slots."""
        return self.nof_ul_slots.value

    @nof_ul_slots.setter
    def nof_ul_slots(self, value):
        self.nof_ul_slots.value = value

    @property
    def nof_ul_symbols(self):
        """Get or set the number of UL symbols in the flex slot."""
        return self.nof_ul_symbols.value

    @nof_ul_symbols.setter
    def nof_ul_symbols(self, value):
        self.nof_ul_symbols.value = value
