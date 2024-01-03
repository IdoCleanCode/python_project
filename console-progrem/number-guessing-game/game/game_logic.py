import random

def create_number():
    return random.randint(1, 100)

def user_input():
    while True:
        try:
            guess = int(input("1부터 100까지 숫자를 입력하세요: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("1부터 100사이 숫자만 입력하세요.")
        except ValueError:
            print("숫자만 입력하세요.")

def check_guess(guess, answer):
    if guess < answer:
        return "높은 숫자입니다."
    elif guess > answer:
        return "낮은 숫자 입니다."
    else:
        return "정답입니다."

def continue_game():
    while True:
        user_input = input("계속하시겠습니까? (y/n): ")
        if user_input.lower() in ['y', 'n']:
            return user_input.lower() == 'y'
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

def play_game():
    while True:
        answer = create_number()
        while True:
            guess = user_input()
            result = check_guess(guess, answer)
            print(result)
            if result == "정답입니다.":
                print(f"축하합니다! 정답은 {answer}입니다.")
                break
        if not continue_game():
            break

play_game()
