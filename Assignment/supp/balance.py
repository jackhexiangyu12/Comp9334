#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMP9334 Week 3B 

To derive the state balance equations for the database server example 
automatically
"""

import numpy as np 

# Recall that the states are 
# (#jobs at s1 #jobs at s2)

# Specify all the states as a list of 2-tuples
# changed according to the n1 we want to find
states = [(0,0),
          (0,1),
          (0,2),
          (0,3),
          (0,4),
          (0,5),
          (1,0),
          (1,1),
          (1,2),
          (1,3),
          (1,4),
          (1,5),
          (2,0),
          (2,1),
          (2,2),
          (2,3),
          (2,4),
          (2,5),
          (3,0),
          (3,1),
          (3,2),
          (3,3),
          (3,4),
          (3,5),
          (4,0),
          (4,1),
          (4,2),
          (4,3),
          (4,4),
          (4,5),
          (5,0),
          (5,1),
          (5,2),
          (5,3),
          (5,4),
          (5,5)]

# Each transition in state can be characterised by a 3-tuple
# For example, if a job finishes at the fast disk and moves to the CPU, then
# it can be represented by the tuple
#           (1,-1,0) 
# where: 
#   The 1 in the first position means a job has moved to the CPU,
#   and 
#   -1 in the second position means a job has left the fast disk

#s2 left 
mv_fast_to_cpu = (0,-1)

#s1 left
mv_slow_to_cpu = (-1,0)

#enter s2
mv_cpu_to_fast = (0,1)

#enter s1
mv_cpu_to_slow = (1,0)

# The corresponding transition rate 
rate_fast_to_cpu = 1/0.7
rate_slow_to_cpu = 2
rate_cpu_to_fast = 1
rate_cpu_to_slow = 1

# The number of states 
num_states = len(states)

# Initialise the R matrix which contains the equations for state balance
R = np.zeros((num_states,num_states))

# Loop through all the state pairs to find the elements of the R matrix
for i in range(num_states):         # i is the row index 
    for j in range(num_states):     # j is the column index 
        if i != j:
            # The states 
            state_i = states[i]
            state_j = states[j]
            
            # Determine the transition by subtracting 
            # state_j from state_i 
            change = tuple(np.subtract(state_i, state_j))
            
            # Determine the transition
            if change == mv_fast_to_cpu:
                R[i,j] = -rate_fast_to_cpu
                R[j,j] += rate_fast_to_cpu
            elif change == mv_slow_to_cpu:
                #print(state_i,state_j);
                R[i,j] = -rate_slow_to_cpu
                R[j,j] += rate_slow_to_cpu
            elif change == mv_cpu_to_fast:
                
                if state_i != (0,2) and state_i != (0,3) and state_i != (0,4) and state_i != (0,5) and state_i != (1,3) and state_i != (1,4) and state_i != (1,5) and state_i != (2,3) and state_i != (2,4) and state_i != (2,5) and state_i != (3,4):
                    R[i,j] = -rate_cpu_to_fast 
                    R[j,j] += rate_cpu_to_fast
                else:
                    #print(state_i,state_j)
                    R[j,j] += rate_cpu_to_fast
            elif change == mv_cpu_to_slow: 

                if state_i != (1,0) and state_i != (2,0) and state_i != (3,0) and state_i != (4,0) and state_i != (5,0):
                    R[i,j] = -rate_cpu_to_slow 
                if state_i == (1,5) or state_i == (2,5) or state_i == (3,5) or state_i == (4,5) or state_i == (5,5):
                    R[j,j] += rate_cpu_to_fast
                
            # All other changes are invalid 
                   
print('The state balance equation matrix \n',R)  

