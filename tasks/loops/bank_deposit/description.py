description_declare_variables = """You have the opportunity to put money on deposit at a certain interest rate and make
a profit after a while.
For example, if you put 10,000 for 3 years at 4% per annum, we get:
    -First year: 10000 + 4% = 10400 # 10000 + 10000 * 0.04
    -Second year: 10400 + 4% = 10816 # 10400 + 10400 * 0.04
    -Third year: 10816 + 4% = 11248.64 # 10816 + 10816 * 0.04

    Net profit = 11248.64 - 10000 = 1248.64
    
Write a calculate_profit function that takes three parameters:
    amount - the initial amount that we put on deposit;
    percent - annual interest rate;
    period - the number of years (time for which the money is deposited).
The function must calculate and return the amount of net profit for all time.
Note: only the whole part is checked"""
