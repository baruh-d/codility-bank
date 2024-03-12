from datetime import datetime

def solution(A, D):
    transactions = A #transaction list
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in D] #dates list in yyyy-mm-dd
    bal = 0 #initial balance at beginning of year
    fee = 5 #fee to be paid per month
    prev_month = None #setting the value of previous month to nothing and will need to be updated
    transactions_in_month = 0 #counter for transactions in the current month
    total_value_in_month = 0
    for amount, date in zip(transactions, dates): #iterating through the amount balance in the transaction list and the dates using zip
        if amount < 0:
            bal -= abs(amount) #if amount is negative then do absolute amount balance - amount to subtract it is a card payment
            transactions_in_month += 1 #increment the transaction count for the new month
            total_value_in_month  += amount
        else:
            bal += amount #if amount is positive then do amount balance + amount to add an incoming transfer
        if transactions_in_month >= 3 and total_value_in_month >= 100 and refunded == False:
            refunded = True
            bal += fee
        if date.month != prev_month:
            #if transactions_in_month < 3 and sum(transactions) < -100: #check if the transactions are less than three and also if they add up to 100        
            transactions_in_month = 1 #reseting the transaction count for the new month
            total_value_in_month = amount
            refunded = False
            prev_month = date.month #update previous month to current month
    bal -= fee * 12 #deduuct the fee   
    return bal #returns balance at end of year
    
#example usage
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))