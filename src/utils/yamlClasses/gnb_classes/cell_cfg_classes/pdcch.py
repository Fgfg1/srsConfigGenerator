from common_conf import CommonConfig
from .pdcch_classes.common import Common
from .pdcch_classes.dedicated import Dedicated

class Pdcch(CommonConfig):
    def __init__(self, name="PdcchConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configurations
        self._common = Common()
        self._dedicated = Dedicated()

    # Getters and setters for 'common' sub-configuration
    @property
    def common(self):
        """Access the common PDCCH configuration."""
        return self._common

    @common.setter
    def common(self, value):
        """Set the common PDCCH configuration."""
        if isinstance(value, Common):
            self._common = value
        else:
            raise ValueError("common must be an instance of Common.")

    # Getters and setters for 'dedicated' sub-configuration
    @property
    def dedicated(self):
        """Access the dedicated PDCCH configuration."""
        return self._dedicated

    @dedicated.setter
    def dedicated(self, value):
        """Set the dedicated PDCCH configuration."""
        if isinstance(value, Dedicated):
            self._dedicated = value
        else:
            raise ValueError("dedicated must be an instance of Dedicated.")

    # Utility methods for managing sub-configurations
    def update_common_config(self, key, value):
        """Update a specific parameter in the common configuration."""
        if hasattr(self._common, key):
            setattr(self._common, key, value)
        else:
            raise KeyError(f"The common configuration has no attribute '{key}'.")

    def update_dedicated_config(self, key, value):
        """Update a specific parameter in the dedicated configuration."""
        if hasattr(self._dedicated, key):
            setattr(self._dedicated, key, value)
        else:
            raise KeyError(f"The dedicated configuration has no attribute '{key}'.")

    def reset_common_config(self):
        """Reset the common configuration to a new instance."""
        self._common = Common()

    def reset_dedicated_config(self):
        """Reset the dedicated configuration to a new instance."""
        self._dedicated = Dedicated()
