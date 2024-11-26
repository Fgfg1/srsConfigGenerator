from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Cells(CommonConfig):
    def __init__(self, name="cells", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._pci = ConfigItem(
            key="pci",
            value=1,
            comment="Physical Cell ID (PCI) of the cell",
            used=False,
        )
        self._dl_arfcn = ConfigItem(
            key="dl_arfcn",
            value=536020,
            comment="Downlink Absolute Radio Frequency Channel Number (ARFCN)",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def pci(self):
        return self._pci.value

    @pci.setter
    def pci(self, value):
        self._pci.set_value(value)

    @property
    def dl_arfcn(self):
        return self._dl_arfcn.value

    @dl_arfcn.setter
    def dl_arfcn(self, value):
        self._dl_arfcn.set_value(value)
