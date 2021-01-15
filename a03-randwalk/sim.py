import matplotlib.pyplot as plt
import numpy as np
import randomwalker as rw

# ---------------------------
# Exercise 1
# ---------------------------
def ind_sim(steps=100):

    # Run simulation
    a = rw.Person()
    for i in range(steps):
        a.step()
        a.record()

    # Plot results
    plt.plot(a.x_hist,a.y_hist)
    plt.axis([-10, 10, -10, 10])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Bird's eye view of random walker")
    plt.show()
    plt.plot(a.d_hist)
    plt.xlabel("Number of steps")
    plt.ylabel("Distance from center")
    plt.title("Distance over time")
    plt.show()

# ---------------------------
# Exercise 2
# ---------------------------
def group_sim(steps=100, groupsize = 50):

    # Create population
    group = []
    for i in range(groupsize):
        group.append(rw.Person())
        
    # Run simulation
    for i in range(steps):
        for ind in group:
            ind.step()
            ind.record()

    # Plot individual bird's eye view
    for ind in group:
        plt.plot(ind.x_hist,ind.y_hist)
    plt.axis([-20, 20, -20, 20])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Bird's eye view of random walker")
    plt.show()
    
    # Plot average distance
    dist = np.zeros(steps+1)
    for ind in group:
        dist += ind.d_hist
        plt.plot(ind.d_hist,alpha=0.5)
    dist /= groupsize
    plt.plot(dist,'k')
    plt.xlabel("Number of steps")
    plt.ylabel("Distance from center")
    plt.title("Average distance over time")
    plt.show()

        
