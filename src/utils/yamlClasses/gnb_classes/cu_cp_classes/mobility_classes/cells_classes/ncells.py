from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ncells(CommonConfig):
    def __init__(self, name="NcellsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._nr_cell_id = ConfigItem(
            key="nr_cell_id",
            value=None,
            comment="NR Cell ID for neighboring cells",
            used=False,
        )
        self._report_configs = ConfigItem(
            key="report_configs",
            value=None,
            comment="Report configuration for neighboring cells",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def nr_cell_id(self):
        return self._nr_cell_id.value

    @nr_cell_id.setter
    def nr_cell_id(self, value):
        self._nr_cell_id.set_value(value)

    @property
    def report_configs(self):
        return self._report_configs.value

    @report_configs.setter
    def report_configs(self, value):
        self._report_configs.set_value(value)
