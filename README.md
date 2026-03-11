# Assignment-6-Summary-Report-Medians-Order-Statistics-and-Elementary-Data-Structures
Assignment 6 Summary Report: Medians, Order Statistics, and Elementary Data Structures

The main purpose of this assignment is to help us understand order statistics and elementary data structures. 

- We are going to develop programs that will demonstrate the implementation and then we will analyze the results. The assignment is divided into two parts where the first part is about implementing the algorithms and finding the k-th smallest element in an array using two approaches: a deterministic algorithm and a randomized algorithm (Ryalat, 2022). 

- The second part is about the implementation of basic data structures like arrays, stacks, queues, and linked lists (Lafore et al., 2022).


resutsl for part 1
Sample Array: [12, 3, 5, 7, 4, 19, 26, 3, 7]
4-th smallest using Deterministic Select: 5
4-th smallest using Randomized Quickselect: 5


EMPIRICAL ANALYSIS
============================================================

Input Size: 100
Random:
  Deterministic Select -> Result: 53587, Time: 0.000058 seconds
  Randomized Quickselect -> Result: 53587, Time: 0.000041 seconds
Sorted:
  Deterministic Select -> Result: 50, Time: 0.000048 seconds
  Randomized Quickselect -> Result: 50, Time: 0.000027 seconds
Reverse Sorted:
  Deterministic Select -> Result: 50, Time: 0.000038 seconds
  Randomized Quickselect -> Result: 50, Time: 0.000020 seconds

Input Size: 500
Random:
  Deterministic Select -> Result: 49962, Time: 0.000242 seconds
  Randomized Quickselect -> Result: 49962, Time: 0.000058 seconds
Sorted:
  Deterministic Select -> Result: 250, Time: 0.000213 seconds
  Randomized Quickselect -> Result: 250, Time: 0.000097 seconds
Reverse Sorted:
  Deterministic Select -> Result: 250, Time: 0.000221 seconds
  Randomized Quickselect -> Result: 250, Time: 0.000110 seconds

Input Size: 1000
Random:
  Deterministic Select -> Result: 49384, Time: 0.000494 seconds
  Randomized Quickselect -> Result: 49384, Time: 0.000243 seconds
Sorted:
  Deterministic Select -> Result: 500, Time: 0.000428 seconds
  Randomized Quickselect -> Result: 500, Time: 0.000203 seconds
Reverse Sorted:
  Deterministic Select -> Result: 500, Time: 0.000379 seconds
  Randomized Quickselect -> Result: 500, Time: 0.000134 seconds

Input Size: 2000
Random:
  Deterministic Select -> Result: 50721, Time: 0.000960 seconds
  Randomized Quickselect -> Result: 50721, Time: 0.000283 seconds
Sorted:
  Deterministic Select -> Result: 1000, Time: 0.000802 seconds
  Randomized Quickselect -> Result: 1000, Time: 0.000258 seconds
Reverse Sorted:
  Deterministic Select -> Result: 1000, Time: 0.000787 seconds
  Randomized Quickselect -> Result: 1000, Time: 0.000395 seconds



results for part two 
ARRAY
After insertions: [10, 20, 30]
Access index 1: 20
After deletion: [10, 30]

MATRIX
[5, 0, 0]
[0, 0, 9]
Access [1][2]: 9
After deletion:
[5, 0, 0]
[0, 0, 0]

STACK
Stack: [100, 200, 300]
Pop: 300
After pop: [100, 200]

QUEUE
Queue: [1, 2, 3]
Dequeue: 1
After dequeue: [2, 3]

SINGLY LINKED LIST
Linked List: [5, 11, 22]
After deletion: [5, 11]

