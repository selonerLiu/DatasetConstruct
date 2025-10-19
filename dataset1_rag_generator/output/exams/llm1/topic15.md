# topic：Theoretical and Methodological Foundations for Security Verification : Representation and verification of secrecy properties based on reachability analysis.

---
**1. What is ProVerif primarily used to verify in security protocols?**  
A) Performance optimization of protocols  
B) Reachability and secrecy properties of terms  
C) User authentication methods  
D) Network topology configurations  
**Answer:** B

---
**2. In ProVerif, which query is used to test if a term M is secret from an attacker?**  
A) query secret(M).  
B) query reachable(M).  
C) query attacker(M).  
D) query accessible(M).  
**Answer:** C

---
**3. When defining the term M in the secrecy query in ProVerif, what must be true about M?**  
A) M can include destructors and free names.  
B) M must be a ground term without destructors but may contain free names.  
C) M can be any variable defined in the process.  
D) M must be a public name only.  
**Answer:** B

---
**4. What does the reachability property in ProVerif determine?**  
A) Which protocols are the fastest to execute.  
B) Whether an attacker can derive a specific term from the protocol.  
C) If the protocol satisfies user authentication requirements.  
D) The equivalence between two protocols.  
**Answer:** B

---
**5. Strong secrecy in the context of ProVerif means:**  
A) The term cannot be decrypted by any participant in the system.  
B) The adversary cannot distinguish between two protocol executions using different secret values.  
C) The secret remains unchanged during the entire protocol execution.  
D) The secret can be reconstructed only by trusted parties.  
**Answer:** B

---
**6. How does ProVerif model cryptographic primitives in the symbolic (Dolev-Yao) model?**  
A) As imperfect black boxes with probabilistic algorithms.  
B) As perfect black boxes modeled by function symbols and equations.  
C) As plaintext strings only.  
D) As random number generators.  
**Answer:** B

---
**7. Which of the following is NOT a category of security properties verified by ProVerif mentioned in the content?**  
A) Secrecy  
B) Correspondences  
C) Authentication  
D) Cryptanalysis resistance  
**Answer:** D

---
**8. The simplest property to verify using ProVerif is:**  
A) Equivalence between different protocols.  
B) Strong secrecy of terms.  
C) Full correctness of message ordering.  
D) Performance timing of cryptographic operations.  
**Answer:** B

---
**9. In a ProVerif input file, where should the secrecy query be placed relative to the main process?**  
A) After the main process definition  
B) Before the main process definition  
C) Outside the input file  
D) Anywhere; the order does not matter  
**Answer:** B

---
**10. Which formalizes an adversary in the context of ProVerif’s security analysis?**  
A) As an external system with unlimited computational power but limited knowledge of keys.  
B) As a participant who follows the protocol honestly.  
C) As a passive observer with no ability to intercept messages.  
D) As a function symbol inside the protocol process.  
**Answer:** A

---