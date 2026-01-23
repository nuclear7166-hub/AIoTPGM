score = int(input("점수 입력 : "))

match score // 10:
    case 10:
        print("A학점")
    case 9:
        print("B학점")
    case 8:
        print("C학점")
    case 7:
        print("D학점")
    case 6:
        print("F학점")
    case _:
        print("F학점")
