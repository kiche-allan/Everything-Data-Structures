# A TV channel needs a tool that determines if a collection of movies A that contains M movies will satisfy all viewers or not.
# Each movie belongs to a subset of genres from a pre-determined set Y.
# The TV channel has a limited number of slots, Z, to fit movies into, with the condition that a movie can only be assigned to a single slot.
# To satisfy all viewers:

 

# All slots must be filled. If you can't due to a shortage of movies, then the viewers can't be satisfied.
# All genres must be covered by the selected movies. A genre is considered covered if 1 or more of the selected movies belong to this genre.
 

# Write a function:
# def solution(A, Y, Z)

 

# that determines if all viewers could be satisfied or not.

 

# Input:

 

 

# A[length M x Y]: An integer array with binary values (0 or 1) representing if each movie i belongs to a genre. Movies are provided sequentially in the array, so for a movie i, the subarray A[i * Y] to A[(i + 1) * Y - 1] represents if it belongs to a genre (1) or not (0).

 

 

# Y: The number of genres

 

 

# Z: The number of slots to fill.

 

 

# Assume that:

 

# (1 <= M <= 20)
# (1 <= Y <= 40)
# (1 <= Z <= 20)
 

# Output:

 

# Boolean: true if all viewers could be satisfied, and false if not.
 

# Example 1:
# Input: A = [1,0,1,1,0,0,0,0,1], Y = 3, Z = 2
# Output: False
# Breakdown of movies:

 

# 1,0,1
# 1,0,0
# 0,0,1
 

# Genre 2 not covered

 

# Example 2:
# Input: A = [1,0,1,1,0,0,0,1,0], Y = 3, Z = 2
# Output: True
# Breakdown of movies:

 

# 1,0,1
# 1,0,0
# 0,1,0
# By selecting movies 1 and 3 to fill the 2 slots, all 3 genres are covered. Thus, satisfying all viewers.