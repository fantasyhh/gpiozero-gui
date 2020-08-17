import PySimpleGUI as sg
from style import *

pins = ['GPIO{}'.format(i) for i in range(2, 28)]


class SgButton(sg.Button):
    def __init__(self, **kwargs):
        if 'button_color' in kwargs:
            super().__init__(border_width=0, **kwargs)
        else:
            super().__init__(button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0,
                             **kwargs)


class SgCombo(sg.Combo):
    def __init__(self, values, **kwargs):
        super().__init__(values=values, size=(20, 1), enable_events=True, readonly=True, **kwargs)


def led_layout():
    layout = [
        [SgCombo(pins, default_value='Select pin', tooltip='The GPIO pin which the device is connected to',
                 key='-pin-')],
        [SgButton(image_data=icon_open, tooltip='Open/Close the device', key='-open-'),
         SgButton(image_data=icon_switch_off, tooltip='Turns the device on/off', key='-switch-')]
    ]
    return layout


def pwmled_layout():
    frequency_list = [str(i) + 'Hz' for i in
                      (50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 1000000, 10000000)]
    cycle_list = [round(x * 0.1, 1) for x in range(0, 11)]
    layout = [
        [SgCombo(pins, default_value='Select pin', tooltip='The GPIO pin which the device is connected to',
                 key='-pin-')],
        [SgCombo(frequency_list, default_value='Select frequency',
                 tooltip='The frequency (in Hz) of pulses emitted to drive the device. Defaults to 100Hz',
                 key='-frequency-')],
        [SgCombo(cycle_list, default_value='Select cycle',
                 tooltip="If 0 (the default), the device’s duty cycle will be 0 initially. " \
                         "Other values between 0 and 1 can be specified as an initial duty cycle. ",
                 key='-cycle-')],
        [SgButton(image_data=icon_open,
                  tooltip='Open/Close the device ', key='-open-'),
         SgButton(image_data=icon_pulse, tooltip='Make the device fade in and out repeatedly', key='-pulse-')],
    ]
    return layout


def servo_layout():
    value_list = [round(x * 0.1, 1) for x in range(-10, 11, 2)]
    min_pulse_width_list = [str(i) + 'ms' for i in [0.5, 1.0, 1.5, 2.0, 2.5, 3]]
    max_pulse_width_list = [str(i) + 'ms' for i in [0.5, 1.0, 1.5, 2.0, 2.5, 3]]
    layout = [
        [SgCombo(pins, default_value='Select pin',
                 tooltip='The GPIO pin which the device is connected to', key='-pin-')],
        [SgCombo(value_list, default_value='Select value',
                 tooltip="Represents the position of the servo as a value between -1 (the minimum position) "
                         "and +1 (the maximum position).  Defaults 0",
                 key='-value-')],
        [SgCombo(min_pulse_width_list, default_value='Select min_pulse_width',
                 tooltip="The pulse width corresponding to the servo’s minimum position. This defaults to 1ms",
                 key='-min_pulse_width-')],
        [SgCombo(max_pulse_width_list, default_value='Select max_pulse_width',
                 tooltip="The pulse width corresponding to the servo’s maximum position. This defaults to 2ms",
                 key='-max_pulse_width-')],
        [SgButton(image_data=icon_open, tooltip='Open/Close the device ', key='-open-')],
    ]
    return layout


def angularservo_layout():
    angle_list = [-180, -135, -90, -45, 0, 45, 90, 135, 180]
    min_angle_list = [-180, -135, -90, -45, 0]
    max_angle_list = [0, 45, 90, 135, 180]
    min_pulse_width_list = [str(i) + 'ms' for i in [0.5, 1.0, 1.5, 2.0, 2.5, 3]]
    max_pulse_width_list = [str(i) + 'ms' for i in [0.5, 1.0, 1.5, 2.0, 2.5, 3]]
    layout = [
        [SgCombo(pins, default_value='Select pin',
                 tooltip='The GPIO pin which the device is connected to', key='-pin-')],
        [SgCombo(angle_list, default_value='Select angle',
                 tooltip="Sets the servo’s initial angle to the specified value. The default is 0." \
                         "The value specified must be between min_angle and max_angle inclusive.",
                 key='-angle-')],
        [SgCombo(min_angle_list, default_value='Select min_angle',
                 tooltip="Sets the minimum angle that the servo can rotate to. This defaults to -90, " \
                         "but should be set to whatever you measure from your servo during calibration",
                 key='-min_angle-')],
        [SgCombo(max_angle_list, default_value='Select max_angle',
                 tooltip="Sets the maximum angle that the servo can rotate to. This defaults to 90, " \
                         "but should be set to whatever you measure from your servo during calibration.",
                 key='-max_angle-')],
        [SgCombo(min_pulse_width_list, default_value='Select min_pulse_width',
                 tooltip="The pulse width corresponding to the servo’s minimum position. This defaults to 1ms",
                 key='-min_pulse_width-')],
        [SgCombo(max_pulse_width_list, default_value='Select max_pulse_width',
                 tooltip="The pulse width corresponding to the servo’s maximum position. This defaults to 2ms",
                 key='-max_pulse_width-')],
        [SgButton(image_data=icon_open, tooltip='Open/Close the device ', key='-open-')],
    ]
    return layout


def phaseenablemotor_layout():
    speed_list = [round(x * 0.1, 1) for x in range(0, 11)]
    layout = [
        [SgCombo(pins, default_value='Select direction pin',
                 tooltip='The GPIO pin that the phase (direction) input of the motor driver chip is connected to',
                 key='-direction_pin-')],
        [SgCombo(pins, default_value='Select speed pin',
                 tooltip='The GPIO pin that the enable (speed) input of the motor driver chip is connected to',
                 key='-speed_pin-')],
        [SgCombo(speed_list, default_value='Select speed',
                 tooltip="Represents the speed of the motor as a floating point value between -1 (full speed backward)" \
                         "and 1 (full speed forward).",
                 key='-speed-')],
        [SgButton(image_data=icon_open,
                  tooltip='Open/Close the device ', key='-open-')]
    ]
    return layout


def button_layout():
    pull_up_list = [True, False]
    layout = [
        [SgCombo(pins, default_value='Select pin',
                 tooltip='The GPIO pin that the phase (direction) input of the motor driver chip is connected to',
                 key='-pin-')],
        [SgCombo(pull_up_list, default_value='Select pull up',
                 tooltip="If True (the default), the GPIO pin will be pulled high,If False, be pulled low ",
                 key='-pull_up-')],
        [SgButton(image_data=icon_open, tooltip='Open/Close the device ', key='-open-'),
         SgButton(button_text='Test', button_color=None, tooltip='test pressed and released', key='-test-')
         ]
    ]
    return layout


def linesensor_layout():
    layout = [
        [SgCombo(pins, default_value='Select pin',
                 tooltip='The GPIO pin that the phase (direction) input of the motor driver chip is connected to',
                 key='-pin-')],
        [SgButton(image_data=icon_open, tooltip='Open/Close the device ', key='-open-'),
         SgButton(button_text='Test', button_color=None, tooltip='test device state changes', key='-test-')
         ]
    ]
    return layout
