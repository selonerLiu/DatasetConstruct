# topic：Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes).

Here are 10 multiple-choice questions based on the topic **"Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes)"**, designed to test student understanding of the provided content.

---

**1. In the given formalism, what must be done before using a variable or a name in a process declaration?**  
A) It can be used without prior declaration.  
B) It must be declared with its type before use.  
C) It must be declared only if used in a conditional statement.  
D) Declaration is optional for free names.  

**Answer:** B

---

**2. According to the scope determination rules, when is a name modeled without arguments?**  
A) When it appears inside an `if-then-else` construct.  
B) When it is part of a function definition.  
C) When it is not in the scope of any variables.  
D) When it is globally quantified.  

**Answer:** C

---

**3. What does it mean when a variable is said to be "in the scope" of another variable?**  
A) It is defined after the other variable in the code.  
B) Its value depends on the value of the other variable at runtime.  
C) It has the same name as the other variable.  
D) It is always declared globally.  

**Answer:** B

---

**4. Why might a restriction need to be annotated with variables?**  
A) To allow substitution of constructors.  
B) To indicate which variables influence the internal representation of fresh names.  
C) To optimize the compilation process.  
D) To simplify the syntax of the language.  

**Answer:** B

---

**5. Which of the following best describes identifier uniqueness in this formalism?**  
A) Names and variables can share the same identifier freely.  
B) All identifiers must be globally unique across the entire system.  
C) Distinct naming of names and variables is recommended to avoid confusion.  
D) Identifiers can be reused in different scopes without conflict.  

**Answer:** C

---

**6. In what situation can the `forall x1 : t1, ..., xn : tn;` prefix be omitted in a clause?**  
A) When all variables are declared globally.  
B) When the clause contains no function symbols.  
C) When F1, ..., Fm, F contain no variables.  
D) When the types are inferred automatically.  

**Answer:** C

---

**7. What is the significance of annotating an input with `[precise]` in ProVerif?**  
A) It disables all optimizations during verification.  
B) It ensures that the input is interpreted exactly once.  
C) It allows the omission of else branches in conditionals.  
D) It tells ProVerif to consider the input as precisely as possible.  

**Answer:** D

---

**8. How are new names represented when they are created within the scope of variables?**  
A) As atomic values without any additional information.  
B) With a list of substitutions corresponding to the current values of the scoped variables.  
C) Using infix operators like `||` or `&&`.  
D) By defaulting to a global session identifier.  

**Answer:** B

---

**9. Which of the following is NOT allowed as an identifier in noninterference declarations?**  
A) Function symbols  
B) Predicates  
C) Names  
D) Variables  

**Answer:** C

---

**10. What kind of ambiguity can arise from omitting the `else 0` clause in conditional expressions?**  
A) Confusion about which `if` the `else` applies to.  
B) Incorrect type inference for variables.  
C) Errors in quantifier scoping.  
D) Failure to compile the process into ProVerif format.  

**Answer:** A

---