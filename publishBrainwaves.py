#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#from consider import Consider

def talker():
    pub = rospy.Publisher('brainwaves', String)
    rospy.init_node('brainwaves', anonymous=True)
    r = rospy.Rate(10) # 10hz
    #con = Consider()
    while not rospy.is_shutdown():
  str = "hello world %s" % rospy.get_time()
	#str = con.get_packet()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

