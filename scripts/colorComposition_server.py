from __future__ import print_function

from xarm_gazebo.srv import colorComposition,colorCompositionResponse
import rospy

def handle_colorComposition(req):
    print("Received color [%s]"%(req.color))
    msg = []
    if (req.color=="green"):
        msg.append("(yellow, blue)")
        msg.append("(blue, yellow)")
        return colorCompositionResponse(msg)
    else:
        return colorCompositionResponse(["¿?"])

def colorComposition_server():
    rospy.init_node('colorComposition_server')
    s = rospy.Service('colorComposition', colorComposition, handle_colorComposition)
    print("Ready to receive color.")
    rospy.spin()

if __name__ == "__main__":
    colorComposition_server()