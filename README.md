#testing

import time
import random

class RobotNavigator:
    def __init__(self):
        self.is_moving = False
        print("[INFO] Robot Navigation System Initialized.")

    def read_ultrasonic_sensor(self):
        # Simulating a distance reading in centimeters
        return random.randint(5, 100)

    def move_forward(self):
        self.is_moving = True
        print("[MOVE] Robot moving forward...")

    def avoid_obstacle(self):
        print("[ALERT] Obstacle detected! Stopping and turning...")
        self.is_moving = False
        time.sleep(1) # Simulate stop duration
        print("[MOVE] Turning 90 degrees right.")
        time.sleep(0.5)

    def run_lifecycle(self):
        print("\n--- Starting Robot Mission Loop ---")
        for loop in range(5): # Simulates 5 processing frames
            distance = self.read_ultrasonic_sensor()
            print(f"[SENSOR] Distance to nearest object: {distance}cm")
            
            if distance < 20:
                self.avoid_obstacle()
            else:
                self.move_forward()
            time.sleep(1)
        
        print("[INFO] Mission loop complete. Returning to docking station.")

if __name__ == "__main__":
    navigator = RobotNavigator()
    navigator.run_lifecycle()
