# device name
N_DigitalOutputDevice = 'DigitalOutputDevice'
N_LED = 'LED'
N_Buzzer = 'Buzzer'
N_PWMOutputDevice = 'PWMOutputDevice'
N_PWMLED = 'PWMLED'
N_Servo = 'Servo'
N_AngularServo = 'AngularServo'
N_PhaseEnableMotor = 'PhaseEnableMotor'
N_Button = 'Button'
N_LineSensor = 'LineSensor'
N_MotionSensor = 'MotionSensor'
N_LightSensor = 'LightSensor'

Devices = [N_DigitalOutputDevice, N_LED, N_Buzzer, N_PWMOutputDevice, N_PWMLED, N_Servo, N_AngularServo,
           N_PhaseEnableMotor, N_Button, N_LineSensor, N_MotionSensor, N_LightSensor]

# device description
D_DigitalOutputDevice = "Represents a generic output device with typical on/off behaviour"
D_LED = "Extends DigitalOutputDevice and represents a light emitting diode (LED).\n" \
        "Connect the cathode (short leg, flat side) of the LED to a ground pin;\n" \
        "Connect the anode (longer leg) to a limiting resistor;\n" \
        "Connect the other side of the limiting resistor to a GPIO pin\n" \
        "(the limiting resistor can be placed either side of the LED)"
D_Buzzer = "Extends DigitalOutputDevice and represents a digital buzzer component.\n" \
           "Connect the cathode (negative pin) of the buzzer to a ground pin;\n" \
           "Connect the other side to any GPIO pin.\n"
D_PWMOutputDevice = "Generic output device configured for pulse-width modulation (PWM)."
D_PWMLED = "Extends PWMOutputDevice and represents a light emitting diode (LED) with variable brightness.\n" \
           "A typical configuration of such a device is to connect a GPIO pin to the anode (long leg) of the LED," \
           " and the cathode (short leg) to ground, with an optional resistor to prevent the LED from burning out"
D_Servo = "Extends CompositeDevice and represents a PWM-controlled servo motor connected to a GPIO pin.\n" \
          "Connect a power source (e.g. a battery pack or the 5V pin) to the power cable of the servo " \
          "(this is typically colored red); connect the ground cable of the servo (typically colored black or brown)" \
          " to the negative of your battery pack, or a GND pin; connect the final cable " \
          "(typically colored white or orange) to the GPIO pin you wish to use for controlling the servo"
D_AngularServo = "Extends Servo and represents a rotational PWM-controlled servo motor which can be set to " \
                 "particular angles (assuming valid minimum and maximum angles are provided to the constructor).\n" \
                 "Connect a power source (e.g. a battery pack or the 5V pin) to the power cable of the servo " \
                 "(this is typically colored red); connect the ground cable of the servo " \
                 "(typically colored black or brown) to the negative of your battery pack, or a GND pin; " \
                 "connect the final cable (typically colored white or orange) to " \
                 "the GPIO pin you wish to use for controlling the servo."
D_PhaseEnableMotor = "Represents a generic motor connected to a Phase/Enable" \
                     " motor driver circuit; the phase of the driver controls whether the motor turns forwards" \
                     "or backwards, while enable controls the speed with PWM."
D_Button = "Represents a simple push button or switch.\n" \
           "Connect one side of the button to a ground pin, " \
           "and the other to any GPIO pin. Alternatively, connect one side of the button to the 3V3 pin, " \
           "and the other to any GPIO pin, then set pull_up to False in the Button constructor"
D_LineSensor = "Represents a single pin line sensor like the TCRT5000 infra-red proximity sensor\n" \
               "A typical line sensor has a small circuit board with three pins: VCC, GND, and OUT. " \
               "VCC should be connected to a 3V3 pin, GND to one of the ground pins, " \
               "and finally OUT to the GPIO specified as the value of the pin parameter in the constructor."
D_MotionSensor = "Represents a passive infra-red (PIR) motion sensor\n" \
                 "A typical PIR device has a small circuit board with three pins: VCC, OUT, and GND. " \
                 "VCC should be connected to a 5V pin, GND to one of the ground pins, " \
                 "and finally OUT to the GPIO specified as the value of the pin parameter in the constructor."
D_LightSensor = "Represents a light dependent resistor (LDR).\n" \
                "Connect one leg of the LDR to the 3V3 pin; connect one leg of a 1µF capacitor to a ground pin; " \
                "connect the other leg of the LDR and the other leg of the capacitor to the same GPIO pin. " \
                "This class repeatedly discharges the capacitor, " \
                "then times the duration it takes to charge (which will vary according to the light falling on the LDR)"
