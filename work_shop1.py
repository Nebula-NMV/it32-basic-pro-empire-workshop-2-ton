print("---------------------------------")
quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมา : "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ : "))
team_members = int( input("จำนวนลูกน้องในทีมที่ไปทำงาน : "))

cost = quantity * cost_price
revenue = sell_price * quantity
profit = revenue - cost
boss =  profit * 0.20
pay_member = (profit - boss) / team_members

print("---------------------------------")
print(f"ต้นทุนทั้งหมด {cost} (บาท)")
print(f"รายรับทั้งหมด {revenue} (บาท)")
print(f"กำไรสุทธิ {profit} (บาท)")
print(f"จำนวนเงินที่หักไปให้บอส {boss} (บาท)")
print(f"จำนวนเงินที่ลูกน้องแต่ละคนได้ {pay_member} (บาท)")
print("---------------------------------")