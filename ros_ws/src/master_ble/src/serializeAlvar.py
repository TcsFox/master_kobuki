#!/usr/bin/env python
import rospy
import tf2_ros
import sys


def serialize_alvar():
  tags = [str(i) for i in range(16)]
  while not rospy.is_shutdown():
    rospy.sleep(2)
    found = False
    for num in tags:
      x,y = None, None
      try:
	trans = tfBuffer.lookup_transform("ar_marker_"+num, "base")
      	x, y = trans.transform.translation.x, trans.transform.translation.y
      	print("x,y for ", num, "is: ", "x: ", x, "y: ", y)
	found = True
      except:
        pass
    if(not found):
      print("no tags found")
	

if __name__ == '__main__':
  rospy.init_node('serialize_alvar')
  print("Node initialized")
  serialize_alvar()
