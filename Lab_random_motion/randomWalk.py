import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as p3 
import matplotlib.animation as animation 

def path_generator(steps, step): 
    path = np.zeros((3, steps)) 
    for i in range(1, steps): 
     x_ran, y_ran, z_ran = np.random.rand(3) 
     sgnX = (x_ran - 0.5)/abs(x_ran - 0.5) 
     sgnY = (y_ran - 0.5)/abs(y_ran - 0.5) 
     sgnZ = (z_ran - 0.5)/abs(z_ran - 0.5) 
     dis = np.array([step*sgnX, step*sgnY, step*sgnZ]) 
     path[:, i] = path[:, i - 1] + dis 

    return path 

def animate(i): 
    global particles, trajectories 
    for trajectory, particle in zip(trajectories, particles): 
     trajectory.set_data(particle[0:2, :i]) 
     trajectory.set_3d_properties(particle[2, :i]) 

def random_walk_3D_animated(n, traj = 1): 
    global particles, trajectories 
    fig = plt.figure() 
    ax = p3.Axes3D(fig) 

    particles = [path_generator(n, 1) for i in range(traj)] 
    print(type(particles))
    trajectories = [ax.plot(particle[0, 0:1], particle[1, 0:1], particle[2, 
        0:1])[0] for particle in particles] 
    ax.set_xlim3d([-100, 100]) 
    ax.set_ylim3d([-100, 100]) 
    ax.set_zlim3d([-100, 100]) 

    animacion = animation.FuncAnimation(fig, animate, 1000, interval=500, 
             blit=False) 
    return animacion 

ani = random_walk_3D_animated(10000, traj = 1) 
plt.show() 