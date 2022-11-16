

# def monthly_interest_rate(annual_interest_rate):
#     return annual_interest_rate / 12.0
#
# def min_monthly_payment(min_monthly_pay_rate, prev_bal):
#     return min_monthly_pay_rate * prev_bal
#
# def monthly_unpaid_bal(prev_bal, min_monthly_payment):
#     return prev_bal - min_monthly_payment
#
# def updated_balance_each_month(monthly_unpaid_bal, monthly_interest_rate):
#     return monthly_unpaid_bal + (monthly_interest_rate*monthly_unpaid_bal)



#So happy: got this first try --> Good engineers read the problem 11 times!
def problem_1(balance, annualInterestRate, monthlyPaymentRate):
    monthly_interest_rate = annualInterestRate/12.0
    #balance changes every month! --> min payment changes every month
    for i in range(1,13):
        min_monthly_payment = monthlyPaymentRate * balance
        monthly_unpaid_bal = balance - min_monthly_payment
        updated_balance_each_month = monthly_unpaid_bal + \
                                     (monthly_interest_rate * monthly_unpaid_bal)
        balance = round(updated_balance_each_month,2)

        # print("Month " + str(i) + " Remaining balance: " +
        #       str(balance))
    print("Remaining balance: " + str(balance))


#Has anyone solved with binary search?
def problem_2(balance, annualInterestRate):
    #retain the original balance
    original_balance = balance
    #calculate monthly interest
    monthlyInterestRate = annualInterestRate/12
    #current monthly payment
    monthlyPayment = 0

    while balance >= 0:
        #reset the value
        balance = original_balance

        #test the new monthlyPaymentValue -->
        # if balance is greater than zero we didn't find the right minimum
        for month in range(1,13):
            unpaidBalance = balance - monthlyPayment
            interest = unpaidBalance + interest
            balance = unpaidBalance  + interest
    print("lowest payment", monthlyPayment)

def problem_3(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    #lower bound being we pay the most possible every month
    lowerBound = balance/12
    #upper bound being we pay the least possible every month?
    upperBound = (balance* (1+monthlyInterestRate)**12)/12
    originalBalance = balance

    while True:
        if abs(balance) <= 0.01: #just < ok?
            break
        balance = originalBalance
        monthlyPayment = (lowerBound + upperBound)/2
        for month in range(1,13):
            unpaidBalance = balance - monthlyPayment
            interest = unpaidBalance * monthlyInterestRate
            balance  = unpaidBalance + interest

            if balance > 0:
                lowerBound = monthlyPayment
            elif balance < 0:
                upperBound = monthlyPayment
            elif balance == 0:
                break
    print("Lowest payment: ", round(monthlyPayment,2))











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # balance = 42
    # annualInterestRate = 0.2
    # monthlyPaymentRate = 0.04
    balance = 484
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04
    problem_1(balance, annualInterestRate, monthlyPaymentRate)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
