# topic：Delimiters: Symbols for separating/grouping structural elements (e.g., (), [], {}, ., ;): Semantic interpretations, Usage rules.

---
**1. In the given content, which symbols are used for separating or grouping structural elements?**
A) +, -, *
B) (), [], {}, ., ;
C) &&, ||, =
D) <, >, <=, >=
**Answer:** B
---
**2. For the sequence construction seq+⟨X ⟩, which delimiter is used to separate elements in the sequence?**
A) :
B) ;
C) ,
D) *
**Answer:** C
---
**3. In the declaration ⟨gbinding⟩ ::= !⟨nat⟩ = ⟨gterm⟩ [; ⟨gbinding⟩], what is the delimiter used to separate multiple ⟨gbinding⟩ elements?**
A) .
B) ;
C) ,
D) :
**Answer:** B
---
**4. In the construction [ [seq+⟨ident⟩]], what is the main purpose of the square - brackets []?**
A) To denote multiplication
B) To separate the sequence from other elements
C) To group the sequence of identifiers
D) To indicate a negative value
**Answer:** C
---
**5. In the rule E,P∪{{out(N,M); P,in(N,x); Q}},A msg(N,M) −−−−−−−→E,P∪{{P,Q{M/x}}},A, what is the role of the semicolon ; in out(N,M); P and in(N,x); Q?**
A) It is used for multiplication
B) It separates different actions in the process
C) It indicates a conditional statement
D) It is used for logical AND operation
**Answer:** B
---
**6. In the grammar ⟨failtypedecl⟩ ::= seq+⟨ident⟩: ⟨typeid⟩[or fail][,⟨failtypedecl⟩], what does the comma , do?**
A) It is used for logical OR operation
B) It separates multiple ⟨failtypedecl⟩ declarations
C) It is used for arithmetic addition
D) It indicates a function call
**Answer:** B
---
**7. In the syntax [ [seq+⟨ident⟩]], if we want to add another identifier to the sequence, what delimiter should we use between the identifiers?**
A) :
B) ;
C) ,
D) *
**Answer:** C
---
**8. In the rule E,P∪{{new a; P}},A− →E∪{a′},P∪{{P{a′ /a}}},A, what is the function of the semicolon ; in new a; P?**
A) It is used to indicate a logical AND operation
B) It separates the new declaration from the following process
C) It is used for arithmetic subtraction
D) It indicates a loop
**Answer:** B
---
**9. In the construction let ⟨ident⟩ = ⟨gterm⟩ in ⟨gterm⟩, what is the role of the keyword in?**
A) It is a delimiter that separates the assignment part from the expression where the assigned value is used
B) It is used for logical OR operation
C) It is used for arithmetic multiplication
D) It indicates a conditional statement
**Answer:** A
---
**10. In the grammar ⟨options⟩ ::= [ [seq+⟨ident⟩]], if the sequence has only one identifier, are the square - brackets [] still necessary?**
A) No, they are not necessary
B) Yes, they are used to group the single identifier
C) They are only necessary if the identifier is a reserved word
D) They are only necessary if the identifier is a number
**Answer:** B
---