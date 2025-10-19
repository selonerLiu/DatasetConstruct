# topic：Declaration of Functions and Destructors: Definition methods，Roles in the system, Introduction mechanisms.

---
**1. How are function symbols declared in the given syntax?**
A) Function symbols are declared without any types.
B) Function symbols are declared with types, e.g., h(T1,...,Tn) : T.
C) Only constructors are declared with types, destructors are not.
D) Function symbols are declared with only one type, regardless of the number of arguments.
**Answer:** B
---
**2. What is the role of destructor function symbols in the system?**
A) Destructor function symbols can only create new terms.
B) Destructor function symbols can manipulate terms and are defined by rewrite rules.
C) Destructor function symbols have no specific role and can be used interchangeably with constructors.
D) Destructor function symbols can only be used in the main process.
**Answer:** B
---
**3. How are free names declared in an input file?**
A) Free names are declared using the syntax “name n : t”.
B) Free names are declared using the syntax “free n : t”, where n is a name and t is its type.
C) Free names are declared without specifying their types.
D) Free names do not need to be declared in the input file.
**Answer:** B
---
**4. What does a constant in the system refer to?**
A) A constant is a variable that never changes its value.
B) A constant can be defined as a function of arity 0, e.g., “fun c() : t” or “const c : t”.
C) A constant is a special type of constructor.
D) A constant is a term that contains only destructor function symbols.
**Answer:** B
---
**5. How are destructors defined in the “reduc” declaration?**
A) Destructors are defined as simple functions without any rules.
B) Destructors are defined by an ordered list of rewrite rules of the form forall x1,1 : t1,1, ..., x1,n1 : t1,n1 ; g(M1,1, ..., M1,k) = M1,0.
C) Destructors are defined by a single rule that applies to all cases.
D) Destructors in the “reduc” declaration are the same as normal destructors and do not have special rules.
**Answer:** B
---
**6. What happens if no rewrite rule can be applied to a destructor function?**
A) The destructor creates a new term randomly.
B) The destructor fails.
C) The system uses a default rewrite rule.
D) The destructor is treated as a constructor.
**Answer:** B
---
**7. What are terms in the system?**
A) Terms can only be variables.
B) Terms can be a variable, a name, or the application of a constructor function symbol to terms.
C) Terms can only be names representing atomic data.
D) Terms can only be the result of a destructor operation.
**Answer:** B
---
**8. Which of the following is a built - in constructor in the system?**
A) not
B) true
C) ||
D) -k for each k natural number
**Answer:** B
---
**9. How does the “reduc” declaration for destructors differ from the basic destructor definition in Section 3.1.1?**
A) There is no difference between the two definitions.
B) The “reduc” declaration allows for the definition of new destructors that could not be defined in Section 3.1.1.
C) The “reduc” declaration only applies to constructors, not destructors.
D) The “reduc” declaration uses a different syntax but has the same functionality as the basic definition.
**Answer:** B
---
**10. What does it mean when a destructor is defined by an ordered list of rewrite rules?**
A) All rewrite rules are applied simultaneously to a destructor operation.
B) ProVerif tries the rewrite rules in the sequence one by one, and if a rule is applicable, the term is reduced according to that rule.
C) Only the first rewrite rule in the list is ever considered.
D) Rewrite rules for destructors are randomly selected for application.
**Answer:** B
---