"""
알고리즘 패러다임 판별 연습

10개의 알고리즘 문제를 읽고, 각 문제에 적합한 패러다임을 판별하라.
패러다임: Brute Force / Divide & Conquer / Greedy / Dynamic Programming

먼저 문제만 읽고 각자 판별한 후, 아래의 해설을 확인한다.
"""


# ============================================================
#  문제 (Problems)
#  각 문제를 읽고, 어떤 패러다임을 사용할지 생각해 보세요.
# ============================================================

PROBLEMS = [
    {
        "id": 1,
        "title": "배열에서 두 수의 합",
        "description": """
정수 배열 nums와 정수 target이 주어진다.
배열에서 두 수를 골라 합이 target이 되는 모든 쌍을 찾아라.
배열의 크기는 최대 100이다.
""",
    },
    {
        "id": 2,
        "title": "최대 부분 배열 합 (Maximum Subarray Sum)",
        "description": """
정수 배열이 주어질 때, 연속 부분 배열의 합 중 최대값을 구하라.
예: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 답: 6 (부분 배열 [4, -1, 2, 1])
""",
    },
    {
        "id": 3,
        "title": "가장 가까운 두 점 (Closest Pair of Points)",
        "description": """
2차원 평면에 n개의 점이 주어진다.
유클리드 거리가 가장 가까운 두 점의 쌍을 찾아라.
n은 최대 100,000이다.
""",
    },
    {
        "id": 4,
        "title": "최소 동전 수 (Coin Change)",
        "description": """
동전의 종류 coins = [1, 5, 7, 10]과 금액 amount가 주어진다.
amount를 만들기 위한 최소 동전 수를 구하라.
""",
    },
    {
        "id": 5,
        "title": "활동 선택 (Activity Selection)",
        "description": """
n개의 활동이 시작 시간과 종료 시간으로 주어진다.
한 사람이 수행할 수 있는 활동의 최대 개수를 구하라.
(활동은 시간이 겹치지 않아야 한다.)
""",
    },
    {
        "id": 6,
        "title": "문자열 순열 검사",
        "description": """
두 문자열 s1, s2가 주어질 때,
s2가 s1의 순열(permutation)을 부분 문자열로 포함하는지 판별하라.
예: s1 = "ab", s2 = "eidbaooo" -> True ("ba"가 s1의 순열)
""",
    },
    {
        "id": 7,
        "title": "최장 증가 부분 수열 (LIS)",
        "description": """
정수 배열이 주어질 때, 가장 긴 증가하는 부분 수열의 길이를 구하라.
예: [10, 9, 2, 5, 3, 7, 101, 18] -> 답: 4 ([2, 3, 7, 101])
""",
    },
    {
        "id": 8,
        "title": "큰 수 곱셈 (Large Number Multiplication)",
        "description": """
매우 큰 두 정수(수천 자릿수)의 곱셈을 효율적으로 수행하라.
일반적인 곱셈은 O(n^2)이지만, 더 빠르게 할 수 있는가?
""",
    },
    {
        "id": 9,
        "title": "회의실 최소 개수",
        "description": """
n개의 회의가 시작 시간과 종료 시간으로 주어진다.
모든 회의를 배치하기 위해 필요한 최소 회의실 수를 구하라.
""",
    },
    {
        "id": 10,
        "title": "편집 거리 (Edit Distance)",
        "description": """
두 문자열 word1, word2가 주어진다.
word1을 word2로 변환하기 위한 최소 연산 수를 구하라.
가능한 연산: 삽입, 삭제, 교체 (각각 비용 1)
""",
    },
]


# ============================================================
#  해설 (Solutions)
# ============================================================

