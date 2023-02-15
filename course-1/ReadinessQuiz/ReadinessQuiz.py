# 1. For a given input list: 1, 2, 3, 4

def get_cubed(lst):
  """
  INPUT: list (containing numeric elements)
  OUTPUT: list (cubed value of each even number in original list)
  Return a list containing the cubed value of each element.
  """
  return [n**3 for n in lst]

print(get_cubed([1, 2, 3, 4]))



# 2. For a given input list: 1,2,3,4,5,6,7

def get_squared_evens(lst):
  """
  INPUT: list (containing numeric elements)
  OUTPUT: list (squared value of each even number in original list)
  Return a list containing the squared value of each even number.
  """
  return [n**2 for n in lst if n % 2 == 0]

print(get_squared_evens([1, 2, 3, 4, 5, 6, 7]))


# 3. Which of the following is/are NOT native or built-in data types in Python?

#heap
#varchar


# 4. For given input lists:  a,b,c  and 1,2,3

def make_dict(lst1,lst2):
    '''
    INPUT: LST1, LST2
    OUTPUT: DICT (LST 1 are the keys and LST2 are the values)
    Given equal length lists create a dictionary where the first list is the keys
    '''
    res = dict(zip(lst1, lst2))
    return res

print(make_dict(['a','b','c'], [1,2,3]))


# 5. Mutable data types/collections in Python can be changed in place. Immutable ones can not change
#in place. Which of the following are mutable?

#set, list


# 6. Which of the following is NOT true about Python?

#Base Python automatically parallelizes processing across cores when multiple cores are available


# 7. For a given input list: abbcccddddeeeeeffffffggggggghhhhhhhh

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)

    Return a dictionary of character counts
    '''
    res = {i : string.count(i) for i in set(string)}
    return res


print(count_characters('abbcccddddeeeeeffffffggggggghhhhhhhh'))


# 8. For the vector v = [2.0, -3.5, 5.1]:

import numpy as np

def calculate_l1_norm(v):
  '''
  INPUT: LIST or ARRAY (containing numeric elements)
  OUTPUT: FLOAT (L1 norm of v)
  calculate and return a norm for a given vector
  '''
  vec_norm = np.linalg.norm(v,1)
  return vec_norm

v = [2.0, -3.5, 5.1]
calculate_l1_norm(v)


# 9. NumPy array practice

import numpy as np

def get_vector_sum(vectorLower, vectorUpper):
  '''
  INPUT: vector lower and upper bounds
  OUTPUT: calculated value for vector sum
  (1) create a vector ranging from 1:150
  (2) transform the vector into a matrix with 10 rows and 15 columns
  (3) print the sum for the 10 rows
  '''


# 10. Which of the following pairs of events are mutually exclusive. There can be more than one answer.

#Negative numbers and positive numbers less than 25
#Numbers between 100-200 and numbers between 201-300


# 11. Geometric distribution

import scipy.stats as stats

def geometric_distribution(p,k):
  '''
  INPUT: probability of success and trials
  OUTPUT: determined probability
  '''


# 12. Poisson distribution

import scipy.stats as stats

def poisson_distribution(mu,k):
  '''
  INPUT: parameter of the poisson distribution and number of accidents
  OUTPUT: determined probability
  '''


# 13. Gaussian distribution

import scipy.stats as stats

def gaussian_distribution(loc_val, scale_val, cdf_val):
    '''
    INPUT: loc (mean of the distribution), scale (standard deviation of the distribution), and cdf values
    OUTPUT: determined probability
    '''


# 14. Perform matrix multiplication on a square matrix HINT: A 2X2 matrix times a 2x2 matrix should yield a 2x2 matrix

def matrix_multiplication(A,B):
  '''
  INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS
  LIST (of length n) OF LIST (of length n) OF INTEGERS
  OUTPUT: LIST OF LIST OF INTEGERS
  (storing the product of a matrix multiplication operation)
  Return the matrix which is the product of matrix A and matrix B
  where A and B will be (a) integer valued (b) square matrices
  (c) of size n-by-n (d) encoded as lists of lists, e.g.
  A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
  | 2 3 4 |
  | 6 4 2 |
  |-1 2 0 |
  You may not use numpy. Write your solution in straight python
  '''
  res = [[0 for x in range(3)] for y in range(3)]
  
  # explicit for loops
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        # resulted matrix
        res[i][j] += A[i][k] * B[k][j]
        
  return res

A = [[12,7,3], [4,5,6], [7,8,9]]
B = [[1,0,0], [0,1,0], [0,0,1]]

matrix_multiplication(A, B)