# Control Flow

---

## Making Decisions Based on Situations

Control flow in programming refers to the order in which a program’s instructions are executed.

Instead of always running code from top to bottom, control flow allows a program to make decisions, repeat actions, or choose different paths based on conditions.

This is what makes programs flexible and intelligent.

### `if` statement 

An `if` statement runs a block of code only if a condition is true.

```python
# The message prints only when score is 50 or higher.
if score >= 50:
    print("You passed")
```

### `else` statement

An `if-else` statement gives two possible paths: 
one when the condition is true, and another when it’s false.

```python
if score >= 50:
    print("You passed")
else:
    print("You failed"
```

### `elif` statement

The elif (else if) statement works like if, but it allows you to check multiple conditions in sequence.

```python
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C or below")
```

### `match-case`

`match-case` is used to compare one value against many possible patterns, similar to a switch statement in other languages.

```python
day = "Monday"

match day:
    # Executed if day is Monday
    case "Monday":
        print("Start of the week")
    # Executed if day is Friday
    case "Friday":
        print("Almost weekend")
    # Executed if non of above options are True
    case _:
        print("Another day")
```
