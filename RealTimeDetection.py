import Leap, sys

class SampleListener(Leap.Listener):
    def on_frame(self, controller):
        # Get the most recent frame
        frame = controller.frame()
        
        # Get hands
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"
            print(handType, "hand, id", hand.id, ", position:", hand.palm_position)
            
            # You can also access fingers, gestures, etc.

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
