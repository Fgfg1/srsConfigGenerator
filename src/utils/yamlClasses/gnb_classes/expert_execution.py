from .expert_execution_classes.cell_affinities import Cell_affinities
from .expert_execution_classes.affinities import Affinities
from .expert_execution_classes.threads import Threads
from src.utils.yamlClasses.common_conf import CommonConfig

class Expert_execution(CommonConfig):
    def __init__(self, name="expert_execution", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configuration attributes
        self._cell_affinities = Cell_affinities()
        self._affinities = Affinities()
        self._threads = Threads()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._cell_affinities,
            self._affinities,
            self._threads
        ]
