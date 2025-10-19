# topic：Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes).

Here are 10 multiple-choice questions designed to test students' understanding of the topic "Scope and Uniqueness Constraints: Mandatory declaration-before-use, Scope determination rules, Identifier uniqueness (variables/functions/processes)."  

---

**1. In the given formalism, what must be done before using a variable or a name in a process declaration?**  
A) It can be used without prior declaration.  
B) It must be declared with its type before use.  
C) It must be declared only if used in a conditional statement.  
D) Declaration is optional for free names.  
**Answer:** B  

---

**2. What is the scope of a name declared as `new a:nonce` in the process `new a:nonce; out(c, a)`?**  
A) The scope is limited to the `out(c, a)` command.  
B) The scope extends to the entire process block.  
C) The scope is global and persists beyond the process.  
D) The scope depends on the enclosing conditional statement.  
**Answer:** B  

---

**3. How is a name represented if it is declared inside the scope of variables, e.g., `in(c, (x, y)); new b:nonce`?**  
A) As `b[]` since variables do not affect naming.  
B) As `b[x=M, y=N]` where M, N are runtime values of x, y.  
C) As `b` without any arguments.  
D) As `b[x, y]` without substitution.  
**Answer:** B  

---

**4. What happens if a variable is not universally quantified in a clause containing variables?**  
A) The clause is invalid and rejected.  
B) The clause is treated as if variables are existentially quantified.  
C) The clause is allowed only if no variables are used.  
D) The variables are automatically assigned the `fail` type.  
**Answer:** A  

---

**5. Which of the following ensures identifier uniqueness in declarations?**  
A) All identifiers must have distinct names, regardless of type.  
B) Variables and names can share identifiers if their types differ.  
C) Identifiers must be unique only within the same category (e.g., two variables cannot share a name).  
D) Identifiers must be unique only if used in the same process.  
**Answer:** C  

---

**6. What is the consequence of omitting `else 0` in nested `if-then-else` constructs?**  
A) The `else` clause is automatically attached to the outer `if`.  
B) The `else` clause is automatically attached to the inner `if`.  
C) The process becomes syntactically invalid.  
D) The ambiguity must be resolved by explicit parentheses.  
**Answer:** D  

---

**7. In the clause `forall x1:t1, ..., xn:tn; F1, ..., Fm -> F`, when can the universal quantification part be omitted?**  
A) If at least one variable is present in F1, ..., Fm, F.  
B) If no variables are present in F1, ..., Fm, F.  
C) If the types t1, ..., tn include the `fail` type.  
D) If the clause is used only once in the process.  
**Answer:** B  

---

**8. Why is distinct naming of variables and names recommended?**  
A) To allow variables and names to be used interchangeably.  
B) To avoid confusion and ensure clarity in process definitions.  
C) Because ProVerif requires names to be longer than variables.  
D) Because variables cannot be substituted if names overlap.  
**Answer:** B  

---

**9. What is the significance of the `[precise]` annotation for an input?**  
A) It enforces exact matching of input values.  
B) It ensures the input is processed only once.  
C) It tells ProVerif to generate more precise axioms for the input.  
D) It restricts the input to non-variable types.  
**Answer:** C  

---

**10. Which of the following is true about function symbol declarations?**  
A) Destructors can only be declared after constructors.  
B) Function symbols must be declared with their types before use.  
C) Function symbols can be used without declaration if they are infix operators.  
D) Only constructors require type declarations.  
**Answer:** B  

---

Each question tests a distinct aspect of scope, declaration rules, or uniqueness constraints, with plausible distractors and clear answers.