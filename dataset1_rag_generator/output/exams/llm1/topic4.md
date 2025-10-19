# topic：Keywords: Character sequences with special syntactic meaning (e.g., if, event, function, free), including their semantic roles.

---
**1. In the described grammar, what is a key restriction on the first character of an identifier?**  
A) It can be any symbol or digit.  
B) It must be a letter.  
C) It must be a digit.  
D) It must be a reserved word.  
**Answer:** B

---
**2. Which of the following is NOT allowed as an identifier in the given formalism?**  
A) `data1`  
B) `_private`  
C) `channel` (as an identifier)  
D) `if`  
**Answer:** D

---
**3. What does the non-terminal ⟨nat⟩ represent in this grammar?**  
A) Integer numbers including negative values.  
B) Natural numbers (non-negative integers).  
C) Floating-point numbers.  
D) Identifiers starting with a digit.  
**Answer:** B

---
**4. Which of the following best describes ⟨typeid⟩ in the formalism?**  
A) It only represents reserved words.  
B) It represents types denoted by identifiers or the reserved word `channel`.  
C) It denotes numeric types only.  
D) It represents any keyword or identifier.  
**Answer:** B

---
**5. Given the precedence rules in the grammar, which operator has the lowest precedence?**  
A) ==>  
B) +  
C) &&  
D) ||  
**Answer:** A

---
**6. In the formal syntax, how are sequences of identifiers (seq+⟨ident⟩) defined?**  
A) Zero or more identifiers separated by spaces.  
B) One or more identifiers separated by commas.  
C) Exactly one identifier.  
D) Identifiers separated by semicolons.  
**Answer:** B

---
**7. What is the semantic role of the reserved word `event` in this context?**  
A) Declaring a new type.  
B) Defining events with associated parameters and optional annotations.  
C) Defining private data.  
D) Creating conditional branches in processes.  
**Answer:** B

---
**8. Which of the following choices correctly describes the form of a pattern (⟨pattern⟩)?**  
A) Only identifiers without type annotations.  
B) Identifiers optionally annotated with types, natural numbers, or combinations thereof.  
C) Identifiers starting with digits only.  
D) Only type identifiers enclosed in brackets.  
**Answer:** B

---
**9. Which of the following is an example of a valid ⟨gbinding⟩ declaration?**  
A) `123 = someTerm;`  
B) `!42 = someTerm; ident = anotherTerm`  
C) `function name = call`  
D) `channel = someValue`  
**Answer:** B

---
**10. What does a lemma typically include according to the given formalism?**  
A) Only conditional statements.  
B) Only function definitions.  
C) One or more guarded terms possibly qualified by public or secret variable declarations.  
D) Reserved words redefined as identifiers.  
**Answer:** C

---