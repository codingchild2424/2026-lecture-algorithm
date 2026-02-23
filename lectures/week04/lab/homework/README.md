# Homework 3 — 분할 정복 곱셈

## 목표
Karatsuba 곱셈을 구현하고, 일반 곱셈과 성능을 비교한다.

## 문제

### Part 1: Karatsuba 곱셈 (60점)
`skeleton/solution.py`의 `karatsuba(x, y)` 함수를 구현하세요.

### Part 2: 성능 비교 (40점)
`benchmark()` 함수에서 일반 곱셈 vs Karatsuba 곱셈의 성능을 비교하세요.

## 힌트
Karatsuba: x*y = z2 * 10^(2m) + z1 * 10^m + z0
- z0 = low(x) * low(y)
- z2 = high(x) * high(y)
- z1 = (low(x)+high(x)) * (low(y)+high(y)) - z0 - z2
