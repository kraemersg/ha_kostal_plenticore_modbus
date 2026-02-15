from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass
)

class RegisterInfo():
    """Register Information"""

    def __init__(self, address, unique_id, name, unit, type, icon, device_class, display_precision, access = "RO", sensor_state_class = SensorStateClass.MEASUREMENT):
        """
        Initialize a new RegisterInfo object.

        Args:
            address (str): register address
            unique_id (str): unique id
            name (str): register name
            unit (str): data unit
            type (str): data type
            icon (str): data type
            device_class (str): data type
            display_precision (str): Display precision
            access (int, optional): Acces mode
        """
        self._address = address
        self._unique_id = unique_id
        self._name = name
        self._unit = unit
        self._type = type
        self._type = type
        self._icon = icon
        self._device_class = device_class
        self._display_precision = display_precision
        self._access = access
        self._sensor_state_class = sensor_state_class

    # Getter for address
    @property
    def address(self):
        return self._address

    # Getter for unique_id
    @property
    def unique_id(self):
        return self._unique_id

    # Getter for name
    @property
    def name(self):
        return self._name

    # Getter for unit
    @property
    def unit(self):
        return self._unit

    @property
    def type(self):
        """Getter for type"""
        return self._type

    # Getter for icon
    @property
    def icon(self):
        """Getter for icon"""
        return self._icon

    # Getter for device_class
    @property
    def device_class(self):
        """Getter for device_class"""
        return self._device_class

    # Getter for display_precision
    @property
    def display_precision(self):
        return self._display_precision

    # Getter for access
    @property
    def access(self):
        return self._access

    @property
    def sensor_state_class(self):
        """Getter for sensor_state_class"""
        return self._sensor_state_class


REGISTERS: list[RegisterInfo] = [
    # --- curated via modbus_wichtig.xlsx (types/lengths from KOSTAL_Register.py) ---
    RegisterInfo(100, "total_dc_power", "Total DC power", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(106, "consumption_battery", "Home own consumption from battery", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(108, "consumption_grid", "Home own consumption from grid", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(110, "consumption_battery_total", "Total home consumption Battery", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(112, "consumption_grid_total", "Total home consumption Grid", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(114, "consumption_pv_total", "Total home consumption PV", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(116, "consumption_pv", "Home own consumption from PV", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(118, "consumption_total", "Total home consumption", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(144, "worktime", "Worktime", "s", "Float", "mdi:timer", SensorDeviceClass.DURATION, 0, "RO", SensorStateClass.TOTAL),

    RegisterInfo(156, "active_power_phase_1", "Active power Phase 1", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(162, "active_power_phase_2", "Active power Phase 2", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(168, "active_power_phase_3", "Active power Phase 3", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(172, "total_ac_active_power", "Total AC active power", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(194, "number_battery_cycles", "Number of battery cycles", None, "Float", "mdi:counter", None, 0, "RO", SensorStateClass.TOTAL_INCREASING),

    RegisterInfo(200, "actual_battery_charge", "Actual battery charge(-)/discharge(+) current", "A", "Float", "mdi:current-dc", SensorDeviceClass.CURRENT, 2, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(210, "act_state_of_charge", "Actual state of charge", "%", "U16", "mdi:battery", SensorDeviceClass.BATTERY, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(214, "battery_temperature", "Battery Temperature", "°C", "Float", "mdi:thermometer", SensorDeviceClass.TEMPERATURE, 1, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(216, "battery_voltage", "Battery voltage", "V", "Float", "mdi:sine-wave", SensorDeviceClass.VOLTAGE, 1, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(224, "active_power_phase_1_powermeter", "Active power phase 1 (powermeter)", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(234, "active_power_phase_2_powermeter", "Active power phase 2 (powermeter)", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(244, "active_power_phase_3_powermeter", "Active power phase 3 (powermeter)", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(252, "total_active_power_powermeter", "Total active power (powermeter)", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(258, "current_dc1", "Current DC1", "A", "Float", "mdi:current-dc", SensorDeviceClass.CURRENT, 2, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(260, "power_dc1", "Power DC1", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(266, "voltage_dc1", "Voltage DC1", "V", "Float", "mdi:sine-wave", SensorDeviceClass.VOLTAGE, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(268, "current_dc2", "Current DC2", "A", "Float", "mdi:current-dc", SensorDeviceClass.CURRENT, 2, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(270, "power_dc2", "Power DC2", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(276, "voltage_dc2", "Voltage DC2", "V", "Float", "mdi:sine-wave", SensorDeviceClass.VOLTAGE, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(278, "current_dc3", "Current DC3", "A", "Float", "mdi:current-dc", SensorDeviceClass.CURRENT, 2, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(280, "power_dc3", "Power DC3", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(286, "voltage_dc3", "Voltage DC3", "V", "Float", "mdi:sine-wave", SensorDeviceClass.VOLTAGE, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(320, "total_yield", "Total yield", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL),
    RegisterInfo(322, "daily_yield", "Daily yield", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL),
    RegisterInfo(324, "yearly_yield", "Yearly yield", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL),
    RegisterInfo(326, "monthly_yield", "Monthly yield", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL),

    RegisterInfo(514, "battery_actual_soc", "Battery actual SOC", "%", "U16", "mdi:battery", SensorDeviceClass.BATTERY, 0, "RO", SensorStateClass.MEASUREMENT),

    RegisterInfo(582, "actual_battery_charge_power", "Actual battery charge/discharge power", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO",
                 SensorStateClass.MEASUREMENT),

    RegisterInfo(1042, "minimum_soc", "Minimum SOC", "%", "Float", "mdi:battery-10", SensorDeviceClass.BATTERY, 0, "RO", SensorStateClass.MEASUREMENT),
    RegisterInfo(1044, "maximum_soc", "Maximum SOC", "%", "Float", "mdi:battery-90", SensorDeviceClass.BATTERY, 0, "RO", SensorStateClass.MEASUREMENT),
	
    RegisterInfo(1046, "total_ac_charge_energy_DC_to_battery", "Total DC charge energy (DC-side to battery)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1048, "total_ac_charge_energy_DC_from_battery", "Total DC discharge energy (DC-side from battery)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1050, "total_ac_charge_energy_AC_to_battery", "Total AC charge energy (AC-side to battery)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1052, "total_ac_charge_energy_battery_to_grid", "Total AC discharge energy (battery to grid)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1054, "total_ac_charge_energy_grid_to_battery", "Total AC charge energy (grid to battery)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1056, "total_dc_energy_from_pv", "Total DC PV energy (sum of all PV inputs)", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1058, "total_dc_energy_from_pv1", "Total DC energy from PV1", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1060, "total_dc_energy_from_pv2", "Total DC energy from PV2", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1062, "total_dc_energy_from_pv3", "Total DC energy from PV3", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1064, "total_energy_ac_side_to_grid", "Total energy AC-side to grid", "Wh", "Float", "mdi:flash", SensorDeviceClass.ENERGY, 0, "RO", SensorStateClass.TOTAL_INCREASING),
    RegisterInfo(1066, "total_dc_power_sum_of_all_pv_inputs", "Total DC power (sum of all PV inputs)", "W", "Float", "mdi:flash", SensorDeviceClass.POWER, 0, "RO", SensorStateClass.MEASUREMENT),
]