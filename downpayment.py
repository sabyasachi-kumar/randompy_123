good_credit=False
price=1000000
if good_credit:
    print("downpayment= $", 0.1*price)
else:
    print("downpayment= $", 0.2*price)

has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("eligible for loan")