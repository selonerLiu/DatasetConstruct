# topic：Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes).

---
**1. In the given content, what is the requirement for using variables F1, ..., Fm, F in clauses?**
A) They can be used without any quantification.
B) They must be universally quantified by forall x1 : t1, ..., xn : tn.
C) They only need to be quantified if they are used in a conditional clause.
D) Quantification is optional for these variables.
**Answer:** B
---
**2. When F1, ..., Fm, F contain no variables, what can be omitted in the quantification part?**
A) The entire clause.
B) The part forall x1 : t1, ..., xn : tn.
C) Only the type identifiers t1, ..., tn.
D) Nothing can be omitted.
**Answer:** B
---
**3. In forall x1 : t1, ..., xn : tn, what can the types t1, ..., tn be?**
A) Only a type identifier.
B) Only of the form t or fail.
C) Either a type identifier or of the form t or fail.
D) They must be primitive data types.
**Answer:** C
---
**4. Consider the process new a:nonce. Where is the name a in terms of variable scope?**
A) It is in the scope of all variables in the process.
B) It is not in the scope of any variables and is modeled as a[ ].
C) It is in the scope of some default variables.
D) Its scope is determined by the next process step.
**Answer:** B
---
**5. In the process in(c,(x: bitstring ,y: bitstring )); new b:nonce, how is the name b represented?**
A) As b[ ] because it is a new name.
B) As b[x= M,y=N] where M, N are the values of x and y at run - time.
C) As b[x, y] without considering their values.
D) As b[c] because c is the input channel.
**Answer:** B
---
**6. What is the purpose of annotating restrictions with variables in the internal representation of fresh names?**
A) To make the code look more organized.
B) To avoid false attacks in the proof of equivalences by ensuring matching names have the same arguments.
C) To increase the execution speed of the process.
D) To simplify the variable substitution process.
**Answer:** B
---
**7. Why is distinct naming of names and variables recommended?**
A) To make the code more concise.
B) To avoid confusion, especially for new users.
C) To follow a coding standard.
D) To reduce the memory usage of the program.
**Answer:** B
---
**8. What is the ambiguity in the expression if M = M′ then if N = N′ then P else Q?**
A) It is not clear which if the else applies to.
B) The comparison operators are not standard.
C) The variables M, M′, N, N′ are not properly declared.
D) The process P and Q are not well - defined.
**Answer:** A
---
**9. What can be done to tell ProVerif to take an input into account as precisely as possible?**
A) Add a comment in the code.
B) Annotate the input with [precise].
C) Use a specific keyword before the input.
D) Define the input in a separate file.
**Answer:** B
---
**10. In the set - to - clause resolution algorithm, how are existing clauses stored?**
A) In a simple list.
B) In a tree indexed by the function symbols of the selected fact, starting from the root.
C) In a hash table with variable names as keys.
D) In a stack data structure.
**Answer:** B
---