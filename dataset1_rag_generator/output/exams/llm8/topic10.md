# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

Here are 10 multiple-choice questions to test students' understanding of the topic:
---
**1. What is the purpose of the evaluation relation D⇓V in the given formalism?**

A) To define the syntax of expressions
B) To specify the semantics of expressions
C) To declare new names
D) To evaluate the type of a term

**Answer:** B
---
**2. Which of the following is a type of value in the given formalism?**

A) A term with variables
B) A ground term or fail
C) A process with a conditional statement
D) A function application

**Answer:** B
---
**3. What is the result of evaluating a conditional statement if M then N else N′ when M fails?**

A) N
B) N′
C) fail
D) The evaluation loops indefinitely

**Answer:** C
---
**4. How are expressions evaluated in the given formalism?**

A) By rewriting them until a value is obtained
B) By applying a set of predefined rules
C) By using a recursive function
D) By evaluating the type of the expression

**Answer:** A
---
**5. What is the purpose of the let x: T = D in P else Q construct?**

A) To declare a new name
B) To evaluate an expression and bind the result to x
C) To specify a conditional statement
D) To define a new function

**Answer:** B
---
**6. Which of the following is an example of a destructor?**

A) A function application
B) A tuple construction
C) A conditional statement
D) A restriction

**Answer:** A
---
**7. What is the type of the tuple constructor tupleT1,...,Tn?**

A) bitstring
B) term
C) expression
D) process

**Answer:** A
---
**8. How are processes that contain expressions with conditionals and expression evaluations handled?**

A) They are transformed into processes without such expressions
B) They are evaluated directly
C) They are rejected by the formalism
D) They are rewritten using a set of predefined rules

**Answer:** A
---
**9. What is the purpose of the new a: T; P construct?**

A) To declare a new name a of type T
B) To evaluate an expression
C) To specify a conditional statement
D) To define a new function

**Answer:** A
---
**10. What happens when no rewrite rule applies during the evaluation of g(D1,...,Dn)?**

A) The evaluation succeeds with a default value
B) The evaluation fails and evaluates to the constant fail
C) The evaluation loops indefinitely
D) The evaluation is undefined

**Answer:** B
---