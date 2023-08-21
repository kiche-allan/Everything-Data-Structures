When analyzing the time complexity of an algorithm, we often need to add or multiply the running times of different parts of the algorithm to get the overall running time. The decision to add or multiply the running times depends on how the different parts of the algorithm are executed in relation to each other.

If the different parts of the algorithm are executed in a sequential manner, where one part must be completed before the other starts, we add the running times of the different parts to get the overall running time. For example, if part 1 has a running time of T(n) = n and part 2 has a running time of T(n) = n^2, the overall running time of the algorithm is T(n) = n + n^2.

If the different parts of the algorithm are executed in parallel, where they can be executed simultaneously, we multiply the running times of the different parts to get the overall running time. For example, if part 1 has a running time of T(n) = n and part 2 has a running time of T(n) = log(n), the overall running time of the algorithm is T(n) = n * log(n).

If the different parts of the algorithm are executed in a nested way, where one part is executed within the other part, we multiply the running times of the different parts to get the overall running time. For example, if part 1 has a running time of T(n) = n and part 2 has a running time of T(n) = log(n) and part 2 is executed within part 1 for n times, the overall running time of the algorithm is T(n) = n * log(n).

In summary, adding the running times of different parts of an algorithm is used when the parts are executed sequentially, multiplying the running times is used when the parts are executed in parallel or nested way.

It's worth noting that when analyzing the time complexity of an algorithm, it's important to be precise and consider all the cases, including the worst case, average case, and best case scenarios.