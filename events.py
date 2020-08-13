import socket
from gpiozero import DigitalOutputDevice, PhaseEnableMotor, PWMOutputDevice, pi_info, Device, Servo, AngularServo,LineSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from devices import *
from device_layout import *


def check_pigpio_service(host, port, timeout=1):
    # pigpio.pi doesnt have timeout param
    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except Exception:
        return False


def get_pi_info(host, port):
    factory = PiGPIOFactory(host=host, port=port)
    Device.pin_factory = factory
    return '{0:full}'.format(pi_info())


def run(window, device, host, port):
    run_window = window
    factory = PiGPIOFactory(host=host, port=port)

    if device in (N_DigitalOutputDevice, N_LED, N_Buzzer):
        run_window.Layout(led_layout())
        switch = False
        device_open = False
        while True:
            event, values = run_window.read()
            if event == '-pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-open-':
                if not device_open:
                    if values['-pin-'] == 'Select pin':
                        sg.popup_no_titlebar("Select your pin!")
                        continue
                    else:
                        d = DigitalOutputDevice(values['-pin-'], pin_factory=factory)
                        device_open = True
                        run_window['-open-'].update(image_data=icon_close)
                else:
                    device_open = False
                    switch = False
                    run_window['-open-'].update(image_data=icon_open)
                    run_window['-switch-'].update(image_data=icon_switch_off)
                    d.close()

            if event == '-switch-':
                if device_open:
                    switch = not switch
                    run_window['-switch-'].update(image_data=icon_switch_on if switch else icon_switch_off)
                    d.on() if switch else d.off()
                else:
                    sg.popup_no_titlebar("Open device first!")
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

    elif device in (N_PWMOutputDevice, N_PWMLED):
        run_window.Layout(pwmled_layout())
        device_open = False
        while True:
            event, values = run_window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # if not exit-event, get param
            cycle = 0 if str(values['-cycle-']).startswith('Select') else values['-cycle-']
            frequency = 100 if values['-frequency-'].startswith('Select') else int(
                values['-frequency-'].replace('Hz', ''))
            if event == '-pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-frequency-':
                if device_open:
                    d.frequency = frequency
            if event == '-cycle-':
                if device_open:
                    d.value = cycle
            if event == '-open-':
                if not device_open:
                    if values['-pin-'] == 'Select pin':
                        sg.popup_no_titlebar("Select your pin!")
                        continue
                    else:
                        d = PWMOutputDevice(values['-pin-'], initial_value=cycle, frequency=frequency,
                                            pin_factory=factory)
                        device_open = True
                        run_window['-open-'].update(image_data=icon_close)
                else:
                    device_open = False
                    d.close()
                    run_window['-open-'].update(image_data=icon_open)

            if event == '-pulse-':
                if device_open:
                    d.pulse()
                else:
                    sg.popup_no_titlebar("Open device first!")

    elif device == N_Servo:
        run_window.Layout(servo_layout())
        device_open = False
        while True:
            event, values = run_window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            value = 0 if str(values['-value-']).startswith('Select') else values['-value-']
            min_pulse_width = (1 if values['-min_pulse_width-'].startswith('Select') else float(
                values['-min_pulse_width-'].replace('ms', ''))) / 1000
            max_pulse_width = (2 if values['-max_pulse_width-'].startswith('Select') else float(
                values['-max_pulse_width-'].replace('ms', ''))) / 1000
            if event == '-pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-value-':
                if device_open:
                    d.value = value
            if event in ('-min_pulse_width-', '-max_pulse_width-'):
                if device_open:
                    sg.popup_no_titlebar('Pulse-width param only work before open!')
            if event == '-open-':
                if not device_open:
                    if values['-pin-'] == 'Select pin':
                        sg.popup_no_titlebar("Select your pin!")
                        continue
                    else:
                        d = Servo(values['-pin-'], initial_value=value, min_pulse_width=min_pulse_width,
                                  max_pulse_width=max_pulse_width, pin_factory=factory)
                        device_open = True
                        run_window['-open-'].update(image_data=icon_close)
                else:
                    device_open = False
                    d.close()
                    run_window['-open-'].update(image_data=icon_open)

    elif device == N_AngularServo:
        run_window.Layout(angularservo_layout())
        device_open = False
        while True:
            event, values = run_window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            angle = 0 if str(values['-angle-']).startswith('Select') else values['-angle-']
            min_angle = -90 if str(values['-min_angle-']).startswith('Select') else values['-min_angle-']
            max_angle = 90 if str(values['-max_angle-']).startswith('Select') else values['-max_angle-']
            min_pulse_width = (1 if values['-min_pulse_width-'].startswith('Select') else float(
                values['-min_pulse_width-'].replace('ms', ''))) / 1000
            max_pulse_width = (2 if values['-max_pulse_width-'].startswith('Select') else float(
                values['-max_pulse_width-'].replace('ms', ''))) / 1000
            if event == '-pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-angle-':
                if device_open:
                    d.angle = angle
            if event in ('-min_pulse_width-', '-max_pulse_width-', '-min_angle-', '-max_angle-'):
                if device_open:
                    sg.popup_no_titlebar('Pulse-width param only work before open!')
            if event == '-open-':
                if not device_open:
                    if values['-pin-'] == 'Select pin':
                        sg.popup_no_titlebar("Select your pin!")
                        continue
                    else:
                        d = AngularServo(values['-pin-'], initial_angle=angle, min_angle=min_angle, max_angle=max_angle,
                                         min_pulse_width=min_pulse_width,
                                         max_pulse_width=max_pulse_width, pin_factory=factory)
                        device_open = True
                        run_window['-open-'].update(image_data=icon_close)
                else:
                    device_open = False
                    d.close()
                    run_window['-open-'].update(image_data=icon_open)

    elif device == N_PhaseEnableMotor:
        run_window.Layout(phaseenablemotor_layout())
        device_open = False
        while True:
            event, values = run_window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            # if not exit-event, get param
            speed = 0 if str(values['-speed-']).startswith('Select') else values['-speed-']
            if event == '-direction_pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-speed_pin-':
                if device_open:
                    sg.popup_no_titlebar("Close device first!")
            if event == '-speed-':
                if device_open:
                    d.value = speed
            if event == '-open-':
                if not device_open:
                    if values['-direction_pin-'] == 'Select direction pin' or values['-speed_pin-'] == 'Select speed pin':
                        sg.popup_no_titlebar("Select your pin!")
                        continue
                    else:
                        d = PhaseEnableMotor(phase=values['-direction_pin-'],enable=values['-speed_pin-'],pin_factory=factory)
                        d.value = 0
                        device_open = True
                        run_window['-open-'].update(image_data=icon_close)
                else:
                    device_open = False
                    d.close()
                    run_window['-open-'].update(image_data=icon_open)

