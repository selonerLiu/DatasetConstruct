# topic：Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes).

Here are 10 multiple-choice questions to test students' understanding of the topic:
---
**1. What is the purpose of the `forall` quantifier in a process declaration?**

A) To specify the type of a variable
B) To universally quantify variables over a specific type
C) To declare a new name
D) To define a function symbol

**Answer:** B
---
**2. How are names and variables declared in the given formalism?**

A) Names and variables are declared with their types using the `type` keyword
B) Names and variables are declared with their types using the `free` keyword
C) Names and variables are declared with their types using the `forall` quantifier
D) Names and variables do not need to be declared

**Answer:** B
---
**3. What is the scope of a variable or name in a process declaration?**

A) It is determined by the position of the variable or name in the process
B) It is determined by the `forall` quantifier
C) It is determined by the type of the variable or name
D) It is determined by the keyword `process`

**Answer:** B
---
**4. What is the purpose of annotating restrictions with variables in the internal representation of fresh names?**

A) To avoid false attacks due to names with different arguments
B) To improve the performance of the verification phase
C) To reduce the number of clauses in the process
D) To increase the scope of variables

**Answer:** A
---
**5. How are function symbols declared in the given formalism?**

A) Using the `type` keyword
B) Using the `free` keyword
C) Using the `forall` quantifier
D) With their types, e.g., `h(T1,...,Tn) : T`

**Answer:** D
---
**6. What is the convention for omitting `else 0` in the if-then-else construct?**

A) It is always omitted
B) It is never omitted
C) It is omitted only in certain contexts
D) It is not clear which `if` the `else` applies to

**Answer:** D
---
**7. What is the purpose of the `precise` annotation in input declarations?**

A) To specify the type of the input
B) To indicate that the input should be taken into account as precisely as possible
C) To declare a new name
D) To define a function symbol

**Answer:** B
---
**8. How are free names declared in the given formalism?**

A) Using the `type` keyword
B) Using the `free` keyword
C) Using the `forall` quantifier
D) Using the `process` keyword

**Answer:** B
---
**9. What is the purpose of the `maxSubset` declaration?**

A) To specify the type of a variable
B) To declare a new name
C) To define a function symbol
D) To specify the lemma declaration

**Answer:** D
---
**10. What is the requirement for identifiers in the given formalism?**

A) They must be unique within a process
B) They must be declared before use
C) They must be declared with their types
D) They can be used without prior declaration

**Answer:** B
---