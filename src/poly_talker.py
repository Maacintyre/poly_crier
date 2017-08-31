#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from random import randint

def talker():
	words = ["Dean","Jon","Vamsi"]

	rospy.init_node('talker')

	pub = rospy.Publisher('names', String)

	rate = rospy.Rate(21)

	while not rospy.is_shutdown():
		number = randint(0,2)
		pub.publish(words[number])
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
