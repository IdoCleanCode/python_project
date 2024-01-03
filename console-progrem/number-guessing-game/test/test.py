import random

def generate_number():
    return random.randint(1, 100)

def get_user_input():
    while True:
        try:
            guess = int(input("1부터 100 사이 숫자를 맞춰주세요: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("1부터 100사이의 숫자만 입력하세요.")
        except ValueError:
            print("숫자로 입력해주세요.")

def check_guess(guess, answer):
    if guess < answer:
        print("더 높은 숫자입니다.")
        return False
    elif guess > answer:
        print("더 낮은 숫자입니다.")
        return False
    else:
        print("정답입니다.")
        return True

def play_game():
    answer = generate_number()
    attempts = 0

    while True:
        guess = get_user_input()
        attempts += 1
        if check_guess(guess, answer):  # 매개변수 순서를 올바르게 수정
            print(f"축하합니다! 당신은 {attempts}번 만에 맞추셨습니다.")
            break

# play_game 함수를 직접 호출하는 부분을 제거하고,
# 이 스크립트가 메인으로 실행될 때만 play_game이 호출되도록 합니다.
if __name__ == "__main__":
    play_game()
