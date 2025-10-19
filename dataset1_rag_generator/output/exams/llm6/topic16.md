# topic：Theoretical and Methodological Foundations for Authentication Verification: Representation and verification of authentication properties using corresponding assertions.

---
**1. What can be used to capture authentication in the handshake protocol?**
A) Secrecy assertions
B) Correspondence assertions
C) Observational equivalence assertions
D) Privacy assertions
**Answer:** B
---
**2. What is the purpose of the handshake protocol regarding authentication?**
A) To ensure the client can communicate with any server
B) To ensure that if client A thinks she executes the protocol with server B, she really does so
C) To ensure the server can authenticate multiple clients simultaneously
D) To ensure the secrecy of the communication between the client and the server
**Answer:** B
---
**3. Which of the following is not a security property that ProVerif can verify?**
A) Secrecy
B) Traceability
C) Randomness
D) Authentication
**Answer:** C
---
**4. How does ProVerif translate the protocol and security properties to be proved?**
A) It translates them into linear equations
B) It translates them into an internal representation by Horn clauses
C) It translates them into a set of differential equations
D) It translates them into a graphical representation
**Answer:** B
---
**5. What does Tamarin need from the user to guide the proof when verifying protocols for an unbounded number of sessions?**
A) Some lemmas
B) A set of initial values
C) A graphical model of the protocol
D) A list of all possible events
**Answer:** A
---
**6. Which of the following is an advantage of using correspondence assertions in authentication verification?**
A) They can only be used for simple protocols
B) They can capture authentication and are useful for analyzing secrecy and authentication properties
C) They are only applicable to the computational model
D) They are difficult to represent and verify
**Answer:** B
---
**7. When proving properties of the form “if some event e1 has been executed, then some event e2 has or will be executed”, what can the verifier show automatically?**
A) The exact time when e2 will be executed
B) The correspondence assertion: if e1 has been executed, then some events e′2
C) The probability of e2 being executed
D) The sequence of all events between e1 and e2
**Answer:** B
---
**8. Which of the following protocols was analyzed by combining manual proofs with ProVerif proofs of correspondences and equivalences?**
A) Certified email protocol
B) JFK (Just Fast Keying) protocol
C) Plutus file system protocol
D) Direct Anonymous Attestation protocol
**Answer:** B
---
**9. What did Weidenbach introduce in 1999 regarding protocol verification?**
A) The use of differential equations for protocol verification
B) The idea of using Horn clauses for verifying protocols
C) The concept of observational equivalence for authentication
D) The method of using correspondence assertions for secrecy verification
**Answer:** B
---
**10. Canetti and Herzog (2006) showed that for a restricted class of protocols using only public - key encryption, what does a proof in the Dolev - Yao model imply?**
A) Security in the symbolic model
B) Security in the computational model in the universal composability framework
C) Security in the observational equivalence model
D) Security in the correspondence assertion model
**Answer:** B
---