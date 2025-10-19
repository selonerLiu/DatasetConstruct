# topic：Operators: Defined operators in ProVerif: Meanings, Usage methods.

---
**1. Which of the following is a keyword in the ProVerif language and cannot be used as an identifier?**
A) variable
B) const
C) function
D) process
**Answer:** B
---
**2. In ProVerif, when aiming for better performance, what should be used instead of equations?**
A) Constructors
B) Destructors
C) Variables
D) Names
**Answer:** B
---
**3. How can you adjust the precision and cost of the analysis in ProVerif?**
A) By changing the number of parallel processes
B) By adjusting the arguments of patterns that represent names
C) By using more function symbols
D) By increasing the number of conditional statements
**Answer:** B
---
**4. What is the default behavior in ProVerif regarding testing the attacker's ability?**
A) Testing if the attacker can distinguish a value from a fresh random value
B) Testing if the attacker can compute the value of x
C) Testing if the attacker can create new names
D) Testing if the attacker can break the encryption
**Answer:** B
---
**5. What is the main difference between ProVerif's calculus and the applied pi calculus?**
A) ProVerif uses equations instead of destructors
B) ProVerif uses destructors instead of equational theories
C) The applied pi calculus has no functions on terms
D) ProVerif does not extend the pi calculus
**Answer:** B
---
**6. In the ProVerif language with certain additional conditions, how is the destructor “equal” written?**
A) equal(M, N)
B) M == N
C) M = N
D) eq(M, N)
**Answer:** C
---
**7. In ProVerif, what is an evaluation context?**
A) A process with a hole not under a replication, a conditional, an input, or an output
B) A process with a hole only under a replication
C) A process with a hole under any operator
D) A process without any holes
**Answer:** A
---
**8. What does setting “set predicatesImplementable = check” do in ProVerif?**
A) It checks if predicate calls are implementable
B) It disables all predicate calls
C) It makes all predicates public
D) It checks if all names are fresh
**Answer:** A
---
**9. In ProVerif, what does the “new” operator do in a process declaration?**
A) It creates a new function symbol
B) It creates a new predicate
C) It creates a new name restriction
D) It creates a new conditional statement
**Answer:** C
---
**10. When using “set movenew = true” in ProVerif, what is the result?**
A) It disables the analysis of fresh names
B) It yields the most precise analysis
C) It makes all names public
D) It reduces the number of function symbols
**Answer:** B
---