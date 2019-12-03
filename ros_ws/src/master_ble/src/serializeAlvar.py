#!/usr/bin/env python
import rospy
import tf2_ros
import sys


def serialize_alvar():
  tags = [str(i) for i in range(16)]
  while not rospy.is_shutdown():
    rospy.sleep(1)
    for num in tags:
      x,y = None, None
      try:
	trans = tfBuffer.lookup_transform("ar_marker_"+num, "base")
      	x, y = trans.transform.translation.x, trans.transform.translation.y
      except:
        print("didn't find transform for", num)
        pass
      print("x,y for ", num, "is: ", "x: ", x, "y: ", y)
	

if __name__ == '__main__':
  rospy.init_node('serialize_alvar')
  print("Node initialized")
  serialize_alvar()
