from .ru_sdr_classes.amplitude_control import Amplitude_control
from .ru_sdr_classes.expert_cfg import Expert_cfg
from src.utils.yamlClasses.config_item import ConfigItem
from src.utils.yamlClasses.common_conf import CommonConfig

class Ru_sdr(CommonConfig):
    def __init__(self, name="ru_sdr", data=None, used=False):
        super().__init__(name, data or {}, used)

        # Configurable attributes using ConfigItem

        # Required FLOAT (61.44). Sets the sampling rate of the RF-frontend in MHz.
        self._srate = ConfigItem(
            key="srate", value=61.44, comment="Sampling rate of the RF-frontend in MHz", used=True
        )

        # Required TEXT (uhd). RF device driver name. Supported: [uhd, zmq].
        self._device_driver = ConfigItem(
            key="device_driver", value="uhd", comment="RF device driver name. Supported: [uhd, zmq]", used=True
        )
        
        # Optional TEXT. An argument that gets passed to the selected RF driver.
        self._device_args = ConfigItem(
            key="device_args", value=None, comment="Argument passed to the selected RF driver", used=False
        )

        # Required FLOAT (50). Sets the transmit gain in dB. Supported: [0 - max value supported by radio].
        self._tx_gain = ConfigItem(
            key="tx_gain", value=50, comment="Transmit gain in dB. Supported: [0 - max value supported by radio]", used=True
        )

        # Required FLOAT (60). Sets the receive gain in dB. Supported: [0 - max value supported by radio].
        self._rx_gain = ConfigItem(
            key="rx_gain", value=60, comment="Receive gain in dB. Supported: [0 - max value supported by radio]", used=True
        )

        # Optional FLOAT (0). Sets the frequency offset in Hertz.
        self._freq_offset = ConfigItem(
            key="freq_offset", value=0, comment="Frequency offset in Hertz", used=False
        )

         # Optional FLOAT (0). Sets the clock calibration in Parts Per Million (PPM).
        self._clock_ppm = ConfigItem(
            key="clock_ppm", value=0, comment="Clock calibration in Parts Per Million (PPM)", used=False
        )

        # Optional FLOAT (0). Shifts the local oscillator frequency in MHz away from the center frequency to move LO leakage out of the channel.
        self._lo_offset = ConfigItem(
            key="lo_offset", value=0, comment="Local oscillator frequency offset in MHz", used=False
        )

        # Optional TEXT (default). Specify the RF device clock source (i.e., 10MHz reference oscillator). Supported: [default, internal, external, gpsdo].
        self._clock = ConfigItem(
            key="clock", value="default", comment="RF device clock source. Supported: [default, internal, external, gpsdo]", used=False
        )
        
        # Optional TEXT (default). Specify the RF device time synchronization source (i.e., 1PPS reference). Supported: [default, internal, external, gpsdo].
        self._sync = ConfigItem(
            key="sync", value="default", comment="RF device time synchronization source. Supported: [default, internal, external, gpsdo]", used=False
        )

        # Optional TEXT (default). Specify the over-the-wire format. Supported: [default, sc8, sc12, sc16].
        self._otw_format = ConfigItem(
            key="otw_format", value="default", comment="Over-the-wire format. Supported: [default, sc8, sc12, sc16]", used=False
        )

        # Optional TEXT (auto). Compensates for any reception and transmission time misalignment inherent to the RF device.
        # Positive values reduce the RF transmission delay with respect to the RF reception. Negative values have the opposite effect.  
        self._time_alignment_calibration = ConfigItem(
            key="time_alignment_calibration",
            value="auto",
            comment="Compensates for reception and transmission time misalignment. Positive values reduce RF transmission delay",
            used=False,
        )

        # Sub-modules
        self._amplitude_control = Amplitude_control()
        self._expert_cfg = Expert_cfg()

        # List of all variables in the order that it shows up in the config file
        self._variables = [
            self._srate,
            self._device_driver,
            self._device_args,
            self._tx_gain,
            self._rx_gain,
            self._freq_offset,
            self._clock_ppm,
            self._lo_offset,
            self._clock,
            self._sync,
            self._otw_format,
            self._time_alignment_calibration,
            self._amplitude_control,
            self._time_alignment_calibration
        ]


    # Expose ConfigItem attributes via properties for compatibility
    @property
    def srate(self):
        return self._srate.value

    @srate.setter
    def srate(self, value):
        self._srate.set_value(value)

    @property
    def device_driver(self):
        return self._device_driver.value

    @device_driver.setter
    def device_driver(self, value):
        self._device_driver.set_value(value)

    @property
    def device_args(self):
        return self._device_args.value

    @device_args.setter
    def device_args(self, value):
        self._device_args.set_value(value)

    @property
    def tx_gain(self):
        return self._tx_gain.value

    @tx_gain.setter
    def tx_gain(self, value):
        self._tx_gain.set_value(value)

    @property
    def rx_gain(self):
        return self._rx_gain.value

    @rx_gain.setter
    def rx_gain(self, value):
        self._rx_gain.set_value(value)

    @property
    def freq_offset(self):
        return self._freq_offset.value

    @freq_offset.setter
    def freq_offset(self, value):
        self._freq_offset.set_value(value)

    @property
    def clock_ppm(self):
        return self._clock_ppm.value

    @clock_ppm.setter
    def clock_ppm(self, value):
        self._clock_ppm.set_value(value)

    @property
    def lo_offset(self):
        return self._lo_offset.value

    @lo_offset.setter
    def lo_offset(self, value):
        self._lo_offset.set_value(value)

    @property
    def clock(self):
        return self._clock.value

    @clock.setter
    def clock(self, value):
        self._clock.set_value(value)

    @property
    def sync(self):
        return self._sync.value

    @sync.setter
    def sync(self, value):
        self._sync.set_value(value)

    @property
    def otw_format(self):
        return self._otw_format.value

    @otw_format.setter
    def otw_format(self, value):
        self._otw_format.set_value(value)

    @property
    def time_alignment_calibration(self):
        return self._time_alignment_calibration.value

    @time_alignment_calibration.setter
    def time_alignment_calibration(self, value):
        self._time_alignment_calibration.set_value(value)
