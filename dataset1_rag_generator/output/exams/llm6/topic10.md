# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

---
**1. Which of the following is a valid way to represent a function application in the given expressions?**
A) `h(D1, D2)` where `h` is a function and `D1`, `D2` are expressions.
B) `D1 + D2` where `D1` and `D2` are expressions (assuming `+` is not allowed in this context).
C) `f()` where `f` is a function but no arguments are provided (and the function requires arguments).
D) `(D1, D2)` which is just a tuple and not a function application.
**Answer:** A
---
**2. When evaluating a function `g(D1,...,Dn)` and no rewrite rule applies, what is the result?**
A) The function keeps evaluating indefinitely.
B) It evaluates to the constant `fail`.
C) It evaluates to the first argument `D1`.
D) It raises an undefined function error.
**Answer:** B
---
**3. Which of the following is a valid tuple construction according to the given context?**
A) `tupleT1,T2(M1, M2)` where `tupleT1,T2` is a constructor taking arguments of types `T1` and `T2`.
B) `(M1, M2)` without a proper constructor (not in the defined tuple construction format).
C) `tuple(M1, M2)` where `tuple` is not a defined constructor in the given rules.
D) `M1,M2` which is just a list of terms and not a proper tuple construction.
**Answer:** A
---
**4. An expression can be composed of all of the following except**:
A) Variables.
B) Constants.
C) Infix symbols that are not allowed in the grammar of terms (e.g., `||` in reduc and equation declarations).
D) Function calls.
**Answer:** C
---
**5. If we have a function `g` defined by rewrite rules `g(U1,...,Un) → U`, and `U1,...,Un` are may - fail terms, what does it mean if `U1` is `fail`?**
A) The evaluation of `g(U1,...,Un)` will always succeed and return a valid term.
B) The evaluation of `g(U1,...,Un)` may fail depending on the rewrite rules.
C) The evaluation of `g(U1,...,Un)` will always succeed and return `fail`.
D) The function `g` cannot accept `fail` as an argument.
**Answer:** B
---
**6. In the expression `h(D1,...,Dk)` where `h` is in `Fd ∪ Fc`, what does `Fd ∪ Fc` represent?**
A) A set of constants.
B) A set of variables.
C) A set of function symbols that can be used in function applications.
D) A set of terms that can be used as operands.
**Answer:** C
---
**7. Which of the following is a correct way to represent an expression evaluation construct?**
A) `let x: T = D in D′ else D′′`
B) `let x = D; D′; D′′` (not in the correct format).
C) `x: T = D; D′; D′′` (not a valid expression evaluation construct).
D) `let x: T = D D′ D′′` (not in the correct format).
**Answer:** A
---
**8. If we have a function `g` with rewrite rules and we want to evaluate `g(D1, D2)`, and the first rewrite rule does not apply, what should we do next?**
A) Stop the evaluation and return `fail`.
B) Try the second rewrite rule.
C) Try to apply the first rewrite rule again with different arguments.
D) Change the function `g` to a different function.
**Answer:** B
---
**9. A tuple `tupleT1,T2(M1, M2)` is a data structure that**:
A) Can only be used in a conditional statement.
B) Is used to represent a single value of type `bitstring` composed of `M1` and `M2`.
C) Can only be used in a parallel composition process.
D) Is not an evaluable unit.
**Answer:** B
---
**10. In an expression, a variable can be**:
A) Only used as an operand in a constant.
B) Substituted by a term.
C) Only used in a function call but not as an argument.
D) Only used in a conditional statement.
**Answer:** B
---