from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Sched_cfg(CommonConfig):
    def __init__(self, name="sched_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration items for Sched_cfg

        # Optional UINT (0). Sets the minimum percentage of PRBs to be allocated to the slice. Supported [0 - 100].
        self._min_prb_policy_ratio = ConfigItem(
            key="min_prb_policy_ratio",
            value=0,
            comment="Sets the minimum PRB policy ratio as a percentage. Supported: [0 - 100].",
            used=False
        )

        # Optional UINT (100). Sets the maximum percentage of PRBs to be allocated to the slice. Supported [1 - 100].
        self._max_prb_policy_ratio = ConfigItem(
            key="max_prb_policy_ratio",
            value=100,
            comment="Sets the maximum PRB policy ratio as a percentage. Supported: [0 - 100].",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._min_prb_policy_ratio,
            self._max_prb_policy_ratio
        ]

    # Getters and setters for ConfigItem
    @property
    def min_prb_policy_ratio(self):
        """Get or set the minimum PRB policy ratio."""
        return self._min_prb_policy_ratio.value

    @min_prb_policy_ratio.setter
    def min_prb_policy_ratio(self, value):
        self._min_prb_policy_ratio.value = value

    @property
    def max_prb_policy_ratio(self):
        """Get or set the maximum PRB policy ratio."""
        return self._max_prb_policy_ratio.value

    @max_prb_policy_ratio.setter
    def max_prb_policy_ratio(self, value):
        self._max_prb_policy_ratio.value = value
