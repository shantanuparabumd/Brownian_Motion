import matplotlib.pyplot as plt
import numpy as np

def simulate_ball_movement():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    # Create the ball
    ball = plt.Circle((-5, -5), 0.5, color='r')

    # Add the ball to the plot
    ax.add_patch(ball)

    def move(theta, distance):
        x = distance * np.cos(theta)
        y = distance * np.sin(theta)
        return x, y

    def check_boundary(x, y):
        if x+0.5 > 10 or x-0.5 < -10:
            return True
        if y+0.5 > 10 or y-0.5 < -10:
            return True
        return False

    theta = np.pi/12
    speed = 0.5
    
    # Update the ball position at each iteration
    try:
        while True:
            # Generate random displacements for x and y coordinates
            dx, dy = move(theta, speed)

            # Check if the ball hits the boundary
            if check_boundary(ball.center[0] + dx, ball.center[1] + dy):
                # Reverse the direction of theta to make the ball rebound
                theta = np.random.uniform(0, 2*np.pi)
                dx, dy = move(theta, speed)
            else:
                # Update the ball position
                ball.center = (ball.center[0] + dx, ball.center[1] + dy)

            # Redraw the plot
            plt.pause(0.1)
            plt.draw()

    except KeyboardInterrupt:
        # Handle keyboard interrupt
        print("Keyboard interrupt detected. Exiting...")

        # Update the ball position
        ball.center = (ball.center[0], ball.center[1])

        # Redraw the plot
        plt.pause(0.1)
        plt.draw()

# Call the function to execute the simulation when the module is run
if __name__ == "__main__":
    simulate_ball_movement()
