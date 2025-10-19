# topic：Theoretical foundation of ProVerif's formal description language (applied pi-calculus).

Below is a set of 10 multiple-choice questions designed to test students' understanding of the topic: "Theoretical foundation of ProVerif's formal description language (applied pi-calculus)." These questions are based on the provided content. Each question is clearly described, features plausible distractors (options that are related but incorrect based on common misconceptions or partial truths from the content), and follows the specified format. The questions are distinct from one another, covering different aspects of the topic such as relationships, extensions, differences, and features.

---

**1. What is the primary relationship between ProVerif's input language and the applied pi calculus?**  
A) ProVerif's input language is identical to the applied pi calculus without any modifications.  
B) ProVerif's input language is a dialect of the applied pi calculus, as introduced by Abadi and Fournet (2001) and updated by Abadi et al. (2016).  
C) ProVerif's input language replaces the applied pi calculus entirely with its own custom extensions.  
D) ProVerif's input language is based on the applied pi calculus but only for basic pi calculus processes, excluding cryptography.  
**Answer:** B

---

**2. How does the applied pi calculus extend the pi calculus?**  
A) It adds support for destructors and error-handling constructs only.  
B) It extends the pi calculus with function symbols defined by an equational theory.  
C) It simplifies the pi calculus by removing support for cryptographic primitives.  
D) It extends the pi calculus solely through the addition of observational equivalence properties.  
**Answer:** B

---

**3. What is one key difference between ProVerif and the applied pi calculus in terms of handling functions and equations?**  
A) ProVerif uses the same equational theories as the applied pi calculus for all functions.  
B) ProVerif uses destructors instead of the equational theories of the applied pi calculus and does not support all equational theories.  
C) ProVerif relies entirely on equational theories but adds more function symbols than the applied pi calculus.  
D) ProVerif and the applied pi calculus both use destructors, but ProVerif limits them to cryptographic contexts.  
**Answer:** B

---

**4. What does ProVerif take as input for modeling a protocol?**  
A) A basic pi calculus process without any extensions.  
B) A model of the protocol in an extension of the pi calculus with cryptography, similar to the applied pi calculus.  
C) Only security properties, without any protocol description.  
D) A full implementation of the protocol in a programming language, translated automatically.  
**Answer:** B

---

**5. Which of the following security properties can ProVerif verify based on its structure?**  
A) Only secrecy, as it is the primary focus of the applied pi calculus.  
B) Secrecy, authentication (correspondences), and some observational equivalence properties.  
C) Authentication and secrecy, but not observational equivalence, as that is handled by Horn clauses alone.  
D) Observational equivalence properties only, excluding secrecy and authentication.  
**Answer:** B

---

**6. How are cryptographic primitives modeled in ProVerif?**  
A) They are modeled exclusively by equational theories, as in the applied pi calculus.  
B) They are modeled by rewrite rules or by equations, allowing for a wide variety of primitives.  
C) They are not modeled directly and must be added as external extensions.  
D) They are modeled only through destructors, without any use of equations.  
**Answer:** B

---

**7. In ProVerif, what do substitutions primarily map when dealing with terms?**  
A) Substitutions always map names to expressions for flexibility.  
B) Substitutions always map variables (not names) to terms, and they never substitute fail or a may-fail variable for an ordinary variable.  
C) Substitutions map both variables and names to any type of expression without restrictions.  
D) Substitutions map variables to names only, to maintain the structure of the applied pi calculus.  
**Answer:** B

---

**8. What is the significance of observational equivalence in the context of ProVerif and the applied pi calculus?**  
A) ProVerif proves diff-equivalence, which is weaker than observational equivalence, making it less useful.  
B) If two processes are equivalent in the pi calculus, the corresponding applied pi calculus processes are observationally equivalent, but ProVerif focuses on the stronger diff-equivalence.  
C) Observational equivalence is not relevant, as ProVerif only deals with secrecy properties.  
D) ProVerif requires encoding into the applied pi calculus to prove observational equivalence directly.  
**Answer:** B

---

**9. How does ProVerif handle errors compared to the applied pi calculus?**  
A) ProVerif does not handle errors, relying entirely on the applied pi calculus's equational theory.  
B) ProVerif has a built-in error-handling construct (like the else branch), whereas the applied pi calculus does not explicitly include this.  
C) Both ProVerif and the applied pi calculus use the same error-handling mechanisms based on destructors.  
D) ProVerif avoids error handling by limiting the use of functions and equations.  
**Answer:** B

---

**10. What role do Horn clauses play in ProVerif's structure for verifying properties?**  
A) Horn clauses are used to model protocols directly, without involving derivability queries.  
B) Horn clauses are part of ProVerif's structure for derivability queries, which help in resolution to determine if a property holds or if there's an attack.  
C) Horn clauses are only used in the applied pi calculus and not in ProVerif's verification process.  
D) Horn clauses replace the need for extensions to the pi calculus in ProVerif.  
**Answer:** B

---

These questions are designed to assess key concepts from the content, such as the foundational relationship, extensions, differences, inputs, and features of ProVerif and the applied pi calculus. Each question has one correct answer based on the provided material, and the distractors are plausible (e.g., they draw from related ideas or partial truths to challenge students without being obviously wrong). If you need any adjustments or additional questions, let me know!