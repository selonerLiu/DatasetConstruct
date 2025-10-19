# topic：Parameter Matching: Function/destructor call requirements(Parameter count matching, Type consistency), Destructor-function constraints.

Here are 10 multiple-choice questions designed to test students' understanding of **Parameter Matching: Function/destructor call requirements (parameter count matching, type consistency), Destructor-function constraints**, based on the provided content.

---

**1. In ProVerif, what is a requirement for a destructor function symbol when used in a pattern-matching context?**

A) It must be defined without any rewrite rules.  
B) It must always return a boolean value.  
C) It must only appear within conditional expressions like `if M = N`.  
D) It must be applied to terms that do not contain constructor symbols.  

**Answer:** C

---

**2. What is a key condition for using a function symbol as a data constructor in pattern-matching?**

A) The function must have no associated destructors.  
B) The function must be declared with a single rewrite rule.  
C) The function must be accompanied by destructors that extract its arguments.  
D) The function must return a built-in type such as `bool` or `int`.  

**Answer:** C

---

**3. When matching a pattern of the form `f(pat1, ..., patn)` in ProVerif, what must be true about the function `f`?**

A) It must be a destructor function.  
B) It must be a public function.  
C) It must be a data constructor.  
D) It must be a conditional expression.  

**Answer:** C

---

**4. What happens if a destructor function is applied to a term for which none of its rewrite rules are applicable?**

A) The term evaluates to zero.  
B) The pattern-matching succeeds silently.  
C) The destructor fails and the pattern-matching fails accordingly.  
D) The system automatically applies a default rewrite rule.  

**Answer:** C

---

**5. For a destructor `g` with arity `k`, what must be consistent across all rewrite rules defining it?**

A) The number of variables used in each rule.  
B) The types of its arguments across all rules.  
C) The return type of the destructor in each rule.  
D) Both B and C.  

**Answer:** D

---

**6. Which of the following best describes a "simple" pattern in the context of ProVerif’s pattern-matching semantics?**

A) A pattern containing only built-in constants like `true` or `false`.  
B) A pattern where all occurrences of `=D` involve a may-fail constructor term `U`.  
C) A pattern that does not include any destructors.  
D) A pattern that uses only one variable binding.  

**Answer:** B

---

**7. What is a necessary condition for a let-binding like `let x = M in P else Q` to succeed when `M` contains destructors?**

A) `M` must be a constructor-only term.  
B) All destructors in `M` must evaluate successfully.  
C) `Q` must be the null process.  
D) `x` must be of a base type like `int` or `bool`.  

**Answer:** B

---

**8. Why must a type converter function produce a value different from values obtained without applying the same converter?**

A) To allow polymorphic behavior.  
B) To ensure termination of evaluation.  
C) To uniquely identify which type conversion was applied during pattern-matching.  
D) To simplify the syntax of constructor applications.  

**Answer:** C

---

**9. In ProVerif, what must be true about the use of the equality destructor `equal(M, N)` outside of conditional expressions?**

A) It can be used freely in any term.  
B) It must be enclosed in a tuple.  
C) It must be part of a function macro definition.  
D) It cannot occur outside of conditional expressions.  

**Answer:** D

---

**10. Which of the following is NOT allowed when using enriched terms in ProVerif with equations?**

A) Declaring all function symbols as public.  
B) Using the expression evaluation construct.  
C) Writing conditionals of the form `if M = N`.  
D) Using equations to define destructors.  

**Answer:** B

---