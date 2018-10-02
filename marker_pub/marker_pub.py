#!/usr/bin/env python
# license removed for brevity
import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
import numpy as np

def load_points():
    data = np.loadtxt('points.txt', delimiter=',')
    points = []
    current_list = []
    for d in data:
        if d[0] == 0.0 and d[1] == 0.0:
            points.append(current_list)
            current_list = list()
        else:
            current_list.append([d[0], d[1]])
    return points

if __name__ == '__main__':
    rospy.init_node('shape_marker_pub', anonymous=True)
    pub = rospy.Publisher('/visualization_marker_array', MarkerArray, queue_size=1)
    rospy.sleep(1)
    points = load_points()
    markers = MarkerArray()
    line_color = ColorRGBA()       # a nice color for my line (royalblue)
    line_color.r = 0.254902
    line_color.g = 0.411765
    line_color.b = 0.882353
    line_color.a = 1.0
    for i, poly in enumerate(points):
        m = Marker()
        m.id = i
        m.header.frame_id = 'map'
        m.header.stamp = rospy.Time.now()
        m.type = Marker.LINE_STRIP
        m.lifetime = rospy.Duration(0)
        m.scale.x = 0.1
        for vertex in poly:
            point = Point()
            point.x = vertex[0]
            point.y = vertex[1]
            point.z = 0.1
            m.points.append(point)
            m.colors.append(line_color)
        markers.markers.append(m)

    pub.publish(markers)
    rospy.sleep(1)
