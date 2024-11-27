from .threads_classes.non_rt import Non_rt
from .threads_classes.upper_phy import Upper_phy
from .threads_classes.lower_phy import Lower_phy
from .threads_classes.ofh import Ofh
from src.utils.yamlClasses.common_conf import CommonConfig

class Threads(CommonConfig):
    def __init__(self, name="ThreadsConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configurations
        self._non_rt = Non_rt()
        self._upper_phy = Upper_phy()
        self._lower_phy = Lower_phy()
        self._ofh = Ofh()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._non_rt,
            self._upper_phy,
            self._lower_phy,
            self._ofh
        ]

    #TODO add getters and setters for the thread classes
