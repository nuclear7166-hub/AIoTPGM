price = int(input("정가 입력하세요. : "))

if price > 40000:
    shippingcost = 0

else:
    shippingcost = 4000

print(f"배송비는 {shippingcost}원 입니다.")
