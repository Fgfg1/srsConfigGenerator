from .ru_sdr_classes.amplitude_control import Amplitude_control
from .ru_sdr_classes.expert_cfg import Expert_cfg
from config_item import ConfigItem
from common_conf import CommonConfig

class Ru_sdr(CommonConfig):
    def __init__(self, name="RuSdrConfig", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem
        self.srate = ConfigItem(
            key="srate", value=61.44, comment="Sampling rate of the RF-frontend in MHz", used=False
        )
        self.device_driver = ConfigItem(
            key="device_driver", value="uhd", comment="RF device driver name. Supported: [uhd, zmq]", used=False
        )
        self.device_args = ConfigItem(
            key="device_args", value=None, comment="Argument passed to the selected RF driver", used=False
        )
        self.tx_gain = ConfigItem(
            key="tx_gain", value=50, comment="Transmit gain in dB. Supported: [0 - max value supported by radio]", used=False
        )
        self.rx_gain = ConfigItem(
            key="rx_gain", value=60, comment="Receive gain in dB. Supported: [0 - max value supported by radio]", used=False
        )
        self.freq_offset = ConfigItem(
            key="freq_offset", value=0, comment="Frequency offset in Hertz", used=False
        )
        self.clock_ppm = ConfigItem(
            key="clock_ppm", value=0, comment="Clock calibration in Parts Per Million (PPM)", used=False
        )
        self.lo_offset = ConfigItem(
            key="lo_offset", value=0, comment="Local oscillator frequency offset in MHz", used=False
        )
        self.clock = ConfigItem(
            key="clock", value="default", comment="RF device clock source. Supported: [default, internal, external, gpsdo]", used=False
        )
        self.sync = ConfigItem(
            key="sync", value="default", comment="RF device time synchronization source. Supported: [default, internal, external, gpsdo]", used=False
        )
        self.otw_format = ConfigItem(
            key="otw_format", value="default", comment="Over-the-wire format. Supported: [default, sc8, sc12, sc16]", used=False
        )
        self.time_alignment_calibration = ConfigItem(
            key="time_alignment_calibration",
            value="auto",
            comment="Compensates for reception and transmission time misalignment. Positive values reduce RF transmission delay",
            used=False,
        )

        # Sub-configurations
        self.amplitude_control = Amplitude_control()
        self.expert_cfg = Expert_cfg()

    # Expose ConfigItem attributes via properties for compatibility
    @property
    def srate(self):
        return self.srate.value

    @srate.setter
    def srate(self, value):
        self.srate.set_value(value)

    @property
    def device_driver(self):
        return self.device_driver.value

    @device_driver.setter
    def device_driver(self, value):
        self.device_driver.set_value(value)

    @property
    def device_args(self):
        return self.device_args.value

    @device_args.setter
    def device_args(self, value):
        self.device_args.set_value(value)

    @property
    def tx_gain(self):
        return self.tx_gain.value

    @tx_gain.setter
    def tx_gain(self, value):
        self.tx_gain.set_value(value)

    @property
    def rx_gain(self):
        return self.rx_gain.value

    @rx_gain.setter
    def rx_gain(self, value):
        self.rx_gain.set_value(value)

    @property
    def freq_offset(self):
        return self.freq_offset.value

    @freq_offset.setter
    def freq_offset(self, value):
        self.freq_offset.set_value(value)

    @property
    def clock_ppm(self):
        return self.clock_ppm.value

    @clock_ppm.setter
    def clock_ppm(self, value):
        self.clock_ppm.set_value(value)

    @property
    def lo_offset(self):
        return self.lo_offset.value

    @lo_offset.setter
    def lo_offset(self, value):
        self.lo_offset.set_value(value)

    @property
    def clock(self):
        return self.clock.value

    @clock.setter
    def clock(self, value):
        self.clock.set_value(value)

    @property
    def sync(self):
        return self.sync.value

    @sync.setter
    def sync(self, value):
        self.sync.set_value(value)

    @property
    def otw_format(self):
        return self.otw_format.value

    @otw_format.setter
    def otw_format(self, value):
        self.otw_format.set_value(value)

    @property
    def time_alignment_calibration(self):
        return self.time_alignment_calibration.value

    @time_alignment_calibration.setter
    def time_alignment_calibration(self, value):
        self.time_alignment_calibration.set_value(value)
