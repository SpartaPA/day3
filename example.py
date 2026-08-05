"""간단한 파이썬 예제 - 구구단과 리스트 다루기"""


def gugudan(dan):
    """입력받은 단의 구구단을 리스트로 반환한다."""
    return [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]


def average(numbers):
    """숫자 리스트의 평균을 구한다. 빈 리스트면 0을 반환한다."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def main():
    for line in gugudan(3):
        print(line)

    scores = [88, 92, 75, 64, 100]
    print()
    print(f"점수: {scores}")
    print(f"평균: {average(scores):.1f}")
    print(f"최고점: {max(scores)}, 최저점: {min(scores)}")


if __name__ == "__main__":
    main()
