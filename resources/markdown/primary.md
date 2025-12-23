# Python101 Course

## Table of Contents
- [Hello World Project](#write-your-first-python-project)
- [Guessing Game Project](#programming-a-guessing-game)

# Write Your First Python Project

---

## Step-by-Step Progress

1. First, create a project directory. For now, let’s name it **`hello_world`**.
2. Give your project some structure by creating a template directory. In this case, create a **`src/`** directory.
3. Create your main project file inside the project directory. We’ll call it **`main.py`**.
4. Write the following source code in the file:

    ```python
    if __name__ == '__main__':
        print("Hello World!")
    ```

5. Run the program to check for any errors.
6. Congratulations! You just wrote your first Python program.

---

## The Anatomy of a Python Program

Let’s break down this **“Hello, World!”** program and understand what each part does.

---

### `if __name__ == '__main__':`

- This statement tells Python to run the code inside it **only when this file is executed directly**.
- If the file is imported into another Python file, this block will **not** run.
- This pattern helps you organize code and maintain better control as your project grows.

---

### Indentation

Before understanding indentation, we need to understand **code blocks**.

> A **code block** is a group of lines that are meant to run together.

- Python uses **indentation** to define code blocks.
- Indentation controls the **execution flow** of your program.
- Lines with the same level of indentation belong to the same block.

Incorrect indentation will cause errors, so consistency is very important in Python.

---

### `print("Hello World!")`

- The `print()` function is doing all the work in this simple program.
- We pass a value (called an **argument**) to the function.
- The function then displays that value on the screen.

In this case, it prints:
```text
Hello World!
```

---
