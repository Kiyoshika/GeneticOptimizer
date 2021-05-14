# GeneticOptimizer
A numerical optimizer inspired by genetic algorithms.

Currently this only optimizes univariate functions but should be easy to generalize to multivariate functions.

STEPS:
1. Start with a large uniform search space.
2. Take first 10 lowest points (for minimizing).
3. Compute estimate as mean of 10 sampled points.
4. Get variance of 10 sampled points.
5. Generate a new 100 sample uniform with mean +/- 2 std from original 10 samples.
6. Repeat until stopping criteria or loop is exhausted.
