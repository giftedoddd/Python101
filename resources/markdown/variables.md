# Variables and Data Types

---

## Initializing Variables and Understanding Data Types in Python

In programming, a **variable** is a named container used to store data that can change during the execution of a program.
Variables allow programmers to reference and manipulate values easily, making them essential for calculations and data management.

In Python we create a variable like this:

```python
apples = 5
```

This line creates a new variable in memory named `apples` and binds it to the value `5`.

In programming, we can assign any valid data type to a variable.

## Data Types

### In programming languages, data types are generally grouped into two categories:
1. Primitive Data Types:
    ```text
    Primitives are predefined data types numeric values or boolean values. 
   They are the most fundamental type and are used as the foundation for more complex data types.
    ``` 

2. Non-Primitive Data Types:
    ```text
   Non-primitive data types are made up of multiple primitive values.
   They are often user-defined and are also called composite data types.
    ```

We will talk about non-primitive data types later in this course

---

### Common Primitive Data Types in Python
* Integer (`int`): Whole numbers
   ```python
   x = 10
   ```

* Float (`float`): Decimal numbers
   ```python
   y = 10.5
   ```

* Boolean (`bool`): `True` or `False` values
   ```python 
   is_active = True
   ```

* String (`str`): A sequence of characters
   ```python
   # In Python, '' and "" are the same — both represent strings
   first_name = "Alice"
   last_name = 'Rice'
   
   long_sentence = """
   A
   long,
   multi-line
   sentence
   """
   ```

### Checking Data Types Using `type()`

Python provides a built-in function called `type()` that allows us to check the data type of a variable

```python
x = 24
y = 12.56472    
is_active = False  
name = "Brad"

print(type(x))      
print(type(y))     
print(type(is_active))  
print(type(name))
```

Output:
```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```

## But What Is a `Class`?:
Humans often build tools by copying ideas from nature—such as airplanes inspired by birds or cars inspired by animal movement.
In programming, Object-Oriented Programming (OOP) follows the same idea by modeling real-world objects using classes.

In the real world, everything we see or touch can be thought of as an object.

Every object has:
* a **shape or structure** (blueprint)
* a **behavior** (functionality)

```text
In programming, a class is a blueprint for creating objects.
It groups data (variables) and behavior (functions) that belong together.
```

For example:
* A `Car` class can describe:
  * what a car **has** (color, speed)
  * what a car **can do** (start, stop, accelerate)

The functions that belong to a class are called methods.
Methods define the actions an object can perform.