import PySimpleGUI as sg
from events import check_pigpio_service, run, get_pi_info
from devices import *
from style import *

sg.theme(window_theme)

connect_layout = sg.Frame('Access',
                          [[sg.Text('Host:'), sg.InputText(default_text='192.168.122.92', size=(15, 1), key='-host-'),
                            sg.InputText(default_text='8888', size=(6, 1), justification='center', key='-port-'),
                            sg.Button('connect', size=(8, 1), key='-connect-')]
                           ])

status_layout = sg.Frame('Status',
                         [[sg.Button(image_data=icon_status_off, key='-status-',
                                     button_color=(sg.theme_background_color(), sg.theme_background_color())),
                           sg.Button(image_data=icon_pi, size=(50, 20),
                                     button_color=(sg.theme_background_color(), sg.theme_background_color()),
                                     key='-pi-')]
                          ])

device_layout = sg.Frame('Device List', [[sg.Listbox(Devices, size=(18, 10),
                                                     background_color=sg.theme_background_color(), enable_events=True,
                                                     key='-device-')]])

description_layout = sg.Frame('Description',
                              [[sg.ML('Here is device description', font='Ubuntu 11', size=(30, 10),
                                      key='-description-')]])

column1 = sg.Column([[connect_layout]])
column2 = sg.Column([[status_layout]])
column3 = sg.Column([[device_layout]])
column4 = sg.Column([[description_layout]])

layout = [
    [column1, column2],
    [column3, column4],
]

window = sg.Window('gpiozero gui', layout, size=(500, 300), finalize=True)
is_connected = False

while True:  # Event Loop
    event, values = window.read()
    if event == '-connect-':
        # when click to connect
        if not is_connected:
            result = check_pigpio_service(values['-host-'], values['-port-'])
            if result:
                is_connected = not is_connected
                sg.popup_no_titlebar('Connect success!', auto_close=True, background_color='red')
                window['-connect-'].update(text='disconnect')
                window['-status-'].update(image_data=icon_status_on)
            else:
                sg.popup_no_titlebar('Failed connect!', background_color='red')
        # when click to disconnect
        else:
            is_connected = not is_connected
            window['-connect-'].update(text='connect')
            window['-status-'].update(image_data=icon_status_off)
    if event == '-pi-':
        if not is_connected:
            sg.popup_no_titlebar('Connect first!', background_color='red')
        else:
            sg.popup('Pi info', get_pi_info(values['-host-'], values['-port-']))
    if event == '-device-':
        if not is_connected:
            sg.popup_no_titlebar('Connect first!', background_color='red')
        else:
            # Listbox has select mod , used to determine if only 1 item can be selected or multiple
            device = values['-device-'][0]
            # update device description
            window['-description-'].update(value=eval('D_{}'.format(device)))
            # create new window
            window2 = sg.Window('run')
            # normal close or except Exception will close window
            try:
                run(window2, device, values['-host-'], values['-port-'])
            except Exception as e:
                sg.popup_no_titlebar(e, background_color='red')
            finally:
                window2.close()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()
