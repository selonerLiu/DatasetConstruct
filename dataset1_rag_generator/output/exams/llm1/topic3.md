# topic：Identifiers: Specifications for constructing variable/function names: Character set, First-character rules, Length restrictions, Keyword reservation policies, and so on.

---
**1. Which of the following statements accurately describes the first character rule for identifiers in the given specification?**  
A) The first character can be any digit or letter.  
B) The first character must always be a letter.  
C) The first character can be a letter or underscore.  
D) The first character can be any ASCII character except reserved words.  
**Answer:** B  

---
**2. In the identifier specification provided, what characters are allowed after the first character?**  
A) Only letters (a-z, A-Z)  
B) Letters and digits only  
C) Letters, digits, underscores (_), single-quotes ('), and accented letters from ISO Latin 1  
D) Letters, digits, underscores (_), and spaces  
**Answer:** C  

---
**3. Which of the following is true about the case sensitivity of identifiers according to the content?**  
A) Identifiers are case-insensitive (e.g., ‘Var’ and ‘var’ are the same).  
B) Identifiers must be all lowercase.  
C) Identifiers are case-sensitive (e.g., ‘Var’ and ‘var’ are different).  
D) Identifiers must be all uppercase.  
**Answer:** C  

---
**4. Which of the following is NOT allowed as an identifier because it is a reserved keyword?**  
A) process  
B) private  
C) myVar  
D) alpha123  
**Answer:** A  

---
**5. Why is it important that identifiers do not match any reserved words in the language?**  
A) To allow their use both as functions and variables simultaneously.  
B) To avoid ambiguity and parsing errors during compilation or interpretation.  
C) To enable easier human readability.  
D) Because reserved words can only be lowercase identifiers.  
**Answer:** B  

---
**6. Which character set forms the basis for all valid identifiers in this formalism?**  
A) Unicode characters only  
B) ASCII characters with additional accented letters from ISO Latin 1  
C) Digits and symbols only  
D) Only English alphabet letters (A-Z, a-z)  
**Answer:** B  

---
**7. According to the description, which of these could serve as a valid identifier?**  
A) '_myVar' (underscore as first character)  
B) '1stVar' (starts with a digit)  
C) 'var_123’ (letter first, followed by underscore and digits)  
D) 'for' (reserved keyword)  
**Answer:** C  

---
**8. When names and variables are declared, what additional information accompanies their identifier?**  
A) Their value  
B) Their type  
C) Their length  
D) Their scope  
**Answer:** B  

---
**9. Which of the following best summarizes the restrictions on identifier naming?**  
A) Identifiers must start with a digit and contain only letters and digits.  
B) Identifiers can start with any character but must be unique.  
C) Identifiers must start with a letter, may contain letters, digits, certain symbols, and must not be reserved words.  
D) Identifiers must be a sequence of digits only.  
**Answer:** C  

---
**10. Why do the authors discourage reusing built-in identifiers such as ‘bool’, ‘attacker’, or ‘message’ as user identifiers?**  
A) Because they will cause performance issues.  
B) Because this practice may lead to confusion or errors in proofs and outputs.  
C) Because these names are deprecated and not recognized.  
D) Because reserved keywords can only be reused in specific modules.  
**Answer:** B  

---