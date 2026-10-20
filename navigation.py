import time
import random

class RobotNavigator:
    def __init__(self):
        self.is_moving = False
        print("[INFO] Beach Clean-Up Rover Navigation System Initialized.")

    def read_ultrasonic_sensor(self):
        # Simulating distance tracking to shoreline or obstacles
        return random.randint(5, 100)

    def move_forward(self):
        self.is_moving = True
        print("[MOVE] Rover patrolling coastline forward...")

    def avoid_obstacle(self):
        print("[ALERT] Dynamic obstacle detected! Halting drive motors...")
        self.is_moving = False
        time.sleep(1) 
        print("[MOVE] Executing pivot turn to clear path boundary.")
        time.sleep(0.5)

    def run_lifecycle(self):
        print("\n--- Starting Autonomous Rover Mission Loop ---")
        for loop in range(5): 
            distance = self.read_ultrasonic_sensor()
            print(f"[SENSOR] Distance to nearest boundary: {distance}cm")
            
            if distance < 25:
                self.avoid_obstacle()
            else:
                self.move_forward()
            time.sleep(1)
        
        print("[INFO] Mission sequence complete. Returning to collection base.")

if __name__ == "__main__":
    navigator = RobotNavigator()
    navigator.run_lifecycle()
