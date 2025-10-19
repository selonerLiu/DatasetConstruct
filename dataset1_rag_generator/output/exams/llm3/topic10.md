# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

Here are 10 multiple-choice questions designed to test students' understanding of the given topic on expressions and terms in the ProVerif formalism:

---

**1. What is a ground term in the given formalism?**  
A) A term that contains at least one variable.  
B) A term that contains no variables.  
C) A term that includes the constant `fail`.  
D) A term that is always a constructor application.  
**Answer:** B  

---

**2. Which of the following is a valid value in the evaluation relation `D ⇓ V`?**  
A) A term containing variables.  
B) A non-ground destructor application.  
C) A ground term or `fail`.  
D) A process with a restriction.  
**Answer:** C  

---

**3. How is the expression `let y = D in in(y, x: T); P` represented in the core calculus?**  
A) As a direct input process without transformation.  
B) As an expression evaluation moved into the process syntax.  
C) As a restriction on the variable `y`.  
D) As a conditional statement.  
**Answer:** B  

---

**4. What does the evaluation of a destructor `g(D₁, ..., Dₙ)` result in if no rewrite rule applies?**  
A) The first rule in `def(g)` is forced to apply.  
B) It evaluates to the last term in `def(g)`.  
C) It evaluates to the constant `fail`.  
D) It loops indefinitely until a rule matches.  
**Answer:** C  

---

**5. Which of the following constructs is allowed in ProVerif expressions but not in core processes?**  
A) Replication (`!P`).  
B) Restriction (`new a: T; D`).  
C) Parallel composition (`P | Q`).  
D) Event (`event(ev); P`).  
**Answer:** B  

---

**6. What is the purpose of the `else` branch in `let x: T = D in D′ else D′′`?**  
A) To handle the case where `D` evaluates to `fail`.  
B) To introduce a new name bound to `x`.  
C) To enforce type checking on `D′`.  
D) To parallelize the evaluation of `D′` and `D′′`.  
**Answer:** A  

---

**7. Which of the following is NOT a valid component of a may-fail term in destructor rules?**  
A) A term `M`.  
B) The constant `fail`.  
C) A may-fail variable `u`.  
D) A process identifier `P`.  
**Answer:** D  

---

**8. How is the term `if M then N else N′` evaluated if `M` fails?**  
A) It evaluates to `N`.  
B) It evaluates to `N′`.  
C) It evaluates to `fail`.  
D) It raises a runtime error.  
**Answer:** C  

---

**9. In the enriched syntax, what can replace occurrences of terms `M` in processes?**  
A) Only ground terms.  
B) Only destructor applications.  
C) Expressions `D` (which may include destructors).  
D) Event constructions.  
**Answer:** C  

---

**10. Which operator has the highest precedence in the given grammar of terms?**  
A) `||` (logical OR).  
B) `&&` (logical AND).  
C) `=` (equality).  
D) `+` (addition).  
**Answer:** D  

--- 

These questions cover key concepts like ground terms, evaluation semantics, destructors, expression syntax, and precedence rules while avoiding redundancy. The distractors are plausible and the answers are clearly indicated.