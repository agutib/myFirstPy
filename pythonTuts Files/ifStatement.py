downpayment = input("Your Downpayment : ")
price = input("Price of the Item : ")
interest = input("How Much is the Interest? in Percent :")
monthly = input("Number of Months? :")

getDecimal = int(interest) / 100
getRemaining = int(price) - int(downpayment)
getMonthly = (getRemaining // int(monthly)) 
getTotal = getMonthly * getDecimal + getMonthly
print (str(getTotal))