SOLUTIONS = [
    {
        "id": 1,
        "paradigm": "Brute Force",
        "explanation": """
배열 크기가 최대 100이므로 모든 쌍을 검사해도 O(n^2) = 10,000번으로 충분하다.
해시맵을 쓰면 O(n)도 가능하지만, 이 규모에서는 브루트포스도 적합하다.
핵심: 제약 조건(n <= 100)이 작으면 브루트포스를 먼저 고려한다.
""",
    },
    {
        "id": 2,
        "paradigm": "Dynamic Programming (또는 Divide & Conquer)",
        "explanation": """
DP 풀이 (Kadane's Algorithm):
  dp[i] = max(arr[i], dp[i-1] + arr[i])
  "i번째 원소에서 끝나는 최대 부분 배열 합"
  O(n) 시간, O(1) 공간.

분할정복 풀이도 가능:
  배열을 반으로 나눠 왼쪽/오른쪽/걸치는 경우 중 최대를 선택.
  O(n log n) 시간.

두 패러다임 모두 적용 가능하지만, DP가 더 효율적이다.
""",
    },
    {
        "id": 3,
        "paradigm": "Divide & Conquer",
        "explanation": """
대표적인 분할정복 문제.
  1. 점들을 x좌표 기준으로 정렬하고 반으로 나눈다
  2. 왼쪽/오른쪽 각각에서 최소 거리를 구한다
  3. 경계를 걸치는 경우를 O(n) 또는 O(n log n)으로 처리
  전체 O(n log n).

브루트포스는 O(n^2)이므로 n=100,000에서는 너무 느리다.
""",
    },
    {
        "id": 4,
        "paradigm": "Dynamic Programming",
        "explanation": """
동전이 [1, 5, 7, 10]처럼 배수 관계가 아니므로 그리디가 실패한다.
예: amount=14일 때 그리디는 10+1+1+1+1 = 5개, 최적은 7+7 = 2개.

DP 풀이:
  dp[i] = min(dp[i - coin] + 1) for each coin
  O(amount * k) 시간 (k = 동전 종류 수)

핵심: 그리디 선택 속성이 성립하지 않으면 DP를 사용한다.
""",
    },
    {
        "id": 5,
        "paradigm": "Greedy",
        "explanation": """
대표적인 그리디 문제 (Activity Selection).
  1. 종료 시간 기준으로 정렬
  2. 겹치지 않는 활동을 순서대로 선택
  O(n log n) 시간.

그리디 선택 속성이 증명되어 있다:
"종료 시간이 가장 빠른 활동을 선택하는 것이 항상 최적 해의 일부이다."
""",
    },
    {
        "id": 6,
        "paradigm": "Brute Force (슬라이딩 윈도우)",
        "explanation": """
슬라이딩 윈도우 기법으로 O(n) 풀이가 가능하다.
  - s1의 길이만큼의 윈도우를 s2 위에서 이동
  - 윈도우 내 문자 빈도가 s1의 빈도와 일치하는지 확인

엄밀히는 슬라이딩 윈도우지만, 본질적으로 "모든 위치를 검사"하는
브루트포스의 최적화 버전이다. DaC/Greedy/DP 어느 것에도 해당하지 않는다.
""",
    },
    {
        "id": 7,
        "paradigm": "Dynamic Programming",
        "explanation": """
LIS(Longest Increasing Subsequence)는 대표적인 DP 문제.

O(n^2) 풀이:
  dp[i] = i번째 원소에서 끝나는 LIS의 길이
  dp[i] = max(dp[j] + 1) for j < i where arr[j] < arr[i]

O(n log n) 풀이:
  이진 탐색을 활용한 최적화 (patience sorting)

핵심: "이전 선택이 이후 선택에 영향"을 주므로 DP가 필요하다.
""",
    },
    {
        "id": 8,
        "paradigm": "Divide & Conquer",
        "explanation": """
카라츠바(Karatsuba) 알고리즘 - 분할정복.
  큰 수를 반으로 나누어 3번의 곱셈으로 해결.
  시간 복잡도: O(n^1.585) (일반 곱셈은 O(n^2))

  x = a * 10^(n/2) + b
  y = c * 10^(n/2) + d
  xy = ac * 10^n + ((a+b)(c+d) - ac - bd) * 10^(n/2) + bd

핵심: 문제를 독립적인 부분으로 나누어 재귀적으로 해결.
""",
    },
    {
        "id": 9,
        "paradigm": "Greedy",
        "explanation": """
이벤트 스윕(Event Sweep) + 그리디.
  1. 시작/종료 이벤트를 시간순으로 정렬
  2. 시작 이벤트마다 카운터 +1, 종료 이벤트마다 -1
  3. 카운터의 최대값 = 필요한 최소 회의실 수
  O(n log n) 시간.

또는 최소 힙을 사용하여:
  1. 종료 시간이 가장 빠른 회의실에 새 회의를 배정
  2. 가능하면 기존 회의실 재사용, 아니면 새 회의실 추가

핵심: "가장 빨리 비는 회의실에 배정"하는 탐욕적 선택이 최적.
""",
    },
    {
        "id": 10,
        "paradigm": "Dynamic Programming",
        "explanation": """
편집 거리(Edit Distance)는 대표적인 DP 문제.

dp[i][j] = word1의 처음 i글자를 word2의 처음 j글자로 바꾸는 최소 비용

재귀식:
  word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
  다를 때: dp[i][j] = 1 + min(
      dp[i-1][j],     # 삭제
      dp[i][j-1],     # 삽입
      dp[i-1][j-1]    # 교체
  )

O(mn) 시간, O(mn) 공간.
LCS와 유사한 구조의 2차원 DP.
""",
    },
]


