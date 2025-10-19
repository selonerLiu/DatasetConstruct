# topic：Comments & Whitespace: Syntax for comments in ProVerif. Roles of spaces, tabs, and newline characters in the language.

---
**1. In ProVerif, which of the following is used to start a single-line comment?**  
A) /*  
B) //  
C) #  
D) --  
**Answer:** C

---
**2. How does ProVerif treat multiple spaces, tabs, or newlines between tokens in its input language?**  
A) They change the meaning of the code significantly.  
B) They are ignored and treated as whitespace.  
C) Tabs are allowed but spaces are not.  
D) Newlines terminate statements like in some programming languages.  
**Answer:** B

---
**3. What is the primary role of whitespace (spaces, tabs, newlines) in ProVerif scripts?**  
A) To separate tokens and improve readability without affecting semantics.  
B) To indent code blocks and define scope.  
C) To indicate line breaks that terminate statements.  
D) To mark comments in the code.  
**Answer:** A

---
**4. Which of the following best describes multiline comments in ProVerif?**  
A) Enclosed between /* and */  
B) Enclosed between <!-- and -->  
C) ProVerif supports only single-line comments starting with #  
D) Enclosed between /** and **/  
**Answer:** C

---
**5. If a syntax error occurs at a certain character position, how does ProVerif help the user locate it?**  
A) ProVerif fixes the error automatically.  
B) It provides the line and column number of the error.  
C) It prints the entire file with error highlights.  
D) It only shows a generic error message without location.  
**Answer:** B

---
**6. In ProVerif, can identifiers be separated by any amount of whitespace including multiple newlines?**  
A) No, only a single space is allowed between tokens.  
B) Yes, any number of spaces, tabs, or newlines can separate tokens.  
C) Only newlines but not tabs are allowed between tokens.  
D) Tokens must be adjacent without any whitespace.  
**Answer:** B

---
**7. Regarding line continuation, how does ProVerif interpret a process declaration that spans multiple lines?**  
A) It treats each line as a separate statement unless terminated by a semicolon.  
B) Whitespace allows statements to continue over multiple lines without special characters.  
C) Newlines must be escaped with backslashes to continue lines.  
D) Statements cannot span multiple lines in ProVerif.  
**Answer:** B

---
**8. Why is it important to use whitespace correctly in ProVerif models?**  
A) Because incorrect whitespace can cause runtime errors during protocol execution.  
B) Because ProVerif uses whitespace to infer data types.  
C) Because whitespace separates tokens; incorrect spacing can cause syntax errors.  
D) Whitespace is not important at all in ProVerif.  
**Answer:** C

---
**9. Which of the following is NOT a reserved keyword in ProVerif and thus can be used as an identifier?**  
A) new  
B) if  
C) channel  
D) handshake  
**Answer:** D

---
**10. How does ProVerif treat tabs within the source code?**  
A) Tabs are converted automatically to spaces and are treated as whitespace.  
B) Tabs cause errors and must be avoided.  
C) Tabs indicate block indentation and affect parsing.  
D) Tabs are ignored completely and stripped from input.  
**Answer:** A

---