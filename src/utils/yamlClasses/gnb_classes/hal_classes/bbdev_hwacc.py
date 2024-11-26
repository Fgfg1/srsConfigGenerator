from .bbdev_hwacc_classes.pdsch_enc import Pdsch_enc
from .bbdev_hwacc_classes.pusch_dec import Pusch_dec
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Bbdev_hwacc(CommonConfig):
    def __init__(self, name="BbdevHwaccConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self._bbdev_acc_type = ConfigItem(
            key="bbdev_acc_type",
            value="srs",
            comment="Type of BBDev accelerator",
            used=False,
        )
        self._hwacc_type = ConfigItem(
            key="hwacc_type",
            value=None,
            comment="Type of hardware accelerator",
            used=False,
        )
        self._id = ConfigItem(
            key="id",
            value=0,
            comment="ID of the hardware accelerator",
            used=False,
        )
        self._msg_mbuf_size = ConfigItem(
            key="msg_mbuf_size",
            value=None,
            comment="Message buffer size for the accelerator",
            used=False,
        )
        self._rm_mbuf_size = ConfigItem(
            key="rm_mbuf_size",
            value=None,
            comment="RM buffer size for the accelerator",
            used=False,
        )
        self._nof_mbuf = ConfigItem(
            key="nof_mbuf",
            value=None,
            comment="Number of message buffers",
            used=False,
        )

        # Sub-configurations
        self._pdsch_enc = Pdsch_enc()
        self._pusch_dec = Pusch_dec()

    # Getters and setters for ConfigItems
    @property
    def bbdev_acc_type(self):
        return self._bbdev_acc_type.value

    @bbdev_acc_type.setter
    def bbdev_acc_type(self, value):
        self._bbdev_acc_type.set_value(value)

    @property
    def hwacc_type(self):
        return self._hwacc_type.value

    @hwacc_type.setter
    def hwacc_type(self, value):
        self._hwacc_type.set_value(value)

    @property
    def id(self):
        return self._id.value

    @id.setter
    def id(self, value):
        self._id.set_value(value)

    @property
    def msg_mbuf_size(self):
        return self._msg_mbuf_size.value

    @msg_mbuf_size.setter
    def msg_mbuf_size(self, value):
        self._msg_mbuf_size.set_value(value)

    @property
    def rm_mbuf_size(self):
        return self._rm_mbuf_size.value

    @rm_mbuf_size.setter
    def rm_mbuf_size(self, value):
        self._rm_mbuf_size.set_value(value)

    @property
    def nof_mbuf(self):
        return self._nof_mbuf.value

    @nof_mbuf.setter
    def nof_mbuf(self, value):
        self._nof_mbuf.set_value(value)
