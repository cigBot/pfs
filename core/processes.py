import os
from core.power import Power
from core.mode import Mode


def power_watchdog(core, eps):
    while True:
        if eps.get_battery_bus_volts() >= Power.NORMAL.value and core.state != Mode.NORMAL:
            core.enter_normal_mode(
                f'Battery level at sufficient state: {eps.get_battery_bus_volts()}')
        elif eps.get_battery_bus_volts() < Power.NORMAL.value and core.state != Mode.LOW_POWER:
            core.enter_low_power_mode(
                f'Battery level at critical state: {eps.get_battery_bus_volts()}')


def is_first_boot():
    if os.listdir().count("first_boot.txt") > 0: # check if the file exists
        os.remove("first_boot.txt") # remove the file if it exists
        return True
    else:
        return False
