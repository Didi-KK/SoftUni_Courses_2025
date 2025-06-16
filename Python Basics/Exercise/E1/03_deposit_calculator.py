deposit = float(input())
deposit_term = int(input())
annual_interest = float(input())
deposit_incl_interest_per_anum = deposit * annual_interest / 100
deposit_incl_interest_per_month = deposit_incl_interest_per_anum / 12
deposit_incl_interest_per_term = deposit + deposit_term * deposit_incl_interest_per_month

print(deposit_incl_interest_per_term)
