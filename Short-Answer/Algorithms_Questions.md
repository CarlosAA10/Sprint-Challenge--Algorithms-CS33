# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
``` 
This operation takes O(n) time because it is dependent on the size of a, it will have to repeat a certain amount of steps until the while condition is broken off. 
Because it still has to execute certain steps N amount of times until it's condition is met, that is why it still has 0(n) complexity.

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
This operation takes O(n*n) or O(n^2) time. This is because one for loop is already O(n), when you nest another for loop inside of another
you multiply those run times O(n) * O(n). You multiply the n times and they become n^2, therefore for any task that had to run 5 steps for example, ran that in 25 times, this means the number of operations this algorithms executes is exponential
```

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
This operation takes only O(n) time complexity because it executes a certain number of times before it reaches its base case which is returning 0 if bunnies is 0
Because of this this operation runs linearly as it is dependent on the size of the bunnies you input
## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# building stories = n
# eggs = plenty
# if floor is f or higher:
#   eggs break
# elif floor is less than f:
#    eggs don't break

My algorithm would be a function that tests whether or not an egg dropped at a certain floor number breaks or not
because i don't know what floor the eggs begin to break in, and i want to use as minimal amount of eggs as possible for this test
I will go ahead and get the total number of floors in the building

I will then divide that number of floors by 3
this will give me a great floor number to test if the eggs will break or not, 
while dividing by 2 may be a safe bet for knowing whether to go higher or lower, 
if you divide by 3, you are given a smaller number and if the egg breaks there, then you've saved yourself an n amount of eggs from having initially tested with half first
if the eggs break at the computed floor number, go down a floor and then run the test again 
if the eggs break , repeat said instructions until the egg doesn't break on new current floor
this floor is the floor number returned 

else if the eggs don't break at the computed floor number, 
add one to the floor number and test if the eggs break
if the eggs break at that floor number, then the previous floor is the floor number you want returned

although we do try to minimize the amount of eggs used for this test, we still have a time complexity of O(n) because this operation is going to run 
n amount of steps until the conditions are met. 
