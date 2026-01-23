##
#  윤년 여부를 판별하는 프로그램을 작성하세요
#

year = int(input("연도를 입력하세요. : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 아닙니다.")

