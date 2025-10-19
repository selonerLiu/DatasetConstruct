# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

---
**1. What is the definition of a ground term in the context of expressions?**
A) A term that contains variables.
B) A term that contains no variable.
C) A term that is always equal to fail.
D) A term that represents a computation failure.
**Answer:** B
---

---
**2. In ProVerif, what does the evaluation relation D⇓V signify?**
A) The ground expression D evaluates to the value V.
B) The value V evaluates to the ground expression D.
C) The process D evaluates to the value V.
D) The value V evaluates to the process D.
**Answer:** A
---

---
**3. Which of the following is an example of a term that can be evaluated using the core calculus?**
A) A variable.
B) A function call.
C) A tuple construction.
D) All of the above.
**Answer:** D
---

---
**4. What is the purpose of introducing additional expression evaluations in ProVerif?**
A) To simplify the syntax of expressions.
B) To allow expressions to contain constructs from processes.
C) To restrict the use of variables in expressions.
D) To prevent the evaluation of expressions.
**Answer:** B
---

---
**5. In the syntax of processes, what does the construct 'out(D,D′); P' represent?**
A) An input operation with pattern matching.
B) An output operation with two expressions.
C) A conditional operation with two expressions.
D) A parallel composition of processes.
**Answer:** B
---

---
**6. What is the role of the 'fail' constant in expressions?**
A) It represents a successful computation.
B) It represents the failure of a computation.
C) It is used to indicate a variable.
D) It is used to represent a ground term.
**Answer:** B
---

---
**7. In ProVerif, which of the following is not allowed in 'reduc' and 'equation' declarations?**
A) Constructors.
B) Infix symbols.
C) The 'fail' constant.
D) Names as function symbols.
**Answer:** D
---

---
**8. What is the term 'new a: T; M' used for in ProVerif?**
A) To declare a new variable 'a' of type 'T'.
B) To construct a new tuple of type 'T'.
C) To create a new name 'a' of type 'T' and evaluate the term 'M'.
D) To assign the value of 'M' to the variable 'a'.
**Answer:** C
---

---
**9. What is the syntax for pattern-matching in input and expression evaluation constructs?**
A) in(D,pat); P
B) let pat = D in P else Q
C) Both A and B
D) Neither A nor B
**Answer:** C
---

---
**10. What is the precedence order for infix symbols in the ProVerif core language?**
A) =, <>, <=, >=, <, >, +, -
B) ||, &&, =, <>, <=, >=, <, >, +, -
C) +, -, =, <>, <=, >=, <, >, ||, &&
D) Both A and B
**Answer:** B
---