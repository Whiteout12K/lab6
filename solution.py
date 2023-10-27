import math
from render import InitRender, Render

# Makes sure the terminal pathway is deleted.
print("\033c")

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]


body1 = (1, (0, 0), (5, 5))
body2 = (1, (100, 100), (5, 5))
body3 = (1, (100, -100), (5, 5))
system = [body1, body2, body3]


def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    #print("Calculated distance.")
    tempbody1 = body1[1]
    tempbody2 = body2[1]
    value = math.sqrt((tempbody2[1] - tempbody1[1])**2 + (tempbody2[0] - tempbody1[0])**2)
    #print(tempbody1, tempbody2, " = ", value)
    #print()
    return value

def calculate_angle_and_corddistance(body1, body2):
    """ Get's the angle and x and y distance """
    tempbody1 = body1[1]
    tempbody2 = body2[1]
    x_distance = (tempbody2[0] - tempbody1[0])
    y_distance = (tempbody2[1] - tempbody1[1])
    #print("Calculated angle in each plane.")
    angle = math.atan(y_distance / x_distance) * 57.2958  # Radians to angle
    #print(x_distance, y_distance, " = ", angle)
    #print()
    return (angle, x_distance, y_distance)

def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    distance = calculate_distance(body1, body2)
    tempbody1 = body1[0]
    tempbody2 = body2[0]
    force = G * ((tempbody1 * tempbody2) / (distance ** 2))
    value = calculate_angle_and_corddistance(body1, body2)
    x_force = force * (value[1] / distance)
    y_force = force * (value[2] / distance)
    #print("Calculated force in each plane.")
    #print(distance, tempbody1, tempbody2, x_force, y_force, " = ", force)
    #print()
    return ((x_force), (y_force))

def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    net_force = (0, 0)
    for value in range(1, len(system)):
        force = calculate_force(body, system[value])
        net_force = ((net_force[0] + force[0]), (net_force[1] + force[1]))
    return net_force

def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    net_force = calculate_net_force_on(body, system)
    #print(net_force)
    acceleration_x = net_force[0]; acceleration_x = acceleration_x / body[0]
    acceleration_y = net_force[1]; acceleration_y = acceleration_y / body[0]
    return (acceleration_x, acceleration_y)

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    updated_system = []
    for value in range(0, len(system)):
        test_subject = system[value]
        acceleration = calculate_acceleration(system[0], system)
        velocity_initial = test_subject[2]
        velocity_x = velocity_initial[0]; acceleration_x = acceleration[0]
        velocity_y = velocity_initial[1]; acceleration_y = acceleration[1]
        velocity_x = velocity_x + (acceleration_x * dt)
        velocity_y = velocity_y + (acceleration_y * dt)
        velocity_final = (velocity_x, velocity_y)
        test_subject = (test_subject[0], test_subject[1], velocity_final)
        updated_system.append(test_subject)
    return updated_system
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    velocity_updated = update_velocity(system, dt)
    updated_system = []
    for value in range(0, len(system)):
        extracted_values = velocity_updated[value]
        velocity = extracted_values[2]; position = extracted_values[1]
        velocity_x = velocity[0]; position_x = position[0]
        velocity_y = velocity[1]; position_y = position[1]
        displacement_x = (velocity[0] * dt) + position[0]
        displacement_y = (velocity[1] * dt) + position[1]
        extracted_values = (extracted_values[0], (displacement_x, displacement_y), velocity)
        updated_system.append(extracted_values)
    return updated_system

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    simulation = system
    for value in range(0, num_steps):
        simulation = update(simulation, dt)
    return simulation

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""

    return

if __name__ == '__main__':
    index = simulate(system, 1, 10)
    print(index)





