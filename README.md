# Maze_Solving_Robot

## Scope of the project is the development of a two wheeled mobile RaspBerry Pi Robot.

The components that will be used in the project involve the following:

<ul>
<li>RaspBerry Pi Model B+</li>
<li>1 x Ultrasonic Sensor</li>
<li>Power Bank 10,000mAh</li>
<li>400 point breadboard</li>
<li>DSD TECH USB to TTL Serial adapter</li>
<li>DC Boost Converter</li>
<li>1 x Servo Motor</li>
<li>L293D Motor Driver</li>
<li>IR sensor</li>
</ul>

### Documentation on Sensor Configuration

<h1>IR Sensor</h1>
In case, Pin 21 is disconnected the internal resistor of the Pi will ensure that the value does not fluctuate between 1 and 0. In this case we are using a pull up resistor which means when the wire is disconnected Pin 21 will read a 1
