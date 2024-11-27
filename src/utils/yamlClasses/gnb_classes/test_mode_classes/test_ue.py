from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Test_ue(CommonConfig):
    def __init__(self, name="test_ue", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Optional ENUM (0). Sets the C-RNTI of the UE. Supported: [0 - 65519].
        self._rnti = ConfigItem(
            key="rnti",
            value=0,
            comment="RNTI for the test UE",
            used=False,
        )

        # Optonal UINT (1). Sets the number of test UE(s) created. Supported [0 - 1024].
        self._nof_ues = ConfigItem(
            key="nof_ues",
            value=1,
            comment="Number of UEs in the test",
            used=False,
        )

        # Optional TEXT. Sets the delay before the UL and DL HARQs are automatically ACKed. This feature should only be used if the UL PHY is not operational.
        self._auto_ack_indication_delay = ConfigItem(
            key="auto_ack_indication_delay",
            value=None,
            comment="Delay for automatic acknowledgment indication",
            used=False,
        )

        # Optional BOOLEAN (true). Enables the PDSCH of the UE. Supported: [false, true].
        self._pdsch_active = ConfigItem(
            key="pdsch_active",
            value=True,
            comment="Indicates whether PDSCH is active",
            used=False,
        )

        # Optional BOOLEAN (true). Enables the PUSCH of the UE. Supported: [false, true].
        self._pusch_active = ConfigItem(
            key="pusch_active",
            value=True,
            comment="Indicates whether PUSCH is active",
            used=False,
        )

        # Optional UINT (15). Sets the Channel Quality Information to be forwarded to the test UE. Supported: [1 - 15].
        self._cqi = ConfigItem(
            key="cqi",
            value=15,
            comment="Channel Quality Indicator (CQI) value",
            used=False,
        )

        # Optional UINT (0). Sets the Precoder Matrix Indicator to be forwarded to test UE. Supported: [0 - 3].
        self._pmi = ConfigItem(
            key="pmi",
            value=0,
            comment="Precoding Matrix Indicator (PMI) value",
            used=False,
        )

        # Optional UINT (1). Sets the Rank Indicator to be forwarded to the test UE. Supported: [1 - 4].
        self._ri = ConfigItem(
            key="ri",
            value=1,
            comment="Rank Indicator (RI) value",
            used=False,
        )

        # Optional INT (0). Sets the Precoder Matrix codebook index "i_1_1" to be forwarded to test UE, in the case of more than 2 antennas. Supported: [0 - 7].
        self._i_1_1 = ConfigItem(
            key="i_1_1",
            value=0,
            comment="I_1_1 parameter value",
            used=False,
        )

        # Optional INT (0). Sets the Precoder Matrix codebook index "i_1_3" to be forwarded to test UE, in the case of more than 2 antennas. Supported: [0 - 1].
        self._i_1_3 = ConfigItem(
            key="i_1_3",
            value=0,
            comment="I_1_3 parameter value",
            used=False,
        )

        # Optional INT (0). Sets the Precoder Matrix codebook index "i_2" to be forwarded to test UE, in the case of more than 2 antennas. Supported: [0 - 3].
        self._i_2 = ConfigItem(
            key="i_2",
            value=0,
            comment="I_2 parameter value",
            used=False,
        )

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._rnti,
            self._nof_ues,
            self._auto_ack_indication_delay,
            self._pdsch_active,
            self._pusch_active,
            self._cqi,
            self._pmi,
            self._ri,
            self._i_1_1,
            self._i_1_3,
            self._i_2
        ]

    # Getters and setters for ConfigItems
    @property
    def rnti(self):
        return self._rnti.value

    @rnti.setter
    def rnti(self, value):
        self._rnti.set_value(value)

    @property
    def nof_ues(self):
        return self._nof_ues.value

    @nof_ues.setter
    def nof_ues(self, value):
        self._nof_ues.set_value(value)

    @property
    def auto_ack_indication_delay(self):
        return self._auto_ack_indication_delay.value

    @auto_ack_indication_delay.setter
    def auto_ack_indication_delay(self, value):
        self._auto_ack_indication_delay.set_value(value)

    @property
    def pdsch_active(self):
        return self._pdsch_active.value

    @pdsch_active.setter
    def pdsch_active(self, value):
        self._pdsch_active.set_value(value)

    @property
    def pusch_active(self):
        return self._pusch_active.value

    @pusch_active.setter
    def pusch_active(self, value):
        self._pusch_active.set_value(value)

    @property
    def cqi(self):
        return self._cqi.value

    @cqi.setter
    def cqi(self, value):
        self._cqi.set_value(value)

    @property
    def pmi(self):
        return self._pmi.value

    @pmi.setter
    def pmi(self, value):
        self._pmi.set_value(value)

    @property
    def ri(self):
        return self._ri.value

    @ri.setter
    def ri(self, value):
        self._ri.set_value(value)

    @property
    def i_1_1(self):
        return self._i_1_1.value

    @i_1_1.setter
    def i_1_1(self, value):
        self._i_1_1.set_value(value)

    @property
    def i_1_3(self):
        return self._i_1_3.value

    @i_1_3.setter
    def i_1_3(self, value):
        self._i_1_3.set_value(value)

    @property
    def i_2(self):
        return self._i_2.value

    @i_2.setter
    def i_2(self, value):
        self._i_2.set_value(value)
