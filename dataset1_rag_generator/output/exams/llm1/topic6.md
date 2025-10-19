# topic：Delimiters: Symbols for separating/grouping structural elements (e.g., (), [], {}, ., ;): Semantic interpretations, Usage rules.

---
**1. In the grammar described, which of the following characters can the first character of an identifier ⟨ident⟩ be?**  
A) Digit (0-9)  
B) Underscore (_)  
C) A letter (a-z, A-Z)  
D) Single-quote (’)  
**Answer:** C  
---

**2. According to the provided grammar, which of the following is *not* allowed inside an identifier ⟨ident⟩ after the first character?**  
A) Accented letters from the ISO Latin 1 character set  
B) Digits (0-9)  
C) Reserved words of the language  
D) Underscores (_)  
**Answer:** C  
---

**3. What kind of comment syntax does the described language support?**  
A) Single line comments starting with //  
B) Comments surrounded by (* and *), with support for nested comments  
C) Block comments with /* and */, no nesting  
D) Comments starting with # until the end of the line  
**Answer:** B  
---

**4. Which symbol set correctly represents the precedences of infix operators from low to high in the grammar?**  
A) &&, ||, =, <>, <=, >=, <, >, +, -  
B) ||, &&, =, <>, <=, >=, <, >, +, -  
C) =, ||, &&, <>, <=, >=, <, >, +, -  
D) ||, &&, <>, =, <=, >=, <, >, +, -  
**Answer:** B  
---

**5. In the grammar, what is the associativity of the + and - operators?**  
A) Right associative  
B) Left associative  
C) Non-associative  
D) Both left and right associative depending on context  
**Answer:** B  
---

**6. According to the grammar rules, which function symbols are *disallowed* in reduc and equation declarations after parsing?**  
A) Constructors such as f, g, h  
B) Logical operators like ||, &&, =, <>, <=, >=, <, >, - and not  
C) Names representing atomic data such as keys and nonces  
D) Variables substituted by terms  
**Answer:** B  
---

**7. What do the delimiters {{ and }} represent in the structural grammar of processes?**  
A) They mark the start and end of sequences in terms.  
B) They denote sets or multisets of processes.  
C) They group function symbols for application.  
D) They separate elements inside an identifier.  
**Answer:** B  
---

**8. In the process grammar, which inference rule corresponds to restricting a name in the environment, i.e., binding a new name?**  
A) (PAR) E,P∪{{P |Q}},A− → E,P∪{{P,Q}},A  
B) (REPL) E,P∪{{!P}},A− → E,P∪{{P,!P}},A  
C) (RESTR) E,P∪{{new a; P}},A− → E∪{a′},P∪{{P{a′/a}}},A if a′̸∈E  
D) (I/O) E,P∪{{out(N,M); P,in(N,x); Q}},A → …  
**Answer:** C  
---

**9. How are variables and names differentiated in the grammar regarding their roles?**  
A) Variables range over names, and names range over variables.  
B) Names represent atomic data such as keys/nonces; variables can be substituted by terms.  
C) Both variables and names are interchangeable in declarations.  
D) Variables represent atomic data, and names can be substituted by terms.  
**Answer:** B  
---

**10. Which of the following delimiters are used for grouping optional sequences of identifiers as options in the grammar?**  
A) ()  
B) []  
C) {{}}  
D) ;;  
**Answer:** B  
---