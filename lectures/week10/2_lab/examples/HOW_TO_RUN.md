# Week 10 Lab - Hash Tables

## Exercises

### Ex 1: Hash Table with Chaining (`ex1_hash_chaining.py`)
Implement a hash table that resolves collisions using chaining (linked lists per bucket).
You need to implement the `put()`, `get()`, and `delete()` methods.

### Ex 2: Hash Table with Linear Probing (`ex2_hash_probing.py`)
Implement a hash table that resolves collisions using linear probing (open addressing).
You need to implement the `put()` and `get()` methods.

## How to Run

```bash
python ex1_hash_chaining.py
python ex2_hash_probing.py
```

## Expected Output

- **Ex 1**: Inserts key-value pairs, prints load factor after each insert, searches for existing/non-existing keys, and displays the internal bucket structure showing chains.
- **Ex 2**: Inserts key-value pairs, prints load factor after each insert, searches for a key, and displays the internal table showing how linear probing distributes items.

## Solutions

Complete reference implementations are available in the `solutions/` subdirectory.
