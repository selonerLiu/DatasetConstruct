# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

Here are 10 multiple-choice questions designed to assess students' understanding of **Expressions (Terms): Composition of operators/operands into evaluable units**, including function applications and tuple constructions, based on the provided content.

---

**1. In the context of ProVerif expressions, what does the symbol `fail` represent?**  
A) A successful computation that returns a boolean value.  
B) A special constant indicating that a computation has failed.  
C) A variable that can be assigned any term during evaluation.  
D) An operator used for conditional branching in expressions.  
**Answer:** B

---

**2. Which of the following best describes a "ground" expression in this formalism?**  
A) An expression that includes at least one variable.  
B) An expression that evaluates only to a constructor function.  
C) An expression that contains no variables and is fully evaluated.  
D) An expression that must be wrapped in a conditional statement.  
**Answer:** C

---

**3. What distinguishes destructors from constructors in the syntax of expressions?**  
A) Destructors always return new names, while constructors do not.  
B) Constructors build data structures, while destructors break them down or extract values.  
C) Destructors are only used in conditional statements, unlike constructors.  
D) Constructors can fail during evaluation, but destructors cannot.  
**Answer:** B

---

**4. Which of the following is a valid form of an enriched term in ProVerif?**  
A) `new x; if x then fail else y`  
B) `f(new a; g(a), h(x))`  
C) `tupleT1,T2(fail, x)`  
D) All of the above  
**Answer:** D

---

**5. In the expression `let x = D in P else Q`, what happens if the evaluation of `D` results in `fail`?**  
A) The process `P` is executed.  
B) The process `Q` is executed.  
C) The entire expression is ignored.  
D) A runtime error is raised.  
**Answer:** B

---

**6. What is the purpose of rewrite rules like `g(U1,...,Un) → U` in defining destructors?**  
A) To define how to create new names during execution.  
B) To specify how a destructor processes input terms and produces output.  
C) To restrict the use of conditionals within expressions.  
D) To ensure all expressions evaluate to `fail`.  
**Answer:** B

---

**7. Which of the following represents a correctly formed tuple constructor according to the formalism?**  
A) `tupleT1,...,Tn(M1,...,Mn)` where each `Mi` is a name  
B) `tupleT1,...,Tn(fail, x)`  
C) `tupleT1,...,Tn(true, false, 5)`  
D) All of the above  
**Answer:** D

---

**8. How is the evaluation of a ground expression `D` defined in this formalism?**  
A) By reducing it to another expression using type inference.  
B) By rewriting it repeatedly until it evaluates to a value `V`.  
C) By checking its syntactic structure without executing it.  
D) By comparing it directly to a known set of constants.  
**Answer:** B

---

**9. In the context of expressions, what role do destructors play when evaluating terms?**  
A) They are used exclusively to declare new names.  
B) They allow processes to manipulate terms by extracting or transforming components.  
C) They enforce that all expressions must terminate successfully.  
D) They prevent the use of tuples in cryptographic operations.  
**Answer:** B

---

**10. Which of the following is **not** allowed inside `reduc` or `equation` declarations in ProVerif?**  
A) Constructor function symbols  
B) Destructor function symbols  
C) Logical operators such as `&&`, `||`, and `not`  
D) Variables bound by `let` expressions  
**Answer:** C

---