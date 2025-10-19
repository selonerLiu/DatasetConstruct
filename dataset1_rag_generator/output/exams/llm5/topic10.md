# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

Here are 10 multiple-choice questions based on the provided content:
---

**1. What is the purpose of the evaluation relation D⇓V in the given formalism?**
A) To define the syntax of expressions
B) To specify the semantics of expressions by evaluating them to values
C) To declare variables and names
D) To define the structure of processes

**Answer:** B
---

**2. What is a value V in the given formalism?**
A) A term containing variables
B) A ground term or the constant fail
C) A process declaration
D) A conditional statement

**Answer:** B
---

**3. How is a ground expression D evaluated in the given formalism?**
A) By rewriting it until a value V is obtained
B) By declaring its variables and names
C) By applying constructors and destructors
D) By using it in a process declaration

**Answer:** A
---

**4. What is the purpose of the let x: T = D in D′else D′′ expression evaluation construct?**
A) To declare a variable x of type T
B) To evaluate an expression D and assign its value to x
C) To specify a conditional statement
D) To define a function application

**Answer:** B
---

**5. What is the difference between a constructor and a destructor in the given formalism?**
A) A constructor is used to define a function application, while a destructor is used to define a process declaration
B) A constructor is used to build data structures, while a destructor is used to manipulate terms in expressions
C) A constructor is used to declare variables, while a destructor is used to declare names
D) A constructor is used to specify a conditional statement, while a destructor is used to specify a loop

**Answer:** B
---

**6. How is a term if M then N else N′ evaluated in the given formalism?**
A) It is evaluated to N if M is equal to true, and to N′ otherwise
B) It is evaluated to N if M is not equal to true, and to N′ otherwise
C) It is evaluated to fail if M fails, or if the else branch is omitted and M is not equal to true
D) It is evaluated to true if M is equal to true, and to false otherwise

**Answer:** C
---

**7. What is the purpose of the new a: T; M construct in the given formalism?**
A) To declare a variable a of type T
B) To construct a new name a of type T and evaluate the enriched term M
C) To specify a conditional statement
D) To define a function application

**Answer:** B
---

**8. What is the result of evaluating an expression g(D1,...,Dn) if no rewrite rule applies?**
A) The expression is evaluated to a value V
B) The expression is evaluated to the constant fail
C) The expression is evaluated to a constructor application
D) The expression is evaluated to a destructor application

**Answer:** B
---

**9. How are constructors and destructors used in the given formalism?**
A) To represent data structures and cryptographic operations
B) To declare variables and names
C) To specify conditional statements
D) To define function applications

**Answer:** A
---

**10. What is the purpose of the pattern-matching construct in(D,pat); P in the given formalism?**
A) To declare a variable pat of type T
B) To evaluate an expression D and assign its value to pat
C) To specify a conditional statement
D) To enrich the input and expression evaluation constructs with pattern-matching

**Answer:** D
---
