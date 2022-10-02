from __future__ import print_function

import sys
import rospy
from xarm_gazebo.srv import *

def colorComposition_client(color):
    rospy.wait_for_service('colorComposition')
    try:
        colorComposition = rospy.ServiceProxy('colorComposition', AddTwoInts)
        resp1 = colorComposition(color)
        return resp1.coordinates
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [color]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        color = (sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s"%(color))
    print("Color es %s se compone de %s"%(color, colorComposition_client(color)))
