import smbus2
import crcmod

class MLX90615:
    """Melexis MLX90615 IR temperature sensor API."""

    # Register addresses (0x1x = EEPROM, 0x2x = RAM)
    MLX90615_CONFIG = 0x12
    MLX90615_EMISSIVITY = 0x13
    MLX90615_ID1 = 0x1E
    MLX90615_ID2 = 0x1F
    MLX90615_RAWIR = 0x25
    MLX90615_TA = 0x26
    MLX90615_TO = 0x27

    def __init__(self, i2c_bus, i2c_address=0x5B):
        """Opens the i2c device."""
        self.bus = smbus2.SMBus(i2c_bus)
        self.address = i2c_address

    def get_register(self, register):
        return self.bus.read_word_data(self.address, register)

    def set_register(self, register, value):
        crc8 = crcmod.predefined.mkPredefinedCrcFun('crc-8')
        value_msb = (value & 0xFF00) >> 8
        value_lsb = value & 0xFF
        crcval = crc8(
            bytearray([(self.address << 1), register, value_lsb, value_msb]))
        print("TODO: Fix register setting, which requires SMBus PEC support.")
        return self.bus.write_i2c_block_data(self.address, register, [value_lsb, value_msb, crcval])

    def get_ambient_temperature(self):
        """Reads ambient temperature in deg C."""
        data = self.get_register(self.MLX90615_TA)
        return self._calculate_temperature(data)

    def get_object_temperature(self):
        """Reads object temperature in deg C."""
        data = self.get_register(self.MLX90615_TO)
        return self._calculate_temperature(data)

    def close(self):
        self.bus.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()

    @staticmethod
    def _calculate_temperature(raw):
        """Converts temperature register value to degrees C."""
        return round((raw * 0.02) - 273.15, 3)

    @property
    def emissivity(self):
        "Emissivity (ε)."
        data = self.get_register(self.MLX90615_EMISSIVITY)
        return data / 16384.0

    @emissivity.setter
    def emissivity(self, value):
        assert 0.1 < value < 1
        data = round(16384 * value)
        return self.set_register(self.MLX90615_EMISSIVITY, data)