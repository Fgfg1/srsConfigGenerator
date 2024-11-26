from config_item import ConfigItem
from common_conf import CommonConfig
from .mobility_classes.cells import Cells
from .mobility_classes.report_configs import Report_configs

class Mobility(CommonConfig):
    def __init__(self, name="MobilityConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attribute using ConfigItem
        self.trigger_handover_from_measurements = ConfigItem(
            key="trigger_handover_from_measurements",
            value=False,
            comment="Enable or disable handover triggering based on measurements",
            used=False,
        )

        # Sub-configurations
        self.cells = Cells()
        self.report_configs = Report_configs()

    # Getter and setter for ConfigItem
    @property
    def trigger_handover_from_measurements(self):
        return self.trigger_handover_from_measurements.value

    @trigger_handover_from_measurements.setter
    def trigger_handover_from_measurements(self, value):
        self.trigger_handover_from_measurements.set_value(value)
