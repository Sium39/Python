#if else statements

hot = False
cold = True

if hot:
    print("It's a hot day")
    
elif cold:
    print("It's a cold day")
else:
    print("Nothing happens")
    
#task

price = 1000000
good_credit = False

if good_credit:
    payment = 0.1 * price
    
else:
    payment = 0.2 * price
    
print(f"Down payment: ${payment}")