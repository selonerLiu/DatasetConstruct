# topic：Declaration of Types, Variables, and Constants: Definition methods，Roles in the system, Introduction mechanisms.

---
**1. How can a constant be defined in the described system?**
A) A constant can only be defined using the “const c : t” construct.
B) A constant may be defined as a function of arity 0, like “fun c() : t.”
C) A constant is always an atomic data like keys and nonces.
D) Constants are defined without any type declaration.
**Answer:** B
---
**2. What is the role of names in the system?**
A) Names can be substituted by terms just like variables.
B) Names represent atomic data such as keys and nonces.
C) Names are used only for defining constructors.
D) Names are always declared as free names.
**Answer:** B
---
**3. When declaring function symbols, what does “h(T1,...,Tn) : T” mean?**
A) The function h takes T arguments of types T1,...,Tn respectively.
B) The function h takes n arguments of the same type T.
C) The function h takes n arguments of types T1,...,Tn respectively, and returns a value of type T.
D) The function h returns n values of types T1,...,Tn respectively.
**Answer:** C
---
**4. How should all free names appearing within an input file be declared?**
A) Using the syntax “type n : t”.
B) Using the syntax “free n : t”.
C) Using the syntax “const n : t”.
D) Free names do not need to be declared.
**Answer:** B
---
**5. Which of the following is a built - in type in ProVerif?**
A) integer
B) bitstring
C) float
D) char
**Answer:** B
---
**6. What is the correct way to declare a user - defined type?**
A) const t.
B) fun t().
C) type t.
D) free t.
**Answer:** C
---
**7. What is the meaning of the construct “⟨decl⟩∗ process ⟨process⟩”?**
A) It represents a single declaration followed by a process.
B) It represents a list of declarations followed by a process.
C) It represents an equivalence query between two processes.
D) It represents a single declaration followed by an equivalence query.
**Answer:** B
---
**8. Regarding the identifiers in ProVerif, which of the following statements is correct?**
A) The built - in identifiers like “attacker” can be freely reused without any issues.
B) The authors encourage reusing built - in identifiers as regular identifiers.
C) Although the built - in identifiers can be reused, the authors strongly discourage this practice.
D) Built - in identifiers cannot be reused under any circumstances.
**Answer:** C
---
**9. Which of the following is a destructor in ProVerif?**
A) attacker
B) is nat
C) mess
D) subterm
**Answer:** B
---
**10. What does the syntax “⟨decl⟩∗ equivalence ⟨process⟩ ⟨process⟩” represent?**
A) A single declaration followed by an equivalence between two processes.
B) A list of declarations followed by an equivalence query between two processes.
C) A single declaration followed by a process.
D) A list of declarations followed by a single process.
**Answer:** B
---