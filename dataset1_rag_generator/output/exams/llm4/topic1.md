# topic：Theoretical foundation of ProVerif's formal description language (applied pi-calculus).

---

**1. Which of the following best describes the theoretical foundation of ProVerif’s formal description language?**  
A) It is based on a minimal extension of propositional logic.  
B) It is based on the applied pi calculus with function symbols defined by equational theories.  
C) It uses a variant of lambda calculus extended with concurrency features.  
D) It is grounded in first-order predicate logic with temporal operators.  
**Answer:** B

---

**2. What is one key difference between ProVerif and the standard applied pi calculus regarding handling equations?**  
A) ProVerif supports all equational theories without restriction.  
B) The applied pi calculus uses destructors instead of equational theories.  
C) ProVerif uses destructors rather than supporting all equational theories.  
D) There are no differences in how equations are handled.  
**Answer:** C

---

**3. What feature does ProVerif include that is not present in the original applied pi calculus?**  
A) Support for multithreaded processes  
B) Built-in error-handling constructs such as else branches  
C) Support for higher-order functions  
D) Use of equational theories to define cryptographic primitives  
**Answer:** B

---

**4. In what way is observational equivalence related to the correspondence between ProVerif and the applied pi calculus?**  
A) If two ProVerif processes are observationally equivalent, then their applied pi calculus counterparts cannot be equivalent.  
B) Observational equivalence in ProVerif implies observational equivalence in the applied pi calculus.  
C) ProVerif only proves secrecy properties, not observational equivalences.  
D) Observational equivalence is irrelevant to ProVerif’s verification process.  
**Answer:** B

---

**5. What kind of security properties can ProVerif verify, in addition to secrecy and authentication?**  
A) Only performance-related properties  
B) Type safety and memory correctness  
C) Observational equivalence properties  
D) Termination and liveness properties only  
**Answer:** C

---

**6. What is the role of substitutions in ProVerif's calculus?**  
A) They map names to expressions exclusively.  
B) They map variables (not names) to terms or expressions.  
C) They are used to replace function symbols with equational rules.  
D) They are used to simulate network failures in protocol models.  
**Answer:** B

---

**7. Which of the following is **not** a part of the core structure of ProVerif as illustrated in its architecture?**  
A) Protocol specification using an extension of the pi calculus  
B) Automatic translation into Horn clauses  
C) Manual proof construction using natural deduction  
D) Resolution engine with selection function  
**Answer:** C

---

**8. Why is diff-equivalence considered stronger than observational equivalence when comparing processes in ProVerif and the applied pi calculus?**  
A) Because it allows for more context changes during execution  
B) Because it requires processes to be identical in all contexts  
C) Because it is easier to prove using equational theories  
D) Because it only applies to deterministic processes  
**Answer:** B

---

**9. How does ProVerif model cryptographic primitives within its formalism?**  
A) Through type annotations and static typing rules  
B) Using built-in constants only, without user-defined operations  
C) By means of rewrite rules or equational theories  
D) By simulating them with probabilistic Turing machines  
**Answer:** C

---

**10. Which of the following statements about the relationship between ProVerif and the applied pi calculus is correct?**  
A) ProVerif can be encoded into the applied pi calculus to prove equivalence.  
B) The applied pi calculus is a strict superset of ProVerif's calculus.  
C) ProVerif and the applied pi calculus are completely incompatible.  
D) ProVerif provides a less expressive formalism than the applied pi calculus.  
**Answer:** A

---