# topic：Theoretical and Methodological Foundations for Security Verification : Representation and verification of secrecy properties based on reachability analysis.

---
**1. What is ProVerif's most basic capability?**
A) Proving correspondence properties.
B) Proving reachability properties.
C) Proving equivalence properties.
D) Proving authentication properties.
**Answer:** B
---
**2. To test the secrecy of the term M in the model in ProVerif, what query should be included in the input file before the main process?**
A) query secrecy(M).
B) query reachable(M).
C) query attacker(M).
D) query secure(M).
**Answer:** C
---
**3. What does the symbolic model, often called the Dolev - Yao model, consider cryptographic primitives as?**
A) Imperfect blackboxes with random behavior.
B) Perfect blackboxes modeled by function symbols in an algebra of terms.
C) Complex algorithms with internal states.
D) User - defined functions.
**Answer:** B
---
**4. In the context of ProVerif, which of the following is the main reference for the proof of equivalences?**
A) Blanchet, 2009
B) Blanchet et al., 2008
C) Blanchet, 2014
D) Blanchet, 2016
**Answer:** B
---
**5. What does strong secrecy (in the case without equational theory) verified by ProVerif mean?**
A) The adversary can distinguish two versions of the protocol using different secret values.
B) The secret is always encrypted during the protocol.
C) The adversary cannot distinguish two versions of the protocol that use different values of the secret.
D) The secret is shared only between trusted parties.
**Answer:** C
---
**6. In the symbolic model, what can the adversary compute using?**
A) Any arbitrary algorithm.
B) Only the cryptographic primitives modeled in the algebra of terms.
C) Only brute - force methods.
D) Special encryption keys.
**Answer:** B
---
**7. Which of the following is the simplest security property ProVerif deals with?**
A) Correspondences
B) Equivalences
C) Secrecy
D) Authentication
**Answer:** C
---
**8. What kind of terms can be used in the query "query attacker(M)"?**
A) Terms with destructors.
B) Ground terms without destructors and containing free names.
C) Non - ground terms.
D) Terms with complex logical operators.
**Answer:** B
---
**9. The reference "Blanchet, B. 2014" is mainly about?**
A) Automated verification of selected equivalences for security protocols.
B) Automatic verification of security protocols in the symbolic model: the verifier ProVerif.
C) Modeling and verifying security protocols with the applied pi calculus and ProVerif.
D) Secrecy types for asymmetric communication.
**Answer:** B
---
**10. In the context of ProVerif, when dealing with secrecy, what is the first step in the verification process?**
A) Formalize the notion of an adversary.
B) Define the cryptographic primitives.
C) Write the main process in the input file.
D) Test the equivalence properties.
**Answer:** A
---