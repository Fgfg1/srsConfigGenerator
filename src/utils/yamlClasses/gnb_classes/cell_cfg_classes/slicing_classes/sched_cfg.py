from common_conf import CommonConfig
from config_item import ConfigItem

class Sched_cfg(CommonConfig):
    def __init__(self, name="SchedConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items for Sched_cfg
        self.min_prb_policy_ratio = ConfigItem(
            key="min_prb_policy_ratio",
            value=0,
            comment="Sets the minimum PRB policy ratio as a percentage. Supported: [0 - 100].",
            used=False
        )
        self.max_prb_policy_ratio = ConfigItem(
            key="max_prb_policy_ratio",
            value=100,
            comment="Sets the maximum PRB policy ratio as a percentage. Supported: [0 - 100].",
            used=False
        )

    # Getters and setters for ConfigItem
    @property
    def min_prb_policy_ratio(self):
        """Get or set the minimum PRB policy ratio."""
        return self.min_prb_policy_ratio.value

    @min_prb_policy_ratio.setter
    def min_prb_policy_ratio(self, value):
        self.min_prb_policy_ratio.value = value

    @property
    def max_prb_policy_ratio(self):
        """Get or set the maximum PRB policy ratio."""
        return self.max_prb_policy_ratio.value

    @max_prb_policy_ratio.setter
    def max_prb_policy_ratio(self, value):
        self.max_prb_policy_ratio.value = value
