from datetime import datetime

def solution(A, D):
    transactions = A
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in D]
    bal = 0
    fee = 5
    prev_month = None
    transactions_in_month = 0
    total_value_in_month = 0
    
    for i, (amount, date) in enumerate(zip(transactions, dates)):
        if amount < 0:
            bal -= abs(amount)
            transactions_in_month += 1
            total_value_in_month += amount
        else:
            bal += amount
            
        if date.month != prev_month:
            if transactions_in_month >= 3 and total_value_in_month >= 100:
                bal -= fee
            transactions_in_month = 0
            total_value_in_month = 0
            prev_month = date.month
            
    bal -= fee * 12  # Deduct the fee for each month of the year
    
    return bal

# Example usage
print(solution([100, 100, -10, -20, -30], ["2020-01-01", "2020-02-01", "2020-02-11", "2020-02-05", "2020-02-08"]))
print(solution([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))
print(solution([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))
print(solution([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14", "2020-07-12"]))
print(solution([-60, 60, -40, -20], ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]))

