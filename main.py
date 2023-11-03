def main():
    print("Monthly Payment:")
    print("")


    principal = float(input("Loan Amount: "))
    apr = float(input("Annual Intrest: "))
    years = int(input("Amount of years"))


    monthly_intrest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payments = principal * monthly_intrest_rate / (1 -(1 + monthly_intrest_rate) ** (-amount_of_months))


    print(f" Monthly payment for loan:${monthly_payments:.2f} " )

if __name__ == "__main__":
    main()