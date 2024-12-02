from src.utils.yamlClasses.common_conf import CommonConfig
from src.utils.yamlClasses.config_item import ConfigItem

class Pf_sched(CommonConfig):
    def __init__(self, name="pf_sched", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configuration item for PF scheduling fairness coefficient

        # Optional FLOAT [2]. Sets the fairness Coefficient to use in Proportional Fair policy scheduler.
        self._pf_sched_fairness_coeff = ConfigItem(
            key="pf_sched_fairness_coeff",
            value=2,
            comment="Sets the fairness coefficient for PF scheduling. Supported: positive integers.",
            used=False
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._pf_sched_fairness_coeff
        ]


    # Getter and setter for ConfigItem
    @property
    def pf_sched_fairness_coeff(self):
        """Get or set the fairness coefficient for PF scheduling."""
        return self._pf_sched_fairness_coeff.value

    @pf_sched_fairness_coeff.setter
    def pf_sched_fairness_coeff(self, value):
        self._pf_sched_fairness_coeff.value = value
