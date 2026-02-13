def total_calc(bill_amt,tip_per):
    total=bill_amt*(1+0.01*tip_per)
    total=round(total,2)
    print("Please pay $",total)

total_calc(150,20)