def print_problems():
    """문제만 출력한다 (해설 없이)."""
    print("=" * 65)
    print(" 알고리즘 패러다임 판별 연습")
    print(" 각 문제를 읽고, 적합한 패러다임을 선택하세요.")
    print(" 패러다임: Brute Force / Divide & Conquer / Greedy / DP")
    print("=" * 65)

    for p in PROBLEMS:
        print(f"\n--- 문제 {p['id']}: {p['title']} ---")
        print(p["description"].strip())
        print(f"  -> 당신의 답: _______________")


def print_solutions():
    """해설을 출력한다."""
    print("\n" + "=" * 65)
    print(" 해설")
    print("=" * 65)

    for s in SOLUTIONS:
        p = PROBLEMS[s["id"] - 1]
        print(f"\n--- 문제 {s['id']}: {p['title']} ---")
        print(f"  정답: {s['paradigm']}")
        print(s["explanation"].rstrip())


def print_summary():
    """패러다임별 요약을 출력한다."""
    print("\n" + "=" * 65)
    print(" 패러다임 판별 가이드")
    print("=" * 65)
    print("""
  1. Brute Force (브루트포스)
     - 제약 조건이 작을 때 (n <= 수백)
     - "모든 경우를 나열/검사"
     - 다른 기법이 떠오르지 않을 때 기본 전략

  2. Divide & Conquer (분할정복)
     - 문제가 독립적인 부분 문제로 나뉠 때
     - 부분 문제 사이에 중복이 없을 때
     - 재귀적 구조가 자연스러울 때
     - 예: 정렬, 최근접 점 쌍, 큰 수 곱셈

  3. Greedy (그리디)
     - "매 단계 최선의 선택"이 전체 최적을 보장할 때
     - 탐욕 선택 속성(Greedy Choice Property)이 성립할 때
     - 선택 후 돌아가지 않아도 될 때
     - 예: 활동 선택, 분할 가능 배낭, Huffman

  4. Dynamic Programming (DP)
     - 최적 부분 구조 + 중복 부분 문제
     - "이전 선택이 이후에 영향"을 줄 때
     - 재귀식/점화식을 세울 수 있을 때
     - 예: LCS, 0-1 배낭, 편집 거리, LIS

  판별 순서:
     문제 읽기 -> 제약 확인 (작으면 BF)
     -> 독립 분할 가능? (D&C)
     -> 매 단계 최선 = 전체 최선? (Greedy)
     -> 중복 부분 문제 + 최적 부분 구조? (DP)
""")


if __name__ == "__main__":
    print_problems()

    print("\n" + "=" * 65)
    input("  [Enter]를 누르면 해설을 확인합니다...")
    print_solutions()
    print_summary()
