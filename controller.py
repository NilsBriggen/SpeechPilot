import smbus, time

class Controller():
	def __init__(self):
		self.bus = smbus.SMBus(1) # Setting the correct Bus output
		self.ADDRESS = 0x22 # Setting output address for the picon zero
		self.MOVETIME = 0.5 # The time it takes for the robot to roll 15cm
		self.TURNTIME = 0.5 # The time it takes for the robot to make a 90° turn
		self.SPEED = 100 # The speed with which the robot makes a turn
		self.bus.write_byte_data(self.ADDRESS, 20, 0) # Resetting the Picon Board. '20' clears all input/output configurations
		
		##############################################################
		# !All calculations for angles or distances are estimations! #
		##############################################################
		
	def setMotor(self, motor, speed):
		# Checking if parameters are valid, if they are, move the robot, if they aren't, print debug message
		if motor==0 or motor==1 and speed>=-128 and speed<128:
			try:
				self.bus.write_byte_data(self.ADDRESS, motor, speed) # Writing the motor and speed to the bus
			except:
				print(f"Couldn't write to Motor{motor}")
		else:
			if motor!=0 and motor!=1:
				print(f"Cannot write to Motor{motor}\nChoose either motor 0 or 1")
			else:
				print(f"Cannot write speed {speed}\nMake sure it is between -128 and 127")
				
	def forward(self, distance):
		# With the given parameters, calculate how long the wheels have to spin for a given distance
		self.setMotor(0, self.SPEED)
		self.setMotor(1, self.SPEED)
		travelLength = (distance/15)*self.MOVETIME
		time.sleep(travelLength)
		self.stop()
		
	def reverse(self, distance):
		# With the given parameters, calculate how long the wheels have to spin for a given distance
		self.setMotor(0, -self.SPEED)
		self.setMotor(1, -self.SPEED)
		travelLength = (distance/15)*self.MOVETIME
		time.sleep(travelLength)
		self.stop()
		
	def left(self, angle):
		# With the given parameters, calculate how long the wheels have to spin for a given angle
		turnLength = (angle/90)*self.TURNTIME
		self.setMotor(0, -self.SPEED)
		self.setMotor(1, self.SPEED)
		time.sleep(turnLength)
		self.stop()
		
	def right(self, angle):
		# With the given parameters, calculate how long the wheels have to spin for a given angle
		turnLength = (angle/90)*self.TURNTIME
		self.setMotor(0, self.SPEED)
		self.setMotor(1, -self.SPEED)
		time.sleep(turnLength)
		self.stop()
		
	def stop(self):
		# Stop all movement
		self.setMotor(0, 0)
		self.setMotor(1, 0)
