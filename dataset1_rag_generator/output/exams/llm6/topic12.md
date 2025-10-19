# topic：Structural Units: Organization of processes and process macros into larger code blocks to implement protocol workflows.Definition and usage methods for processes and process macros in ProVerif.

---
**1. In ProVerif, how are sub - processes specified in the declarations to facilitate development?**
A) By encoding them directly into the main process without any additional syntax.
B) Using macros of the form let R(x1 : t1, ..., xn : tn) = P.
C) By writing them as separate functions outside the main code.
D) By using a special "sub - process" keyword.
**Answer:** B
---
**2. What does the macro expansion R(M1, ..., Mn) do in ProVerif?**
A) It replaces the macro name R with a random value.
B) It expands to P with M1, ..., Mn substituted for x1, ..., xn respectively.
C) It deletes the macro definition from the code.
D) It creates a new macro with the given arguments.
**Answer:** B
---
**3. In ProVerif, how are user - defined types declared?**
A) Using the syntax type t.
B) By writing t = type.
C) By using the "user - type" keyword followed by the type name.
D) There is no way to declare user - defined types.
**Answer:** A
---
**4. How should free names appearing within an input file in ProVerif be declared?**
A) Using the syntax free n : t.
B) By just writing the name n without any type specification.
C) Using the "free - name" keyword followed by the name.
D) They don't need to be declared.
**Answer:** A
---
**5. What is the purpose of the phase construct in ProVerif?**
A) It is used to define the color scheme of the code for better readability.
B) It acts as a global synchronization for processes.
C) It is used to create a new type of process.
D) It is used to delete old processes from the code.
**Answer:** B
---
**6. In ProVerif, how can you define a macro for security assumptions on primitives?**
A) By writing macro name(i1, ..., in) = declarations.
B) By using the def name(i1, ..., in) { declarations } syntax.
C) By using a "security - macro" keyword followed by the name and declarations.
D) It is not possible to define such macros.
**Answer:** B
---
**7. What does the macro expansion of name(a1, ..., an) do when name is defined using the def syntax in ProVerif?**
A) It creates a new macro with the arguments a1, ..., an.
B) It expands to the declarations inside def with a1, ..., an substituted for i1, ..., in.
C) It deletes the macro definition from the code.
D) It prints the values of a1, ..., an.
**Answer:** B
---
**8. In ProVerif, when using the phase construct, what happens when phase 1 starts?**
A) All processes continue running as normal.
B) All processes that did not reach a phase n construct with n ≥ 1 are discarded, and processes that start with phase 1 run.
C) All processes are paused until the user manually resumes them.
D) All processes are deleted from the code.
**Answer:** B
---
**9. What is the advantage of using process macros in ProVerif?**
A) They make the code run faster.
B) They are only an encoding useful for development and can be expanded in the main process.
C) They change the programming language used by ProVerif.
D) They are required for all protocols in ProVerif.
**Answer:** B
---
**10. ProVerif uses an abstract representation of protocols by Horn clauses. What is an advantage of this approach?**
A) It guarantees termination in all cases.
B) It is more precise than tree - automata because it keeps relational information on messages.
C) It makes the code easier to write without any rules.
D) It allows for the use of any programming language within ProVerif.
**Answer:** B
---