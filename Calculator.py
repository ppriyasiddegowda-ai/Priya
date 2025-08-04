# Calculator using Functions, Loops, and Conditionals

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Welcome to CLI Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Thanks for using the calculator. Bye!")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Try again.")
        continue

    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))







1. What is normalization?

Normalization is a process in database design that organizes data to reduce data redundancy and improve data integrity. It involves dividing large tables into smaller ones and defining relationships between them using rules called normal forms (1NF, 2NF, 3NF, etc.).




2. Explain primary vs foreign key.

Key Type	Description

Primary Key	Uniquely identifies each row in a table. Cannot be null.
Foreign Key	A field in one table that refers to the primary key of another table. Used to maintain referential integrity.





3. What are constraints?

Constraints are rules applied to table columns to enforce data integrity. Common types:

NOT NULL – Value cannot be NULL.

UNIQUE – All values must be unique.

PRIMARY KEY – Uniquely identifies records.

FOREIGN KEY – Ensures referential integrity.

CHECK – Ensures values meet a condition.

DEFAULT – Sets a default value.





4. What is a surrogate key?

A surrogate key is a system-generated unique identifier (like an auto-incremented number) used as the primary key when no natural key is suitable. It has no business meaning.




5. How do you avoid data redundancy?

Use normalization to structure data properly.

Create separate tables for repeating groups.

Use foreign keys to reference related data.

Design with clear relationships and constraints.





6. What is ER diagram?

An ER (Entity-Relationship) diagram is a visual representation of the entities in a database and the relationships between them. It helps in designing a logical database structure.




7. What are the types of relationships in DBMS?

One-to-One (1:1) – Each record in Table A relates to one in Table B.

One-to-Many (1:N) – One record in Table A relates to many in Table B.

Many-to-Many (M:N) – Records in both tables relate to multiple records in the other.





8. Explain the purpose of AUTO_INCREMENT.

AUTO_INCREMENT is used to automatically generate unique values for a column (usually the primary key) when a new record is inserted.

Example:

id INT AUTO_INCREMENT PRIMARY KEY




9. What is the default storage engine in MySQL?

The default storage engine in MySQL is InnoDB, which supports:

ACID compliance

Transactions

Foreign keys

Row-level locking





10. What is a composite key?

A composite key is a combination of two or more columns used together to uniquely identify a row in a table when a single column is not sufficient.

Example:

PRIMARY KEY (student_id, course_id)




