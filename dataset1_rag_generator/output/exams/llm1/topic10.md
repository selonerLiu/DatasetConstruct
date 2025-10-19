# topic：Expressions (Terms): Composition of operators/operands (variables, constants, function calls) into evaluable units, including Function applications, or Tuple constructions.

---
**1. In the context of ProVerif expressions, what does the evaluation relation \(D \Downarrow V\) represent?**  
A) The expression \(D\) is syntactically valid and \(V\) is a variable.  
B) The expression \(D\) evaluates to the value \(V\) where \(V\) is either a ground term or fail.  
C) \(D\) is a destructor that transforms \(V\) into \(D\).  
D) \(D\) and \(V\) are equivalent terms by syntactic equality.  
**Answer:** B

---
**2. Which of the following best describes a ground term in the ProVerif syntax?**  
A) A term that contains at least one variable.  
B) A constructor with at least one argument that is a variable.  
C) A term that contains no variables.  
D) An expression that always evaluates to fail.  
**Answer:** C

---
**3. What is the role of the constant 'fail' in terms and expressions?**  
A) It represents a successful computation result.  
B) It denotes the failure of computation or evaluation.  
C) It is a special constant that stands for true conditions.  
D) It acts as a constructor for tuples.  
**Answer:** B

---
**4. How are expressions extended in ProVerif to include process constructs?**  
A) By allowing expressions to reference global variables only.  
B) By including restrictions, expression evaluations (let), and conditionals within expressions.  
C) By replacing variables with constants only.  
D) By restricting the use of destructors in expressions.  
**Answer:** B

---
**5. In the syntax of processes, what does the construct `let x: T = D in P else Q` mean?**  
A) It declares variable \(x\) as an unrestricted variable.  
B) It defines \(x\) by evaluating \(D\); if evaluation fails, process \(Q\) is executed; otherwise, process \(P\).  
C) It runs both \(P\) and \(Q\) in parallel after evaluating \(D\).  
D) It duplicates process \(P\) with and without \(x\).  
**Answer:** B

---
**6. Consider the destructor \(g(U_1,...,U_n) \to U\). What happens if no rewrite rule applies during evaluation?**  
A) The evaluation proceeds to the next rule.  
B) The evaluation returns a variable.  
C) The evaluation fails and yields the constant fail.  
D) The evaluation returns \(U\) by default.  
**Answer:** C

---
**7. How is pattern-matching incorporated in ProVerif’s input constructs?**  
A) It is only allowed in output expressions.  
B) It enriches inputs with `in(D, pat); P` to match expressions against patterns during input.  
C) It replaces variables with constants automatically.  
D) Pattern-matching is not supported in process inputs.  
**Answer:** B

---
**8. What is the difference between a term \(M\) and an expression \(D\) in the ProVerif core language?**  
A) \(M\) can include process constructs, but \(D\) cannot.  
B) \(M\) is always ground, while \(D\) always contains variables.  
C) \(M\) is a term without process constructs, while \(D\) can include expressions such as restriction, let, and conditionals.  
D) \(D\) only consists of variables, and \(M\) only of constants.  
**Answer:** C

---
**9. What is the meaning of `new a: T; D` in expressions?**  
A) It deletes the name \(a\) from the scope of \(D\).  
B) It creates a new name \(a\) of type \(T\) and then evaluates the enriched term \(D\).  
C) It declares a constant \(a\) that cannot be used in \(D\).  
D) It starts a new process with a fresh variable \(a\).  
**Answer:** B

---
**10. When expressing a process input with pattern matching `in(D, pat); P`, what happens if the received message does not match the pattern?**  
A) The process immediately fails.  
B) The input blocks until a matching message is received.  
C) The process continues with \(P\) ignoring the input.  
D) The unmatched message is discarded and the process restarts.  
**Answer:** B

---