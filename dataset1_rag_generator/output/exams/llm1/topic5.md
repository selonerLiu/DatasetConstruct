# topic：Operators: Defined operators in ProVerif: Meanings, Usage methods.

---
**1. In ProVerif, which of the following operators represents the term equality check between two terms M and N?**  
A) M <> N  
B) M = N  
C) not(M)  
D) M && N  
**Answer:** B  
---

**2. Which operator in ProVerif is used to express the negation of a term M?**  
A) M || N  
B) M && N  
C) not(M)  
D) M <> N  
**Answer:** C  
---

**3. What is the purpose of the operator ‘new n : t; P’ in ProVerif processes?**  
A) To declare a constant named n of type t used globally  
B) To create a fresh name n of type t restricted to process P  
C) To output the name n of type t to process P  
D) To declare a variable n of type t used in process P  
**Answer:** B  
---

**4. In the context of ProVerif, what does the operator ‘if M then P else Q’ accomplish?**  
A) It loops executing process P while M holds true  
B) It conditionally executes process P if M evaluates to true, else executes Q  
C) It defines a non-deterministic choice between P and Q  
D) It outputs messages M to processes P and Q  
**Answer:** B  
---

**5. Which operator correctly represents the conjunction (logical AND) of two terms M and N in ProVerif?**  
A) M || N  
B) M && N  
C) not(M)  
D) M = N  
**Answer:** B  
---

**6. When modeling message transmission in ProVerif, which operator is used to represent sending a message N on channel M followed by process P?**  
A) in(M, N); P  
B) out(M, N); P  
C) new M; out(N, P)  
D) get(M, N); P  
**Answer:** B  
---

**7. What kind of ProVerif process does the operator ‘!P’ denote?**  
A) A conditional statement depending on P  
B) The null process that does nothing  
C) The replication of process P indefinitely  
D) Parallel composition of process P with itself  
**Answer:** C  
---

**8. Which of the following operators is used in ProVerif to represent the disjunction (logical OR) of two terms M and N?**  
A) M && N  
B) M || N  
C) not(M)  
D) M = N  
**Answer:** B  
---

**9. If you want to represent parallel execution of two processes P and Q in ProVerif, which operator do you use?**  
A) P ; Q  
B) P | Q  
C) !P | Q  
D) new P; Q  
**Answer:** B  
---

**10. In ProVerif, what does the operator ‘in(M, x: t); P’ represent?**  
A) Receiving a message from channel M and storing it in variable x of type t before executing P  
B) Sending a message M with payload x of type t followed by P  
C) Declaring a new input channel M of type t used by P  
D) Replicating process P x times on channel M  
**Answer:** A  
---