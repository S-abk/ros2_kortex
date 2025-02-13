#Gripper Action Client
#This code positions the grippers to desired position

import rclpy
from rclpy.action import ActionClient
from control_msgs.action import GripperCommand

def gripper_action_client():
    rclpy.init()

    # Create a node
    node = rclpy.create_node('gripper_action_client')

    # Create an ActionClient
    client = ActionClient(node, GripperCommand, '/robotiq_gripper_controller/gripper_cmd')

    # Wait for the action server to become available
    if not client.wait_for_server(timeout_sec=5.0):
        print('Action server not available')
        return

    # Create a goal with the desired command parameters
    goal = GripperCommand.Goal()
    goal.command.position = 0.0  # Desired position of the gripper
    goal.command.max_effort = 100.0  # Maximum effort the gripper should use

    # Send the goal
    future = client.send_goal_async(goal)
    
    # Wait for the result
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        print('Goal was accepted!')
    else:
        print('Goal was rejected :(')

    # Cleanup
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    gripper_action_client()

