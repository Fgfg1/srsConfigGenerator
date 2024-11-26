from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig
from .sched_expert_cfg_classes.policy_sched_cfg import Policy_sched_cfg
from .sched_expert_cfg_classes.ta_sched_cfg import Ta_sched_cfg

class Sched_expert_cfg(CommonConfig):
    def __init__(self, name="SchedExpertCfgConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Sub-configurations
        self._policy_sched_cfg = Policy_sched_cfg()
        self._ta_sched_cfg = Ta_sched_cfg()

    # Add getters and setters for sub-configurations if needed
    @property
    def policy_sched_cfg(self):
        return self._policy_sched_cfg

    @policy_sched_cfg.setter
    def policy_sched_cfg(self, value):
        self._policy_sched_cfg = value

    @property
    def ta_sched_cfg(self):
        return self._ta_sched_cfg

    @ta_sched_cfg.setter
    def ta_sched_cfg(self, value):
        self._ta_sched_cfg = value
