# topic：Declaration of Types, Variables, and Constants: Definition methods，Roles in the system, Introduction mechanisms.

---
**1. In ProVerif, how is a constant defined in terms of arity and declaration syntax?**  
A) A constant is a function of arity 1 and declared using `fun c(t) : t.`  
B) A constant is a function of arity 0 and declared using `fun c() : t.`  
C) A constant is declared only by `const c : t .` without involving functions.  
D) A constant must be declared as a free name using `free c : t .`  
**Answer:** B

---

**2. What role do names such as a, b, c, and k play in the ProVerif modeling language?**  
A) They represent variables that can be substituted by terms.  
B) They represent atomic data such as keys and nonces.  
C) They are only used as types in function declarations.  
D) They are channels used for communication between processes.  
**Answer:** B

---

**3. Which of the following correctly describes the difference between names and variables in ProVerif?**  
A) Names and variables are interchangeable and can be substituted freely.  
B) Names represent atomic data and cannot be substituted, whereas variables can be substituted by terms.  
C) Variables represent atomic data, and names are substituted by terms.  
D) Both are declared without types and function symbols.  
**Answer:** B

---

**4. How are types declared in ProVerif?**  
A) They are declared using `var t.`  
B) They are declared using `free t : type.`  
C) They are declared using `type t .`  
D) They are declared implicitly when variables or names are declared.  
**Answer:** C

---

**5. Which construct is used to declare a free name in ProVerif, and what is its syntax?**  
A) `const n : t .` where n is a constant name.  
B) `free n : t .` where n is a free name of type t.  
C) `fun n() : t .` defining a function with zero arity.  
D) `letfun n = t .` which defines a let function.  
**Answer:** B

---

**6. What does the function symbol declaration `h(T1,...,Tn) : T` mean in ProVerif?**  
A) `h` is a constant symbol with type T.  
B) `h` is a function taking n arguments where each has types T1 to Tn, returning type T.  
C) `h` is a variable that can hold any of the types T1 to Tn.  
D) `h` is a destructor that breaks down types T into T1 to Tn.  
**Answer:** B

---

**7. Which of the following statements about free names in an input file is TRUE?**  
A) Free names do not require declaration before use.  
B) Multiple free names of the same type can be declared in a single `free` declaration.  
C) Free names can only be used as function parameters.  
D) Free names represent destructors in the language.  
**Answer:** B

---

**8. What is discouraged by the authors regarding the use of built-in identifiers like `true`, `false`, `attacker` in ProVerif?**  
A) Modifying their definitions to suit protocol needs.  
B) Declaring them as constants.  
C) Reusing these built-in identifiers as user-defined identifiers.  
D) Using them as function names only.  
**Answer:** C

---

**9. What is the primary purpose of constructors and destructors in ProVerif's function symbols?**  
A) Constructors build complex data from simpler ones; destructors extract components from data.  
B) Both constructors and destructors are used only for variable substitution.  
C) Destructors create new types; constructors delete them.  
D) They are placeholders for types and have no computational semantics.  
**Answer:** A

---

**10. According to the grammar for declarations, which of the following is NOT a valid declaration form?**  
A) `free seq+⟨ident⟩: ⟨typeid⟩ ⟨options⟩.`  
B) `const seq+⟨ident⟩: ⟨typeid⟩ ⟨options⟩.`  
C) `fun ⟨ident⟩(seq⟨typeid⟩): ⟨typeid⟩ ⟨options⟩.`  
D) `newtype ⟨ident⟩ : ⟨typeid⟩.`  
**Answer:** D

---