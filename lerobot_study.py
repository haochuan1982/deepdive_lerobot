from lerobot.robots.so_follower import SO101Follower, SO101FollowerConfig
import numpy as np
import pinocchio as pin
import time

ARM_JOINTS = ["shoulder_pan", "shoulder_lift", "elbow_flex", "wrist_flex", "wrist_roll"]

robot = SO101Follower(
            SO101FollowerConfig(
                port='/dev/ttyACM0',
                id="my_awesome_follower_arm",
                disable_torque_on_disconnect=True,
                use_degrees=True,
            )
        )
robot.connect()

observation = robot.get_observation()
print(observation)

#for joint, degree in observation.items():
#    observation[joint] = degree + 5
#observation["shoulder_pan.pos"] -= 20
#observation["shoulder_lift.pos"] += 20
#observation["elbow_flex.pos"] += 30
#observation["shoulder_pan.pos"] = 0
#observation["shoulder_lift.pos"] = 30
#observation["elbow_flex.pos"] = 120
#observation["wrist_flex.pos"] = 80
#print(observation)

#robot.send_action(observation)
#time.sleep(2)

observation = robot.get_observation()
print(observation)

robot.disconnect()
