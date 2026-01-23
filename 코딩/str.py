str1 = "abcd"
str2 = "efgh"
str3 = """1234567890"""
str4 = """abcdefg"""
str5 = str1 + str2
str6 = str5 + "hijk"

print(str1)
print("첫 번째 문자열" + str2)
print("변수에 있는 값을 출력 %s 값 출력 가능" % str3)
print("두 변수에 %s 있는 문자열 출력 %s" % (str1, str2))
print("첫 번째 변수의 값 {0}, 두 번째 변수의 값{1}".format(str5, str6))
print(f"{str1}, {str2}, {str3}")
