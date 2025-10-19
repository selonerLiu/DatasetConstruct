# topic：Parameter Matching: Function/destructor call requirements(Parameter count matching, Type consistency), Destructor-function constraints.

---
**1. For a destructor \(g\) of arity \(k\) with rewrite rules, what is the requirement regarding the types of its arguments?**
A) The arguments of \(g\) can have different types in each rewrite rule.
B) The arguments \(M_{1,1}, \ldots, M_{1,k}\) must have the same types as \(M_{i,1}, \ldots, M_{i,k}\) for \(i \in [2, m]\), and these are the types of the arguments of \(g\).
C) Only the first argument \(M_{1,1}\) needs to have a consistent type across all rewrite rules.
D) The types of the arguments are determined by the return type of \(g\).
**Answer:** B
---
**2. What happens when a destructor \(g\) of arity \(k\) is encountered during execution and no rewrite rule can be applied?**
A) The program continues execution ignoring the destructor.
B) The destructor is replaced with a default value.
C) The destructor fails.
D) The program tries to find an alternative rewrite rule in a different section of the code.
**Answer:** C
---
**3. In the context of pattern - matching, if a pattern \(f(pat_1,\ldots,pat_n)\) is used, what condition must hold for it to match a term \(f(M_1,\ldots,M_n)\)?**
A) The pattern can match regardless of whether \(pat_i\) matches \(M_i\) for \(i\leq n\).
B) \(pat_i\) must match \(M_i\) for all \(i\leq n\), and \(f\) must be a data constructor.
C) Only the first \(pat_1\) needs to match \(M_1\).
D) \(f\) can be any function symbol, not necessarily a data constructor.
**Answer:** B
---
**4. Regarding the return type of a destructor \(g\) defined by rewrite rules, which of the following is true?**
A) The return type can be different for each rewrite rule of \(g\).
B) The return types \(M_{1,0}, \ldots, M_{m,0}\) of all rewrite rules of \(g\) must have the same type.
C) The return type is determined by the type of the first argument of \(g\).
D) The return type is always a built - in type.
**Answer:** B
---
**5. What does it mean for a destructor to "fail" during execution?**
A) The program crashes immediately.
B) The pattern - matching associated with the destructor fails.
C) The destructor is re - evaluated with different arguments.
D) The destructor is replaced with a null value.
**Answer:** B
---
**6. When defining a destructor using rewrite rules of the form \(\forall x_{1,1}:t_{1,1}, \ldots, x_{1,n_1}:t_{1,n_1}; g(M_{1,1}, \ldots, M_{1,k}) = M_{1,0}\), what are the terms \(M_{1,1}, \ldots, M_{1,k}, M_{1,0}\) built from?**
A) They are built from destructor applications only.
B) They are built from the application of constructors to variables \(x_{1,1}, \ldots, x_{1,n_1}\) of types \(t_{1,1}, \ldots, t_{1,n_1}\) respectively.
C) They are built from random values.
D) They are built from a combination of built - in functions only.
**Answer:** B
---
**7. In the ProVerif language, for a destructor call, what is the requirement for parameter count matching?**
A) The number of parameters can vary in each call.
B) The number of parameters in the call must match the arity of the destructor.
C) The number of parameters is determined by the context of the call.
D) The destructor can accept any number of parameters.
**Answer:** B
---
**8. What is a key constraint on destructor - function calls regarding type consistency?**
A) Only the first parameter of a destructor call needs to have the correct type.
B) The types of all parameters in a destructor call must be consistent with the types specified in the rewrite rules.
C) Type consistency is not a requirement for destructor calls.
D) The return type of a destructor call does not need to match the types in the rewrite rules.
**Answer:** B
---
**9. For a data constructor \(f\) of arity \(n\) with associated destructors \(g_i\) for \(i\in\{1,\ldots,n\}\), how are these destructors defined?**
A) \(g_i\) can be defined in any way as long as they are related to \(f\).
B) \(g_i(f(x_1,\ldots,x_n)) \to x_i\).
C) \(g_i\) is defined based on the number of times \(f\) is used.
D) \(g_i\) is defined independently of \(f\).
**Answer:** B
---
**10. If a destructor \(g\) has multiple rewrite rules, and an instance of the term \(g(M_{1,1}, \ldots, M_{1,k})\) is encountered during execution, what is the process for handling it?**
A) It is replaced with a random value.
B) The program tries the first rewrite rule. If it is applicable, the term is reduced according to that rule. Otherwise, it tries the second rewrite rule and so on.
C) It is always replaced with the first result \(M_{1,0}\) from the first rewrite rule.
D) The program skips all rewrite rules and continues execution.
**Answer:** B
---