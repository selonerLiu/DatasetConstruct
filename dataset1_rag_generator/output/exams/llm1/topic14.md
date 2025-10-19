# topic：Parameter Matching: Function/destructor call requirements(Parameter count matching, Type consistency), Destructor-function constraints.

---
**1. In the context of destructor function symbols in ProVerif, what happens when no rewrite rule applies to a destructor in a term?**  
A) The term is evaluated as true.  
B) The destructor succeeds with a default value.  
C) The destructor fails and the whole pattern-matching fails.  
D) The term is skipped and the evaluation continues.  
**Answer:** C  
---

**2. What is the main characteristic of a "simple" pattern cpat in the given definitions?**  
A) It contains only variables and constants without constructors.  
B) Every destructor occurrence =D in cpat is a may-fail constructor term U.  
C) It uses nested destructor function symbols only.  
D) It contains no equals sign (=) in its structure.  
**Answer:** B  
---

**3. According to the content, what form must the expression in a conditional statement take in ProVerif to comply with the specified restrictions?**  
A) M < N or M > N  
B) M = N  
C) M && N  
D) not M  
**Answer:** B  
---

**4. How are new destructors defined in the system according to the content?**  
A) By writing them as public functions without any constraints.  
B) Only by extending the definitions given in Section 3.1.1.  
C) By providing a sequence of rewrite rules specifying pattern matching and reduction.  
D) Through macros that combine constructors and destructors arbitrarily.  
**Answer:** C  
---

**5. What is the requirement for a converter function in relation to its argument and the same-type values without conversion?**  
A) It must be identical to its argument and type neutral.  
B) It must always produce a value of a different type than its argument.  
C) It must be different from its argument, different also from values of the same type without applying the converter, and must identify which converter was applied.  
D) It can return the same value as the argument if the types match.  
**Answer:** C  
---

**6. When matching a pattern f(pat1,...,patn) to a term f(M1,...,Mn), under what condition is this pattern valid according to the provided content?**  
A) When f is any function symbol, public or private.  
B) When f is a data constructor and each pati matches Mi for all i ≤ n.  
C) When the destructors are absent in the pattern.  
D) When pat1 matches M1 only and the others are ignored.  
**Answer:** B  
---

**7. What must be true about the types of arguments in destructor rewrite rules such as g(M1,1,...,M1,k) = M1,0?**  
A) The return type M1,0 can be different from the types of Mi,j.  
B) All arguments M1,1,...,M1,k must have the same type, and M1,0 must have the type specified by the destructor g.  
C) Types do not need to be consistent if the rewrite rules are convergent.  
D) Types of arguments can vary arbitrarily across different rewrite rules.  
**Answer:** B  
---

**8. In the process statements like `let x = M in P else Q`, why is it important to consider that M may contain destructor functions?**  
A) Because destructors always succeed and simplify evaluation.  
B) Because destructors may fail, causing the entire let expression to fail and trigger the else branch.  
C) Because destructors cause variables to be typed as null.  
D) Because destructors make the term M immutable.  
**Answer:** B  
---

**9. Regarding patterns and may-fail constructor terms, what is implied if a pattern contains a destructor function symbol that is not a may-fail constructor term?**  
A) The pattern is considered simple.  
B) The pattern cannot be processed and will always fail.  
C) The pattern is not simple, and may require more complex matching semantics.  
D) The pattern automatically succeeds regardless of the term matched.  
**Answer:** C  
---

**10. What is the significance of the condition that the expression evaluation construct is removed in the ProVerif subset considered?**  
A) To simplify the matching so that only public functions and equality are used.  
B) To allow arbitrary computations in conditionals.  
C) To accept destructors anywhere in the program without limitation.  
D) To increase the complexity of term rewriting and matching.  
**Answer:** A  
---

