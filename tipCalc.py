def calculate_tip(bill, percent):
    tip =  bill * (percent/100)
    return tip

bill_amount = float(input("what was the bill amount"))
tip_percent = float(input("what perent do you want to tip"))
#need to make that the percentage into a float somehow, or in some way deal with th error on line 8
'''Traceback (most recent call last):
  File "/workspaces/PythonInterviewPrep/tipCalc.py", line 8, in <module>
    total = bill_amount(bill_amount, tip_percent)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
total = bill_amount(bill_amount, tip_percent)
print(f"the amount: {tip}")