import rospy
from geometry_msgs.msg import PoseStamped, Quaternion
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import rclpy
from rclpy.node import Node
#from geometry_msgs.msg import PoseStamped, Quaternion

topic_name_ros1 = 'CAM_POS'
topic_name_ros2 = 'CAM_POS'

def get_position_and_orientation():
  #check if ROS1 or ROS2 is running
  is_ros1 = rospy.get_node_uri() is not None
  is_ros2 = not is_ros1

  if is_ros1:
    #initialize ROS1 mode
    rospy.init_mode('position_listener')
    
    def callback_ros1(msg):
      x = msg.pose.position.x
      y = msg.pose.position.y
      z = msg.pose.position.z
      quaternion = (
                  msg.pose.orientation.x,
                  msg.pose.orientation.y,
                  msg.pose.orientation.z,
                  msg.pose.orientation.w
                  )
      roll, pitch. yaw = euler_from_quaternion(quaternion)
      return (x,y,z,roll, pitch. yaw)
      
    rospy.Subscriber(topic_name_ros1, PoseStamped, callback_ros1)
    rospy.spin() # keep the ros1 node alive

    
  elif is_ros2:
    class PositionListener(Node):
      def __init__(self): 
        super().__init__('position_listener')
        self.subscription = self.create)subscription(
        PoseStampted,
        topic_name_ros2,
        10
        )
        self.subscription  # prevent unused variable warning
      def callback_ros2(self, msg):
      x = msg.pose.position.x
      y = msg.pose.position.y
      z = msg.pose.position.z
      quaternion = (
                  msg.pose.orientation.x,
                  msg.pose.orientation.y,
                  msg.pose.orientation.z,
                  msg.pose.orientation.w
                  )
      roll, pitch. yaw = euler_from_quaternion(quaternion)
      return (x,y,z,roll, pitch. yaw)
  
  rclpy.init()
  node = PositionListner()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  try:
    get_position_and_orientation()
  except rospy.ROSInterruptException:
    pass
      


