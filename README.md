<!-- Write something about the comments at the beginning of lagrange.py -->
# lagrange.py --> The File For Copying Expressions for Acceleration
It has been a long time since I have used this, but when I run it as is, it will print out the
equations for the Lagrange equations for an N-link manipulator.
The equations are printed in a way that is easy to copy and paste into another Python or JavaScript program.
There is another way to get it to print out LaTeX code, but I don't remember how to do that.
In the case of just copying the equations for simulations, change the N value to the number of links you want.
Then run the program and copy the equations into your program.

<!-- Write something about robot_simulation_*.py files -->
# robot_simulation_*.py --> The Files For Simulating the Robot Manipulator
These files are for simulating the robot manipulator.
robot_simulation_euler.py --> Uses Euler's Method
robot_simulation_rk4.py --> Uses Runge-Kutta 4th Order Method

In both of these files, you can change the N value to the number of links you want.
You will also need to change the initial conditions for the robot manipulator to match the amount of links you chose.
There are also optional initial conditions for the robot manipulator.
Then run the program and it will simulate the robot manipulator.
They will output files into a folder, in which you can copy the data into another program to simulate the robot manipulator.