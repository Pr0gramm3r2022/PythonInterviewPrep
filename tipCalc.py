def calculate_tip(bill, percent):
    tip =  bill * (percent/100)
    return tip

bill_amount = float(input("what was the bill amount"))
tip_percent = float(input("what perent do you want to tip"))

total = bill_amount(bill_amount, tip_percent)
print(f"the amount: {tip}")