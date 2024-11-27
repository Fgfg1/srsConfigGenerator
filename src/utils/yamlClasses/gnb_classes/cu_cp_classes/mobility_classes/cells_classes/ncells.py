from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ncells(CommonConfig):
    def __init__(self, name="NcellsConfig", data=None, used=True):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required UINT. The ID of this neighbor cell.
        self._nr_cell_id = ConfigItem(
            key="nr_cell_id",
            value=None,
            comment="NR Cell ID for neighboring cells",
            used=True,
        )

        # Required TEXT. List of report configurations to use for measurements of this neighbor cell.
        self._report_configs = ConfigItem(
            key="report_configs",
            value=None,
            comment="Report configuration for neighboring cells",
            used=True,
        )
        # the above config might become a class later as it takes a list of report_configs(aka the other class in mobility)

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._nr_cell_id,
            self._report_configs
        ]

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
