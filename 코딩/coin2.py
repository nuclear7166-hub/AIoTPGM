##
#     자판기에서 거스름돈을 교환하는 프로그램
#

itemprice = int(input("상품의 가격을 입력하세요 : "))
note = int(input("1000원 지폐개수 : "))
coin500 = int(input("500원 동전개수 : "))
coin100 = int(input("100원 동전개수 : "))

change = note * 1000 + coin500 * 500 + coin100 * 100 - itemprice
print(f" 거스름돈은 {change}원 입니다.")

ncoin500 = change // 500
left_money = change % 500

ncoin100 = left_money // 100
left_money = left_money % 100

ncoin10 = left_money // 10
left_money = left_money % 10

ncoin1 = left_money

print(
    f"500원 동전은 {ncoin500}개, 100원 동전은 {ncoin100}개, 10원 동전은 {ncoin10}개, 1원 동전은 {ncoin1}개 입니다. "
)
