from .expert_execution_classes.cell_affinities import Cell_affinities
from .expert_execution_classes.affinities import Affinities
from .expert_execution_classes.threads import Threads
from common_conf import CommonConfig

class Expert_execution(CommonConfig):
    def __init__(self, name="ExpertExecutionConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configuration attributes
        self.cell_affinities = Cell_affinities()
        self.affinities = Affinities()
        self.threads = Threads()
