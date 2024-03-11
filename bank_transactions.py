from datetime import datetime

def solution(A, D):
    transactions = A #transaction list
    dates = D #dates list
    bal = 0 #initial balance at beginning of year
    fee = 5 #fee to be paid per month
    for amount in transactions: #iterating through the amount balance in the transaction list
        if amount < 0:
            bal -= abs(amount) #if amount is negative then do amount balance - amount
            for transactions in dates:
                if bal < amount 
                
        elif amount >= 0:
            bal += abs(amount) #if amount is positive then do amount balance + amoun
        
    return bal
    
    
