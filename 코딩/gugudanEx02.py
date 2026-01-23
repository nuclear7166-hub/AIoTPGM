# 단을 입력 받아 해당 단을 출력하는 프로그램 작성
# 0을 입력하기 전까지 계속 실행

while True:
    dan = int(input("출력할 단을 입력하세요(종료=0) : "))
    if dan == 0:
        break
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
