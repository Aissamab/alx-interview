# Box Unlocking Problem

## Description
This project provides a method to determine if all boxes in a given set can be opened. Each box is sequentially numbered from 0 to \( n - 1 \) and may contain keys to other boxes. The goal is to check if all the boxes can be unlocked given the initial conditions.

## Problem Statement
You are given `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to \( n - 1 \), and each box may contain keys to other boxes. The keys are represented as positive integers that correspond to the box numbers they can open.

### Conditions:
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not correspond to any box.
- The first box `boxes[0]` is initially unlocked.

### Task:
Write a method that determines if all the boxes can be opened.

## Method Prototype
```python
def canUnlockAll(boxes):

