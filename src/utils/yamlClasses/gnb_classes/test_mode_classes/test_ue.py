from config_item import ConfigItem
from common_conf import CommonConfig

class Test_ue(CommonConfig):
    def __init__(self, name="TestUeConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.rnti = ConfigItem(
            key="rnti",
            value=0,
            comment="RNTI for the test UE",
            used=False,
        )
        self.nof_ues = ConfigItem(
            key="nof_ues",
            value=1,
            comment="Number of UEs in the test",
            used=False,
        )
        self.auto_ack_indication_delay = ConfigItem(
            key="auto_ack_indication_delay",
            value=None,
            comment="Delay for automatic acknowledgment indication",
            used=False,
        )
        self.pdsch_active = ConfigItem(
            key="pdsch_active",
            value=True,
            comment="Indicates whether PDSCH is active",
            used=False,
        )
        self.pusch_active = ConfigItem(
            key="pusch_active",
            value=True,
            comment="Indicates whether PUSCH is active",
            used=False,
        )
        self.cqi = ConfigItem(
            key="cqi",
            value=15,
            comment="Channel Quality Indicator (CQI) value",
            used=False,
        )
        self.pmi = ConfigItem(
            key="pmi",
            value=0,
            comment="Precoding Matrix Indicator (PMI) value",
            used=False,
        )
        self.ri = ConfigItem(
            key="ri",
            value=1,
            comment="Rank Indicator (RI) value",
            used=False,
        )
        self.i_1_1 = ConfigItem(
            key="i_1_1",
            value=0,
            comment="I_1_1 parameter value",
            used=False,
        )
        self.i_1_3 = ConfigItem(
            key="i_1_3",
            value=0,
            comment="I_1_3 parameter value",
            used=False,
        )
        self.i_2 = ConfigItem(
            key="i_2",
            value=0,
            comment="I_2 parameter value",
            used=False,
        )

    # Getters and setters for ConfigItems
    @property
    def rnti(self):
        return self.rnti.value

    @rnti.setter
    def rnti(self, value):
        self.rnti.set_value(value)

    @property
    def nof_ues(self):
        return self.nof_ues.value

    @nof_ues.setter
    def nof_ues(self, value):
        self.nof_ues.set_value(value)

    @property
    def auto_ack_indication_delay(self):
        return self.auto_ack_indication_delay.value

    @auto_ack_indication_delay.setter
    def auto_ack_indication_delay(self, value):
        self.auto_ack_indication_delay.set_value(value)

    @property
    def pdsch_active(self):
        return self.pdsch_active.value

    @pdsch_active.setter
    def pdsch_active(self, value):
        self.pdsch_active.set_value(value)

    @property
    def pusch_active(self):
        return self.pusch_active.value

    @pusch_active.setter
    def pusch_active(self, value):
        self.pusch_active.set_value(value)

    @property
    def cqi(self):
        return self.cqi.value

    @cqi.setter
    def cqi(self, value):
        self.cqi.set_value(value)

    @property
    def pmi(self):
        return self.pmi.value

    @pmi.setter
    def pmi(self, value):
        self.pmi.set_value(value)

    @property
    def ri(self):
        return self.ri.value

    @ri.setter
    def ri(self, value):
        self.ri.set_value(value)

    @property
    def i_1_1(self):
        return self.i_1_1.value

    @i_1_1.setter
    def i_1_1(self, value):
        self.i_1_1.set_value(value)

    @property
    def i_1_3(self):
        return self.i_1_3.value

    @i_1_3.setter
    def i_1_3(self, value):
        self.i_1_3.set_value(value)

    @property
    def i_2(self):
        return self.i_2.value

    @i_2.setter
    def i_2(self, value):
        self.i_2.set_value(value)
