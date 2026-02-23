# Week 10 — Hash Tables and Set Data Structures

## Overview
- **Learning Objectives**:
  - Understand the concept of hashing: mapping arbitrary-sized keys to fixed-size indices
  - Analyze hash functions and the properties of a good hash function (deterministic, uniform distribution)
  - Understand hash collisions and why they are inevitable (pigeonhole principle)
  - Learn collision resolution strategies: separate chaining (open hashing) and open addressing (closed hashing)
  - Distinguish open addressing variants: linear probing, quadratic probing, double hashing
  - Understand load factor, its impact on performance, and the rehashing mechanism
  - Analyze average-case O(1) time complexity for hash table operations
  - Recognize hash-based data structures in practice: sets and maps (dictionaries)
- **Textbook**: CLRS 3rd Edition, Chapter 11
- **Quiz**: Quiz 7 (covers Week 09 content: Search Trees — BST, Red-Black Tree, B-Tree) at the START of the 1st hour (~15 min)
- **Homework**: None

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 7** (covers Week 09: Search Trees — BST, Red-Black Tree, B-Tree)
- [00:15–00:25] Hash concept: mapping keys to indices, hash function definition, key-value storage
- [00:25–00:35] Hash function examples: division method (h(k) = k mod m), multiplication method; properties of good hash functions
- [00:35–00:45] Hash collision: why it occurs, pigeonhole principle, collision resolution overview
- [00:45–00:50] Separate chaining: concept, linked list per bucket, insertion/search/deletion walkthrough
- Slides: `theory/10_hash_tables_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:10] Separate chaining: complexity analysis under simple uniform hashing assumption
- [00:10–00:25] Open addressing: linear probing (step-by-step), quadratic probing, double hashing
  - Clustering problem in linear probing, advantages of double hashing
- [00:25–00:35] Load factor (alpha = n/m): definition, impact on expected chain length, performance thresholds
- [00:35–00:42] Rehashing: when and how to resize, amortized O(1) cost
- [00:42–00:48] Hash-based data structures: Set and Map (Dictionary), average O(1) operations, real-world usage
- [00:48–00:50] Summary and comparison: hash table vs BST vs sorted array
- Slides: `theory/10_hash_tables_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **알고리즘 실습** (25분)
  - [00:00–00:15] Chaining 해시 테이블 구현
  - [00:15–00:25] Open Addressing (Linear Probing) 구현
- **프로젝트 작업** (25분)
  - [00:25–00:40] 프로젝트에 해시 기반 기능 추가 (캐싱, 빠른 조회 등)
  - [00:40–00:50] 해시 적용 전후 성능 비교 측정
- Guide: `lab/README.md`
- **프로젝트 마일스톤**: 해시 테이블 활용 기능 추가

## Materials
- Theory: `theory/10_hash_tables_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: None
- Quiz: Quiz 7 (Week 09 content — Search Trees)
