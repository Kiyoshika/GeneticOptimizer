"""
- Zach Weaver, 14 May 2021

A genetic inspired numerical optimization algorithm (univariate).

STEPS:
1. Start with a large uniform search space.
2. Take first 10 lowest points (for minimizing).
3. Compute estimate as mean of 10 sampled points.
4. Get variance of 10 sampled points.
5. Generate a new 100 sample uniform with mean +/- 2 std from original 10 samples.
6. Repeat until stopping criteria or loop is exhausted.
"""

import pandas as pd
import numpy as np

# objective function
def o_func(x):
    return 2*(x - 3)**2 + (x + 4)**4 - 4
    
itr = 0
previous = None
minimum_est = None
for i in range(1000):
    if itr == 0:
        points = np.linspace(-10, 10, 100)
    else:
        points = np.random.uniform(low = new_gen_mean - 2*new_gen_var, high = new_gen_mean + 2*new_gen_var, size = 100)
    points_eval = o_func(points)
    
    points_df = pd.DataFrame(points)
    points_eval_df = pd.DataFrame(points_eval)
    point_tuple_df = pd.concat([points_df, points_eval_df], axis=1)
    point_tuple_df.columns = ['point', 'evaluation']
    point_tuple_df = point_tuple_df.sort_values(by=['evaluation'], ascending=True)
    new_gen = np.array(point_tuple_df[['point']][0:10])
    new_gen_mean = np.mean(new_gen)
    new_gen_var = np.std(new_gen)
    if itr == 0:
        previous = np.mean(points)
    else:
        if abs(previous - np.mean(points)) <= 0.00001:
            minimum_est = np.mean(points)
            break
    
    previous = np.mean(points)
    print("Iter #" + str(itr) + ": " + str(np.mean(points)))
    itr += 1

print("Estimate X value of minimum: ", minimum_est)
