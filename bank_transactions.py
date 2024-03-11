from datetime import datetime

def solution(A, D):
    transactions = A #transaction list
    dates = D #dates list
    bal = 0 #initial balance at beginning of year
    fee = 5 #fee to be paid per month
    prev_month = None #setting the value of previous month to nothing and will need to be updated
    transactions_in_month = 0 #counter for transactions in the current month
    for amount, date in zip(transactions, dates): #iterating through the amount balance in the transaction list and the dates using zip
        if amount < 0:
            bal -= abs(amount) #if amount is negative then do absolute amount balance - amount to subtract it is a card payment
        else:
            bal += amount #if amount is positive then do amount balance + amount to add an incoming transfer
            transactions_in_month += 1 #increment the transaction count for the new month
        if date.month != prev_month:
            if transactions_in_month >= 3 and sum(transactions) >= 100:
                pass #if results to true then do not deduct fee
            else:
                bal -= fee #deduuct the fee for the month
            transactions_in_month = 0 #reseting the transaction count for the new month
            prev_month = date.month #update previous month to current month
    return bal
    
    
transactions = [100, 100, -10, -20, -30] 
dates = [datetime(2020, 1, 1), datetime(2020, 2, 1), datetime(2020, 2, 11), datetime(2020, 2, 5), datetime(2020, 2, 8)]
print(solution(transactions, dates))
