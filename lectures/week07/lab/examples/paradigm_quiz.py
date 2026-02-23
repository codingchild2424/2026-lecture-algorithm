"""Algorithm Paradigm Quiz - identify the best approach for each problem."""

PROBLEMS = [
    {
        "question": "정렬된 배열에서 특정 값의 위치를 찾아라.",
        "answer": "Divide & Conquer",
        "explanation": "이진 탐색 — 배열을 반으로 나누어 탐색. O(log n)"
    },
    {
        "question": "동전의 종류가 [1, 5, 10, 50, 100, 500]일 때 거스름돈 최소 동전 수를 구하라.",
        "answer": "Greedy",
        "explanation": "큰 동전부터 사용 — 한국/미국 화폐처럼 배수 관계일 때 그리디가 최적."
    },
    {
        "question": "두 문자열의 최장 공통 부분 수열(LCS) 길이를 구하라.",
        "answer": "Dynamic Programming",
        "explanation": "부분 문제가 겹치고 최적 부분 구조 존재 — DP 테이블로 O(mn) 해결."
    },
    {
        "question": "n개의 점 중 가장 가까운 두 점의 거리를 구하라.",
        "answer": "Divide & Conquer",
        "explanation": "점을 x좌표 기준으로 분할, 각 절반에서 최근접 쌍을 구하고 경계를 확인. O(n log n)"
    },
    {
        "question": "n개의 활동 중 겹치지 않게 최대한 많은 활동을 선택하라.",
        "answer": "Greedy",
        "explanation": "종료 시간 기준 정렬 후 탐욕적 선택 — Activity Selection Problem."
    },
    {
        "question": "n개의 물건(각각 무게와 가치)에서 배낭 용량 W 이내로 최대 가치를 담아라. (물건 쪼갤 수 없음)",
        "answer": "Dynamic Programming",
        "explanation": "0-1 Knapsack — 각 물건을 넣거나 안 넣거나의 선택이 겹치는 부분 문제를 형성."
    },
    {
        "question": "배열의 모든 부분 집합을 출력하라.",
        "answer": "Brute Force",
        "explanation": "2^n개의 부분 집합을 모두 생성해야 함 — 최적화 여지 없음."
    },
    {
        "question": "n×n 행렬 두 개를 곱하라. (n이 매우 큼)",
        "answer": "Divide & Conquer",
        "explanation": "Strassen 알고리즘 — 행렬을 4등분하여 7번의 곱셈으로 해결. O(n^2.81)"
    },
    {
        "question": "문자열을 Huffman 코드로 압축하라.",
        "answer": "Greedy",
        "explanation": "빈도수가 낮은 문자부터 합치는 탐욕적 선택이 최적."
    },
    {
        "question": "피보나치 수열의 n번째 항을 구하라.",
        "answer": "Dynamic Programming",
        "explanation": "fib(n) = fib(n-1) + fib(n-2) — 겹치는 부분 문제의 대표적 예시."
    },
]


def run_quiz():
    score = 0
    options = ["Brute Force", "Divide & Conquer", "Greedy", "Dynamic Programming"]

    for i, problem in enumerate(PROBLEMS, 1):
        print(f"\n{'='*60}")
        print(f"문제 {i}: {problem['question']}")
        print()
        for j, opt in enumerate(options, 1):
            print(f"  {j}. {opt}")

        try:
            choice = int(input("\n답 (1-4): "))
            chosen = options[choice - 1]
        except (ValueError, IndexError):
            chosen = ""

        if chosen == problem["answer"]:
            print(f"  ✓ 정답! — {problem['explanation']}")
            score += 1
        else:
            print(f"  ✗ 오답. 정답: {problem['answer']}")
            print(f"    {problem['explanation']}")

    print(f"\n{'='*60}")
    print(f"결과: {score}/{len(PROBLEMS)}")


if __name__ == "__main__":
    print("=== 알고리즘 패러다임 판별 퀴즈 ===")
    print("각 문제에 가장 적합한 알고리즘 패러다임을 선택하세요.\n")
    run_quiz()
