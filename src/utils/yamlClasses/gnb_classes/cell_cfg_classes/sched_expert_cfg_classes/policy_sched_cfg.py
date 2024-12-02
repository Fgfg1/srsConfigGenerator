from src.utils.yamlClasses.common_conf import CommonConfig
from .policy_sched_cfg_classes.pf_sched import Pf_sched

class Policy_sched_cfg(CommonConfig):
    def __init__(self, name="policy_sched_cfg", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configuration for PF scheduling
        self.__pf_sched = Pf_sched()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self.__pf_sched
        ]

    # Getter and setter for the Pf_sched configuration
    @property
    def pf_sched(self):
        """Access the Proportional Fair (PF) scheduling configuration."""
        return self.__pf_sched

    @pf_sched.setter
    def pf_sched(self, value):
        """Set the Proportional Fair (PF) scheduling configuration."""
        if isinstance(value, Pf_sched):
            self.__pf_sched = value
        else:
            raise ValueError("pf_sched must be an instance of Pf_sched.")

    # Utility methods for managing Pf_sched
    def reset_pf_sched(self):
        """Reset the PF scheduling configuration to its default state."""
        self.__pf_sched = Pf_sched()

    def update_pf_sched(self, key, value):
        """Update a specific attribute in the PF scheduling configuration."""
        if hasattr( self._pf_sched, key):
            setattr( self._pf_sched, key, value)
        else:
            raise KeyError(f"The Pf_sched configuration has no attribute '{key}'.")
