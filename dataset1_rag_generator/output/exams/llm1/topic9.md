# topic：Declaration of Functions and Destructors: Definition methods，Roles in the system, Introduction mechanisms.

---
**1. In the formalism described, what do the identifiers a, b, c, and k mainly represent?**  
A) Variables that can be substituted by terms.  
B) Function symbols for constructors and destructors.  
C) Names representing atomic data such as keys and nonces.  
D) Types declared by the user.  
**Answer:** C

---
**2. Which of the following best describes the role of variables like x, y, and z in the system?**  
A) They are atomic data elements that cannot be changed.  
B) They can be substituted by terms during process execution.  
C) They represent constant values with fixed types.  
D) They must always be free names declared at the start.  
**Answer:** B

---
**3. How are user-defined types declared in the system?**  
A) `type t.`  
B) `free t: var.`  
C) `fun t() : type.`  
D) `const t : var.`  
**Answer:** A

---
**4. What is the correct syntax to declare free names appearing in an input file?**  
A) `var n : t .`  
B) `free n : t .`  
C) `const n : t .`  
D) `fun n() : t .`  
**Answer:** B

---
**5. Which term best describes the purpose of constructors in this formalism?**  
A) Functions that manipulate terms only as constants.  
B) Functions that combine terms into more complex terms.  
C) Operators that only appear in expressions to manipulate variables.  
D) Rewrite rules used for destructors to modify terms.  
**Answer:** B

---
**6. Destructors are defined by which of the following mechanisms in this system?**  
A) Declaration of new variables and types.  
B) Application of constructor functions to terms.  
C) An ordered list of rewrite rules of the form `g(U₁,...,Uₙ) → U`.  
D) Assigning constant values to names and variables.  
**Answer:** C

---
**7. What happens if a destructor function symbol's rewrite rules fail to match a term?**  
A) The term is left unchanged.  
B) The destructor returns the constant `fail`.  
C) The process aborts immediately without output.  
D) The first rewrite rule is reapplied indefinitely.  
**Answer:** B

---
**8. How does the formalism model constants within the declaration framework?**  
A) As functions with no arguments (arity 0), e.g., `fun c() : t.`  
B) As variables declared without type annotations.  
C) Using the `free c : var.` syntax.  
D) As destructors applied to empty terms.  
**Answer:** A

---
**9. Which of the following correctly describes the difference between built-in and user-defined destructors?**  
A) Built-in destructors are declared with `fun` only, user-defined with `type`.  
B) User-defined destructors use rewrite rules, built-in have fixed semantic behavior (e.g. not, &&).  
C) Built-in destructors can only return constants, user-defined always return terms.  
D) There is no distinction; all destructors are declared similarly.  
**Answer:** B

---
**10. Why can't modular exponentiation operations be directly represented using destructor rewrite rules in this formalism?**  
A) Because rewrite rules can only represent boolean operations.  
B) Because some operations require equations beyond simple rewrite rules.  
C) Because variables cannot be substituted by modular expressions.  
D) Because constructors cannot accept modular exponents as arguments.  
**Answer:** B

---