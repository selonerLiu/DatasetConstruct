# topic：Process Constructs(Statements): Fundamental units for program execution steps in ProVerif, including Control flow (e.g., if-then-else), Declarations, Input (in)/output (out) operations, Termination, Process composition.

Here are 10 multiple-choice questions designed to test students' understanding of **Process Constructs (Statements)** in ProVerif:

---

**1. Which construct represents a process that does nothing in ProVerif?**  
A) `null`  
B) `0`  
C) `stop`  
D) `nil`  
**Answer:** B  

---

**2. What is the purpose of the `phase n; P` construct in ProVerif?**  
A) To terminate the process after `n` steps.  
B) To synchronize processes globally by advancing to phase `n` and discarding earlier phases.  
C) To loop the process `P` for `n` iterations.  
D) To restrict the scope of names in `P` to phase `n`.  
**Answer:** B  

---

**3. How is a constant defined in ProVerif?**  
A) `const c = t;`  
B) `fun c(): t.` or `const c : t.`  
C) `let c : t = ...;`  
D) `define c as t;`  
**Answer:** B  

---

**4. Which of the following is NOT a valid process composition construct in ProVerif?**  
A) `P | Q` (parallel composition)  
B) `P + Q` (non-deterministic choice)  
C) `!P` (replication)  
D) `new n: t; P` (name restriction)  
**Answer:** B  

---

**5. What does the process `in(M, x: t); P` model?**  
A) Output a term `M` on channel `x`, then execute `P`.  
B) Input a term on channel `M`, bind it to `x`, then execute `P`.  
C) Evaluate `M` and assign it to `x`, then run `P`.  
D) Check if `M` equals `x`, then execute `P`.  
**Answer:** B  

---

**6. Which construct is used to express correspondence properties (e.g., "if `end(M)` occurs, `begin(M)` must have occurred")?**  
A) `event(e(M1,...,Mn)); P`  
B) `assert(M); P`  
C) `phase n; P`  
D) `if M then P else Q`  
**Answer:** A  

---

**7. How is the conditional statement structured in ProVerif?**  
A) `if M then P` (no else clause).  
B) `if M then P else Q` (else is mandatory).  
C) `case M of P else Q`.  
D) `when M do P`.  
**Answer:** B  

---

**8. Which limitation does ProVerif have regarding cryptographic primitives?**  
A) It cannot handle symmetric encryption.  
B) Modular exponentiation cannot be directly represented via rewrite rules.  
C) It only supports hash functions.  
D) Destructors cannot be defined.  
**Answer:** B  

---

**9. What is the role of `new n: t; P`?**  
A) To create a public channel `n` for process `P`.  
B) To restrict the scope of the fresh name `n` to process `P`.  
C) To declare a global variable `n` of type `t`.  
D) To output `n` on channel `t`.  
**Answer:** B  

---

**10. Which process construct is used to model infinite replication of `P`?**  
A) `loop P`  
B) `!P`  
C) `repeat P`  
D) `P*`  
**Answer:** B  

--- 

Each question tests a distinct aspect of process constructs, with plausible distractors and clear answers. The format aligns with your example.