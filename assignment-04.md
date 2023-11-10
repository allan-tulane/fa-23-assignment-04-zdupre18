# CMPS 2200 Assignment 4

In this assignment we'll look at the greedy and dynamic programming paradigms.

**To make grading easier, please place all written solutions directly in `answers.md`, rather than scanning in handwritten work or editing this file.**

All coding portions should go in `main.py` as usual.


## Part 1: Making Change

The pandemic is over and you decide to take a much needed vacation. You arrive in a city called Geometrica, and head to the bank to
exchange $N$ dollars for local currency. In Geometrica they have a
currency that is 1-1 with U.S. Dollars, but they only have
coins. Moreover the coins are in
denominations of powers of $2$ (e.g., $k$ denominations of values $2^0$, $2^1$, \ldots,
$2^k$). You wonder why they have
such strange denominations. You think about it a while, and because
you had such a good Algorithms instructor, you realize that there is a
very clever reason. 

**1a)** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.

**enter answer in `answers.md`**
for n dollars a greedy function would have to have a function to intalize an empty list to store coins gthen iterate through coin denominations in decrerasing order starting from the largest int. If however the curretn denomination is less or = to remaining N then add the max # of coins to the list. This will continue til N becomes 0 


**1b)** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.

  greedy - to prove this take a proffess of c be the coin denominations and N remaining largest coin denominiation would have to be C <= N. The alogiorthsm choice of the largest coin denomination at each step is greedy since its optimal choice since it looks at the largest coin denomination at each step

  optimal substructure - this can be constructed a solution would be to construct optimal solutions to subproblems of the main problem. if we remove off occurrences of c and leave with N -c the optimal sub-problem would be to construct an optimal solution for the og problem. Combining optimal solutions from subproblems 

**enter answer in `answers.md`**


**1c)** What is the work and span of your algorithm?

work = O(1) because its constant and iterates through each step. since its propeprotal to num of coins denominations 
span = O(1) because its also proportion to num of coin denominations and the process denomination equality since each step depends on the previous 

**enter answer in `answers.md`**


## Part 2: Making Change Again

You get tired of Geometrica and travel to the nearby town of
Fortuito. While Fortuito also has a 1-1 exchange rate to the US
Dollar, it has an even stranger system of currency where any given bank
has a completely arbitrary set of denominations ($k$ denominations of
values $D_0, D_2, \ldots, D_k$). There is no guarantee that you can
even make change. So you wonder, given $N$ dollars is it possible to
even make change? If so, how can it be done with as few coins as
possible?

**2a)** You realize the greedy algorithm you devised above doesn't
  work in Fortuito. Give a simple counterexample that shows that the
  greedy algorithm does not produce the fewest number of coins.
  
**enter answer in `answers.md`**
useing the denomaination fo {4,3,1} and n=6
1. choose largest denomination less or equal to N = 4
2. N=2 (6-4)
3. choose larges denominatin less than or equal to n = 1 now add one

result is 6 4 +1+1


**2b)** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.

  for it to be an optimal substrucute it would need to have strucutes for it subproblem as well.

  D - denominations N == num of coins to make change 

  n - D(i) 

**enter answer in `answers.md`**


**2c)** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?

work would be O(kN) span O(n) (k is denominations) 

my process was to make a dynamic program that would be efficient for most of the expected values 
stargting with a for loop that would check the range and then add N+1 and then update the table if the coin reduces the num of coins needed. Then have a final entry in the table continuing the min number of coin. using bottom up allows for largest tob 
**enter answer in `answers.md`**


## Part 3: Edit Distance

In class we proved an optimal substructure property for the **Edit
Distance** problem. This allowed us to implement a simple recursive
algorithm in Python that was horribly inefficient.


**3a)** The code for `MED` from the lecture notes is provided as a
  starting point in `main.py.` Now implement `fast_MED`, a **top-down**
  memoized version of `MED`. Test your implementation code using `test_MED`.


**3b)** Now that you have implemented an efficient algorithm for
  computing edit distance, let's turn to the problem of identifying
  the actual edits between two sequences.

 Notice that in the process of computing the optimal edit
  distance, we can also keep track of the actual sequence of edits to
  each position of $S$ and $T$. Update your implementation of `fast_MED` to
  return the optimal edit distance as well as an *alignment* of the
  two strings which show the edits that yield this distance. An
  alignment just shows what changes are made to $S$ to transform it to
  $T$. For example, suppose $S$=`relevant` and $T$=`elephant`. If
  insertion and deletion costs are both equal to $1$, then the
  edit distance between $S$ and $T$ is 4 and an
  alignment of these two strings would look like this:

  `relev--ant`\
  `-ele-phant`

Implement `fast_align_MED` to return the aligned versions of $S$ and $T$,
and test your code with `test_alignment`.

