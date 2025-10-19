# topic：Identifiers: Specifications for constructing variable/function names: Character set, First-character rules, Length restrictions, Keyword reservation policies, and so on.

---
**1. What is the rule for the first character of an identifier in the described language?**
A) It can be any character from the ISO Latin 1 character set.
B) It must be a digit.
C) It must be a letter.
D) It can be an underscore.
**Answer:** C
---
**2. Which of the following character sets are allowed in identifiers?**
A) Only letters (a - z, A - Z) and digits (0 - 9).
B) Letters (a - z, A - Z), digits (0 - 9), underscores, single - quotes, and accented letters from the ISO Latin 1 character set.
C) Only letters (a - z, A - Z) and underscores.
D) Letters (a - z, A - Z), digits (0 - 9), and special symbols like @ and #.
**Answer:** B
---
**3. What is the policy regarding reserved words and identifiers?**
A) Reserved words can be used as identifiers if they are in lowercase.
B) Reserved words cannot be used as identifiers.
C) Reserved words can be used as identifiers if they are part of a longer name.
D) There is no policy regarding reserved words and identifiers.
**Answer:** B
---
**4. Are there any length restrictions for identifiers?**
A) Identifiers must be at least 3 characters long.
B) Identifiers must be at most 10 characters long.
C) The text does not mention any length restrictions, so identifiers can be of an unlimited length.
D) Identifiers must be exactly 5 characters long.
**Answer:** C
---
**5. Can an identifier start with a single - quote?**
A) Yes, as long as the rest of the characters are valid.
B) No, the first character of an identifier must be a letter.
C) It depends on whether it is a variable or a function identifier.
D) Yes, but only for function identifiers.
**Answer:** B
---
**6. In the context of identifiers, are identifiers case - sensitive?**
A) No, all identifiers are treated the same regardless of case.
B) Yes, identifiers are case - sensitive.
C) Only function identifiers are case - sensitive.
D) Only variable identifiers are case - sensitive.
**Answer:** B
---
**7. Which of the following is a valid identifier according to the given rules?**
A) among (a reserved word)
B) 1abc (starts with a digit)
C) 'abc (starts with a single - quote)
D) validName
**Answer:** D
---
**8. If a user wants to use a word that is similar to a reserved word but not exactly the same, can it be used as an identifier?**
A) No, any word close to a reserved word cannot be used.
B) Yes, as long as it is distinct from the reserved words and follows the other identifier rules.
C) It can only be used if it is a variable identifier.
D) It can only be used if it is a function identifier.
**Answer:** B
---
**9. Can a reserved word be used as an identifier if it is in a comment?**
A) No, it is still not allowed even in a comment.
B) Yes, reserved words can be used freely in comments.
C) It depends on the type of comment (single - line or multi - line).
D) Only some reserved words can be used in comments.
**Answer:** B
---
**10. If an identifier contains an accented letter from the ISO Latin 1 character set, is it still valid?**
A) No, accented letters are not allowed in identifiers.
B) Yes, as long as it follows the other rules like starting with a letter and being distinct from reserved words.
C) It is only valid for variable identifiers.
D) It is only valid for function identifiers.
**Answer:** B
---