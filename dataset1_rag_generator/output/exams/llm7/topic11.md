# topic：Process Constructs(Statements): Fundamental units for program execution steps in ProVerif, including Control flow (e.g., if-then-else), Declarations, Input (in)/output (out) operations, Termination, Process composition.

---
**1. What is a constant in the context of ProVerif's input language?**
A) A variable that can change its value during execution.
B) A function with arity 0.
C) A process that does nothing.
D) A special type of destructor.
**Answer:** B
---

---
**2. Which of the following is a specific construct for constants in ProVerif?**
A) `var c : t`
B) `fun c() : t`
C) `const c : t`
D) `proc c : t`
**Answer:** C
---

---
**3. In ProVerif, what is the nil process represented by?**
A) A process that performs a specific task.
B) A process that does nothing.
C) A process that represents an error state.
D) A process that terminates immediately.
**Answer:** B
---

---
**4. What does the syntax of terms and processes in ProVerif's input language assume?**
A) A set of symbols for constructors and destructors.
B) A set of symbols for variables and names.
C) A set of symbols for control flow statements.
D) A set of symbols for input and output operations.
**Answer:** A
---

---
**5. How does ProVerif handle the limitation of representing modular exponentiation in its framework?**
A) It uses destructors defined by rewrite rules.
B) It supports equations as explained in §2.5.1.
C) It uses the nil process to overcome the limitation.
D) It cannot represent modular exponentiation.
**Answer:** B
---

---
**6. What is the purpose of process macros in ProVerif?**
A) To define destructors for cryptographic primitives.
B) To ease the development by allowing sub-processes to be defined.
C) To model the handshake protocol.
D) To represent atomic data such as keys and nonces.
**Answer:** B
---

---
**7. What does the phase construct in ProVerif represent?**
A) A local synchronization between processes.
B) A global synchronization that increments phases.
C) A way to model different stages of a protocol.
D) A construct to represent the end of a process.
**Answer:** C
---

---
**8. In ProVerif, what is the purpose of the event construct?**
A) To execute a certain program point with specific values.
B) To record that a certain program point has been reached.
C) To model the input on a channel.
D) To represent the output of a message.
**Answer:** B
---

---
**9. How does ProVerif internally evaluate a [Query] provided by the user?**
A) By proving that a state in which a property is violated is reachable.
B) By attempting to reconstruct a violated property.
C) By proving that a state in which a property is violated is unreachable.
D) By directly executing the query without analysis.
**Answer:** C
---

---
**10. What is the role of auxiliary events in ProVerif's process calculus?**
A) To execute specific program points with values.
B) To model the input and output operations.
C) To specify security properties related to the execution of events.
D) To represent the termination of a process.
**Answer:** C
---