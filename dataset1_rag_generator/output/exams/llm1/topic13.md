# topic：Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes).

---
**1. In the given formalism, what is mandatory before using any variable or name in a process declaration?**  
A) It can be used without prior declaration.  
B) It must be declared with its type before use.  
C) It must be declared only if used inside a function.  
D) Declaration is only required for constructors.  
**Answer:** B  
---

**2. How are variables of formulas such as F1, ..., Fm, and F quantified in the clauses?**  
A) Existentially quantified by exists x1 : t1, ..., xn : tn.  
B) Universally quantified by forall x1 : t1, ..., xn : tn.  
C) Quantification is optional depending on the variable type.  
D) Variables are left unquantified for flexibility.  
**Answer:** B  
---

**3. What happens when formulas F1, ..., Fm, and F do not contain any variables?**  
A) The quantifiers forall x1 : t1, ..., xn : tn must still be included.  
B) The quantifiers can be omitted.  
C) Variables must be introduced artificially.  
D) The formula becomes invalid without variables.  
**Answer:** B  
---

**4. In the declaration `new a:nonce`, what is the scope of the name `a`?**  
A) It is in the scope of variables declared previously.  
B) It is not in the scope of any variables and modeled without arguments.  
C) It inherits the scope of the process it is declared in.  
D) It is globally scoped across all processes.  
**Answer:** B  
---

**5. Given a process snippet `in(c, (x: bitstring, y: bitstring)); new b:nonce`, how is the name `b` represented?**  
A) As `b[]` without arguments since it is fresh.  
B) As `b[x= M, y = N]` representing variables x and y in scope.  
C) As a global name without any bindings.  
D) As `b[x, y]` where x and y are just placeholders.  
**Answer:** B  
---

**6. What is the role of constructors and destructors in the given formalism?**  
A) They represent variable declarations only.  
B) They are function symbols used for creating and analyzing data terms.  
C) They are reserved keywords that cannot be redefined.  
D) They denote only input/output channels.  
**Answer:** B  
---

**7. Why is it recommended to distinctly name names and variables when modeling processes?**  
A) To reduce the size of the code only.  
B) To avoid confusion and false attacks due to argument mismatches in biprocesses.  
C) Because the language syntax requires it.  
D) To improve performance during code execution.  
**Answer:** B  
---

**8. What does the special type declaration `t or fail` imply for a variable?**  
A) The variable can never take the value `fail`.  
B) The variable is only allowed to take the value `fail`.  
C) The variable may take either a value of type `t` or the special value `fail`.  
D) The variable is untyped and can take any value.  
**Answer:** C  
---

**9. Which of the following best describes the scope of session identifiers in the internal representation of fresh names?**  
A) Session identifiers are optional and can be omitted safely.  
B) Session identifiers are always present and sufficient for soundness.  
C) Session identifiers must be manually added by users.  
D) Session identifiers represent variables to be substituted.  
**Answer:** B  
---

**10. What is the consequence of omitting `else 0` in nested if-then-else constructs, according to the content?**  
A) It clarifies the conditional branching.  
B) It may create ambiguity about which `if` the `else` applies to.  
C) The program will throw an error during parsing.  
D) It is a recommended style to write concise code.  
**Answer:** B  
---