# topic：Theoretical foundation of ProVerif's formal description language (applied pi-calculus).

---
**1. What is the input language of ProVerif a dialect of?**
A) The pi calculus
B) The applied pi calculus
C) The lambda calculus
D) The calculus of constructions
**Answer:** B
---
**2. How is the applied pi calculus related to the pi calculus?**
A) It is a subset of the pi calculus.
B) It is an extension of the pi calculus with function symbols defined by an equational theory.
C) It has no relation to the pi calculus.
D) It is a completely different calculus with no similarities to the pi calculus.
**Answer:** B
---
**3. What is one of the differences between ProVerif and the applied pi calculus?**
A) ProVerif supports all equational theories while the applied pi calculus does not.
B) ProVerif uses destructors in addition to the equational theories of the applied pi calculus, but does not support all equational theories.
C) The applied pi calculus uses destructors and ProVerif does not.
D) There are no differences between them.
**Answer:** B
---
**4. What does ProVerif take as input regarding the protocol?**
A) A model of the protocol in the pi calculus without any extensions.
B) A model of the protocol in an extension of the pi calculus with cryptography.
C) A model of the protocol in the lambda calculus.
D) A model of the protocol in natural language description.
**Answer:** B
---
**5. Which of the following security properties can ProVerif verify?**
A) Only secrecy
B) Secrecy, authentication, and some observational equivalence properties
C) Only authentication
D) No security properties can be verified by ProVerif.
**Answer:** B
---
**6. In the context of ProVerif and the applied pi calculus, if ProVerif processes are equivalent in a certain sense, what can be said about the corresponding applied pi calculus processes?**
A) They are not related in terms of equivalence.
B) The corresponding applied pi calculus processes are observationally equivalent.
C) The applied pi calculus processes are always non - equivalent.
D) The equivalence of ProVerif processes has no bearing on the applied pi calculus processes.
**Answer:** B
---
**7. What is the significance of the destructors in ProVerif compared to the applied pi calculus?**
A) Destructors are used in the applied pi calculus but not in ProVerif.
B) ProVerif uses destructors instead of the equational theories of the applied pi calculus.
C) Destructors are just an optional feature in ProVerif with no real difference from the applied pi calculus.
D) Destructors make ProVerif less powerful than the applied pi calculus.
**Answer:** B
---
**8. What is the role of the automatic translator in the structure of ProVerif?**
A) It translates natural language descriptions of protocols into ProVerif code.
B) It is not part of the ProVerif structure.
C) It is involved in the process of dealing with Horn clauses and derivability queries.
D) It translates the protocol model and security properties into a form suitable for ProVerif's internal processing.
**Answer:** D
---
**9. What kind of functions do both ProVerif's calculus and the applied pi calculus extend the pi calculus with?**
A) Only linear functions on terms.
B) (Fairly arbitrary) functions on terms.
C) Only polynomial functions on terms.
D) Only constant functions on terms.
**Answer:** B
---
**10. What do substitutions in ProVerif's protocol specification language always map?**
A) Names to expressions.
B) Variables (not names) to terms.
C) Variables to fail or may - fail variables.
D) Names to terms.
**Answer:** B
---