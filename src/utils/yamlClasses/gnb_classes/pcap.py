from config_item import ConfigItem
from common_conf import CommonConfig

class Pcap(CommonConfig):
    def __init__(self, name="PcapConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.ngap_filename = ConfigItem(
            key="ngap_filename",
            value="/tmp/gnb_ngap.pcap",
            comment="File path for NGAP pcap logs",
            used=False,
        )
        self.ngap_enable = ConfigItem(
            key="ngap_enable",
            value=False,
            comment="Enable NGAP pcap logging",
            used=False,
        )
        self.n3_filename = ConfigItem(
            key="n3_filename",
            value="/tmp/gnb_n3.pcap",
            comment="File path for N3 pcap logs",
            used=False,
        )
        self.n3_enable = ConfigItem(
            key="n3_enable",
            value=False,
            comment="Enable N3 pcap logging",
            used=False,
        )
        self.e1ap_filename = ConfigItem(
            key="e1ap_filename",
            value="/tmp/gnb_e1ap.pcap",
            comment="File path for E1AP pcap logs",
            used=False,
        )
        self.e1ap_enable = ConfigItem(
            key="e1ap_enable",
            value=False,
            comment="Enable E1AP pcap logging",
            used=False,
        )
        self.e2ap_filename = ConfigItem(
            key="e2ap_filename",
            value="/tmp/gnb_e2ap.pcap",
            comment="File path for E2AP pcap logs",
            used=False,
        )
        self.e2ap_enable = ConfigItem(
            key="e2ap_enable",
            value=False,
            comment="Enable E2AP pcap logging",
            used=False,
        )
        self.f1ap_filename = ConfigItem(
            key="f1ap_filename",
            value="/tmp/gnb_f1ap.pcap",
            comment="File path for F1AP pcap logs",
            used=False,
        )
        self.f1ap_enable = ConfigItem(
            key="f1ap_enable",
            value=False,
            comment="Enable F1AP pcap logging",
            used=False,
        )
        self.f1u_filename = ConfigItem(
            key="f1u_filename",
            value="/tmp/gnb_f1u.pcap",
            comment="File path for F1U pcap logs",
            used=False,
        )
        self.f1u_enable = ConfigItem(
            key="f1u_enable",
            value=False,
            comment="Enable F1U pcap logging",
            used=False,
        )
        self.rlc_filename = ConfigItem(
            key="rlc_filename",
            value="/tmp/gnb_rlc.pcap",
            comment="File path for RLC pcap logs",
            used=False,
        )
        self.rlc_rb_type = ConfigItem(
            key="rlc_rb_type",
            value="all",
            comment="RLC RB type for pcap logging. Supported: [all, specific]",
            used=False,
        )
        self.rlc_enable = ConfigItem(
            key="rlc_enable",
            value=False,
            comment="Enable RLC pcap logging",
            used=False,
        )
        self.mac_filename = ConfigItem(
            key="mac_filename",
            value="/tmp/gnb_mac.pcap",
            comment="File path for MAC pcap logs",
            used=False,
        )
        self.mac_type = ConfigItem(
            key="mac_type",
            value="udp",
            comment="MAC type for pcap logging. Supported: [udp, tcp]",
            used=False,
        )
        self.mac_enable = ConfigItem(
            key="mac_enable",
            value=False,
            comment="Enable MAC pcap logging",
            used=False,
        )

    # Getters and setters for all ConfigItems
    @property
    def ngap_filename(self):
        return self.ngap_filename.value

    @ngap_filename.setter
    def ngap_filename(self, value):
        self.ngap_filename.set_value(value)

    @property
    def ngap_enable(self):
        return self.ngap_enable.value

    @ngap_enable.setter
    def ngap_enable(self, value):
        self.ngap_enable.set_value(value)

    @property
    def n3_filename(self):
        return self.n3_filename.value

    @n3_filename.setter
    def n3_filename(self, value):
        self.n3_filename.set_value(value)

    @property
    def n3_enable(self):
        return self.n3_enable.value

    @n3_enable.setter
    def n3_enable(self, value):
        self.n3_enable.set_value(value)

    @property
    def e1ap_filename(self):
        return self.e1ap_filename.value

    @e1ap_filename.setter
    def e1ap_filename(self, value):
        self.e1ap_filename.set_value(value)

    @property
    def e1ap_enable(self):
        return self.e1ap_enable.value

    @e1ap_enable.setter
    def e1ap_enable(self, value):
        self.e1ap_enable.set_value(value)

    @property
    def e2ap_filename(self):
        return self.e2ap_filename.value

    @e2ap_filename.setter
    def e2ap_filename(self, value):
        self.e2ap_filename.set_value(value)

    @property
    def e2ap_enable(self):
        return self.e2ap_enable.value

    @e2ap_enable.setter
    def e2ap_enable(self, value):
        self.e2ap_enable.set_value(value)

    @property
    def f1ap_filename(self):
        return self.f1ap_filename.value

    @f1ap_filename.setter
    def f1ap_filename(self, value):
        self.f1ap_filename.set_value(value)

    @property
    def f1ap_enable(self):
        return self.f1ap_enable.value

    @f1ap_enable.setter
    def f1ap_enable(self, value):
        self.f1ap_enable.set_value(value)

    @property
    def f1u_filename(self):
        return self.f1u_filename.value

    @f1u_filename.setter
    def f1u_filename(self, value):
        self.f1u_filename.set_value(value)

    @property
    def f1u_enable(self):
        return self.f1u_enable.value

    @f1u_enable.setter
    def f1u_enable(self, value):
        self.f1u_enable.set_value(value)

    @property
    def rlc_filename(self):
        return self.rlc_filename.value

    @rlc_filename.setter
    def rlc_filename(self, value):
        self.rlc_filename.set_value(value)

    @property
    def rlc_rb_type(self):
        return self.rlc_rb_type.value

    @rlc_rb_type.setter
    def rlc_rb_type(self, value):
        self.rlc_rb_type.set_value(value)

    @property
    def rlc_enable(self):
        return self.rlc_enable.value

    @rlc_enable.setter
    def rlc_enable(self, value):
        self.rlc_enable.set_value(value)

    @property
    def mac_filename(self):
        return self.mac_filename.value

    @mac_filename.setter
    def mac_filename(self, value):
        self.mac_filename.set_value(value)

    @property
    def mac_type(self):
        return self.mac_type.value

    @mac_type.setter
    def mac_type(self, value):
        self.mac_type.set_value(value)

    @property
    def mac_enable(self):
        return self.mac_enable.value

    @mac_enable.setter
    def mac_enable(self, value):
        self.mac_enable.set_value(value)
