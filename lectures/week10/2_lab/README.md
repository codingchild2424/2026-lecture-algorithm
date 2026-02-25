# Week 10 Lab — Hash Tables + Project

## Objectives
- Implement two collision resolution strategies for hash tables.
- Add hash-based features to the project.

---

## Algorithm Exercises (25 min)

### Ex 1: Chaining Hash Table (15 min)
Refer to `examples/hash_chaining.py` and implement a hash table using the chaining method.

### Ex 2: Open Addressing (10 min)
Refer to `examples/hash_probing.py` and implement the linear probing method.

---

## Project Demo: Hash Table Explorer (10 min)

Run the reference project to see hash tables in action:
```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```
Explore: hash table visualization, collision resolution comparison, phone book app, and performance benchmarks.

---

## Project Work (15 min)

### Proj 1: Add Hash-Based Features (10 min)
Add features to your project that utilize hash tables:
- Shopping Mall: Fast product lookup by product ID, shopping cart caching
- Social Network: User ID mapping, session management
- Campus Map: Building name to coordinate mapping

### Proj 2: Performance Comparison (5 min)
Measure and record the performance of sequential list search vs. hash table lookup in your project.

**Milestone**: Hash table feature integration complete
