base = int(input("사각형의 밑변을 입력하세요 : "))
height = int(input("사각형의 높이를 입력하세요 : "))

area = base * height

print(f"밑변이 {base}이고 높이가{height}인 사각형의 면적은 {area}입니다. ")

print("높이가", height, "이고 밑변이", base, "인 사각형의 면적은", area, "입니다")
print("높이가 %d이고 밑변이 %d인 사각형의 면적은 %d입니다") % (base, height, area)
