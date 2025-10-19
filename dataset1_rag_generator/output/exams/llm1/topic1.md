# topic：Theoretical foundation of ProVerif's formal description language (applied pi-calculus).

---
**1. What is the input language of ProVerif primarily based on?**  
A) The original pi calculus by Milner  
B) The applied pi calculus introduced by Abadi and Fournet (2001) and updated in 2016  
C) The spi calculus by Abadi and Gordon  
D) The λ-calculus with cryptographic extensions  
**Answer:** B  

---
**2. How does the applied pi calculus extend the original pi calculus?**  
A) By introducing probabilistic computation  
B) By allowing function symbols defined by an equational theory  
C) By removing concurrency constructs  
D) By replacing messages with integers only  
**Answer:** B  

---
**3. Which feature is used by ProVerif that differs from the equational theories in the applied pi calculus?**  
A) ProVerif uses only equality checks  
B) ProVerif uses destructors in addition to equational theories  
C) ProVerif removes all destructors for simplification  
D) ProVerif uses probabilistic encryption exclusively  
**Answer:** B  

---
**4. What is ProVerif’s built-in construct that is not present in the applied pi calculus?**  
A) A repeat loop construct  
B) Error-handling through the else branch of expression evaluation  
C) Non-deterministic choice operators  
D) Higher-order functions support  
**Answer:** B  

---
**5. What types of security properties can ProVerif verify?**  
A) Only secrecy properties  
B) Only authentication properties  
C) Secrecy, authentication (correspondences), and some observational equivalence properties  
D) Only observational equivalence properties  
**Answer:** C  

---
**6. What kind of mathematical objects model cryptographic primitives in ProVerif?**  
A) Probabilistic automata  
B) Automata with states only  
C) Rewrite rules or equations  
D) Simple term algebras without functions  
**Answer:** C  

---
**7. How is the ProVerif input language related to the applied pi calculus?**  
A) It is a completely unrelated language specialized for cryptography  
B) It is a minimal core extension of the applied pi calculus language  
C) It is only superficially similar but semantically different  
D) It restricts the applied pi calculus to only names, not variables  
**Answer:** B  

---
**8. What is the importance of 'differential equivalence' (diff-equivalence) in ProVerif compared to observational equivalence?**  
A) Diff-equivalence is a weaker condition than observational equivalence  
B) ProVerif proves diff-equivalence, which is stronger than observational equivalence  
C) Neither diff-equivalence nor observational equivalence is supported by ProVerif  
D) Diff-equivalence and observational equivalence are equivalent notions in ProVerif  
**Answer:** B  

---
**9. In the context of substitutions in ProVerif, what do substitutions map?**  
A) Variables and names to constants only  
B) Variables (but not names) to terms or expressions  
C) Names only to processes  
D) Neither variables nor names are substituted  
**Answer:** B  

---
**10. What underlying formal method tool does ProVerif use to resolve derivability queries?**  
A) Model checking with BDDs  
B) Resolution with selection on Horn clauses  
C) SAT solving over propositional formulas  
D) Linear programming  
**Answer:** B  

---