# Loops

---

## What is `Loop`:

Loops allow you to repeat a block of code multiple times, which is useful for tasks that need to be done over and over.
There are two common types of loops in Python: `while` loops and `for` loops.

## `while` Loop

A while loop runs as long as a certain condition is True.
The condition is checked before each iteration, and if it’s still True, the loop will continue.
If the condition becomes False, the loop stops.

### Example:

```python
count = 0

while count < 5:
    print("This is loop iteration: ", count)
    count += 1  # Increment the count to avoid an infinite loop
```

In this example:

- The loop starts with count = 0 and prints the message.
- After each iteration, count is incremented.
- The loop stops when count reaches 5 because the condition count < 5 becomes False.

## `for` Loop

A for loop iterates over a sequence, such as a list, tuple, or a range of numbers.
It automatically goes through each item in the sequence and executes the code block.

### Example

```python
for i in range(5):
    print("This is loop iteration: ", i)
```

In this example:
- The range(5) generates numbers from 0 to 4.
- The loop runs 5 times, printing the iteration number on each pass.

## Summary:

- while loop: Repeats as long as a condition is True.
- for loop: Iterates over a sequence of values (e.g., list or range).

Both loops help make your code more efficient when you need to repeat actions multiple times.