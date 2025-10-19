# topic：Declaration of Functions and Destructors: Definition methods，Roles in the system, Introduction mechanisms.

Here are **10 multiple-choice questions** designed to assess students' understanding of the topic:  
**"Declaration of Functions and Destructors: Definition methods, Roles in the system, Introduction mechanisms."**

---

**1. In the formalism described, what is the role of a destructor function symbol like `g`?**  
A) It constructs new terms from existing ones.  
B) It only appears in process definitions.  
C) It manipulates terms using rewrite rules to produce other terms.  
D) It represents atomic data such as keys or nonces.  
**Answer:** C

---

**2. Which of the following correctly describes how names (`a`, `b`, `c`, etc.) are treated in this formalism?**  
A) They can be substituted by other terms during execution.  
B) They represent variables that change over time.  
C) They must always be declared with their type before use.  
D) They are not part of the typed language.  
**Answer:** C

---

**3. What is the correct way to declare a free name `n` of type `t` in this formalism?**  
A) `name n : t.`  
B) `free n : t.`  
C) `var n : t.`  
D) `decl n : t.`  
**Answer:** B

---

**4. How are destructors defined when using the extended method introduced in Section 4.2.1?**  
A) Using a single `fun` declaration without conditions.  
B) By declaring them as constants of arity zero.  
C) Through an ordered list of rewrite rules using `reduc`.  
D) By assigning them directly to a constructor function.  
**Answer:** C

---

**5. What is the purpose of the syntax `h(T1, ..., Tn) : T` for function symbols?**  
A) It defines a variable substitution rule.  
B) It specifies the types of inputs and output for the function `h`.  
C) It declares a set of rewrite rules for a destructor.  
D) It creates a new atomic name.  
**Answer:** B

---

**6. Which of the following best describes the difference between constructors and destructors in this formalism?**  
A) Constructors manipulate terms using rewrite rules, while destructors build terms.  
B) Both can appear anywhere in processes, but destructors are faster.  
C) Constructors build terms, while destructors break them down using rules.  
D) There is no functional difference; both refer to the same class of functions.  
**Answer:** C

---

**7. In ProVerif, how can a constant `c` of type `t` be declared?**  
A) `fun c() : t.`  
B) `const c : t.`  
C) Either `fun c() : t.` or `const c : t.`  
D) Constants cannot be declared in ProVerif.  
**Answer:** C

---

**8. What happens if none of the rewrite rules for a destructor apply to a given term?**  
A) The process terminates successfully.  
B) The destructor returns a default value of zero.  
C) The destructor fails and may lead to process failure.  
D) The system automatically generates a new rule.  
**Answer:** C

---

**9. Which of the following is a built-in destructor in ProVerif?**  
A) `tuple`  
B) `true`  
C) `not`  
D) `fun`  
**Answer:** C

---

**10. Why are equations introduced in the context of destructors and cryptographic primitives?**  
A) To simplify variable declarations.  
B) To allow modular exponentiation and other complex operations not expressible via rewrite rules alone.  
C) To replace all rewrite rules with simpler expressions.  
D) To optimize performance of basic protocols.  
**Answer:** B

--- 

Let me know if you'd like these adapted into a printable quiz format or need explanations for each answer!