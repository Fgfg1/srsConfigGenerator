from src.utils.yamlClasses.common_conf import CommonConfig
from .mac_cell_group_classes.bsr_cfg import Bsr_cfg
from .mac_cell_group_classes.phr_cfg import Phr_cfg
from .mac_cell_group_classes.sr_cfg import Sr_cfg

class Mac_cell_group(CommonConfig):
    def __init__(self, name="MacCellGroupConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configurations
        self.__bsr_cfg = Bsr_cfg()
        self.__phr_cfg = Phr_cfg()
        self.__sr_cfg = Sr_cfg()

    # Getters and setters for each sub-configuration
    @property
    def bsr_cfg(self):
        """Access the BSR configuration."""
        return self.__bsr_cfg

    @bsr_cfg.setter
    def bsr_cfg(self, value):
        """Set the BSR configuration."""
        if isinstance(value, Bsr_cfg):
            self.__bsr_cfg = value
        else:
            raise ValueError("bsr_cfg must be an instance of Bsr_cfg.")

    @property
    def phr_cfg(self):
        """Access the PHR configuration."""
        return self.__phr_cfg

    @phr_cfg.setter
    def phr_cfg(self, value):
        """Set the PHR configuration."""
        if isinstance(value, Phr_cfg):
            self.__phr_cfg = value
        else:
            raise ValueError("phr_cfg must be an instance of Phr_cfg.")

    @property
    def sr_cfg(self):
        """Access the SR configuration."""
        return self.__sr_cfg

    @sr_cfg.setter
    def sr_cfg(self, value):
        """Set the SR configuration."""
        if isinstance(value, Sr_cfg):
            self.__sr_cfg = value
        else:
            raise ValueError("sr_cfg must be an instance of Sr_cfg.")

    # Utility methods for managing sub-configurations
    def reset_bsr_cfg(self):
        """Reset the BSR configuration to a new instance."""
        self.__bsr_cfg = Bsr_cfg()

    def reset_phr_cfg(self):
        """Reset the PHR configuration to a new instance."""
        self.__phr_cfg = Phr_cfg()

    def reset_sr_cfg(self):
        """Reset the SR configuration to a new instance."""
        self.__sr_cfg = Sr_cfg()

    def update_bsr_cfg(self, key, value):
        """Update a specific parameter in the BSR configuration."""
        if hasattr( self._bsr_cfg, key):
            setattr( self._bsr_cfg, key, value)
        else:
            raise KeyError(f"The BSR configuration has no attribute '{key}'.")

    def update_phr_cfg(self, key, value):
        """Update a specific parameter in the PHR configuration."""
        if hasattr( self._phr_cfg, key):
            setattr( self._phr_cfg, key, value)
        else:
            raise KeyError(f"The PHR configuration has no attribute '{key}'.")

    def update_sr_cfg(self, key, value):
        """Update a specific parameter in the SR configuration."""
        if hasattr( self._sr_cfg, key):
            setattr( self._sr_cfg, key, value)
        else:
            raise KeyError(f"The SR configuration has no attribute '{key}'.")
