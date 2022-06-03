from calendar import month
from datetime import datetime
from numpy import full, integer
import numpy_financial as numfi
from math import floor



def create_lists(months_until_completion: integer, term_of_asset: integer, yearly_return_amount: integer, investment: integer):
    yearly_invest_array = [0] * term_of_asset  # Term of asset creates the list length that has yearly investments and yearly returns.
    yearly_return_array = [0] * term_of_asset
    print(f"yearly_invest_array:{yearly_invest_array}")
    print(f"yearly_return_array:{yearly_return_array}")
    print()

    months_remainder = months_until_completion % 12 # Months of investment in partial year.
    full_years_of_invest = int((months_until_completion - months_remainder)/12) # Number of full years of investment
    invest_by_month = investment/months_until_completion # investment spread over investment period
    full_year_investment_amount = int(invest_by_month * 12) # Full year of investment Amount. Used to set Array of payments.
    partial_year_invest_amount = floor(months_remainder * invest_by_month) # Partial year used to set investments array.
    index_of_partial_year = full_years_of_invest
    
    term_in_months = (term_of_asset*12) # Converts term into monthly units.
    months_of_return= term_in_months - months_until_completion #calculates total months of return.
    remainder_of_return_months = months_of_return % 12 # Gives months of return in partial year. 
    full_years_of_return = int(months_of_return - remainder_of_return_months)/12 # Gives number of full years of return.
    first_full_year = 1+(term_of_asset-full_years_of_return) # Gives first full year of returns.
    index_first_full_return = int(term_of_asset - full_years_of_return) #Index of first full year of return.

    partial_year_return_amount = floor((remainder_of_return_months/12)*yearly_return_amount) # Gives amount of return in partial year.

    for i in range(index_first_full_return,term_of_asset):
        print(f"Year of return: {i}")
        yearly_return_array[i] = yearly_return_amount

    if full_years_of_invest >= 0:
        for i in range(0,full_years_of_invest):
            print(f"year of investment:{i}")
            yearly_invest_array[i] = full_year_investment_amount

    if months_remainder > 0:
        yearly_invest_array[index_of_partial_year] = partial_year_invest_amount #Note: Years of investment    
        yearly_return_array[index_of_partial_year] = partial_year_return_amount 

    print(f"Months remainder:{months_remainder}")
    print(f"Full years of investment:{full_years_of_invest}")
    print(f'Invest by month:{invest_by_month}')
    print(f"Full Years Invest amount:{full_year_investment_amount}")
    print(f"Partial Year Invest:{partial_year_invest_amount}")
    print()
    print(f"term in months: {term_in_months}")
    print(f"months of return: {months_of_return}")
    print(f"remainder of return months: {remainder_of_return_months}")
    print(f"full years of return: {full_years_of_return}")
    print(f"First full year:{first_full_year}")
    print(f"Index Year of First full return: {index_first_full_return}")
    print()
    print(f"yearly_invest_array:{yearly_invest_array}")
    print(f"yearly_return_array:{yearly_return_array}")
    print()

    return yearly_invest_array, yearly_return_array

def irr_process(yearly_invest_array: list,yearly_return_array: list) -> float:

    # yearly_invest_array = [10,100,0]
    # yearly_return_array = [0,110,100]
    irr_inputs = []


    for i in range(len(yearly_return_array)):
        net_year = yearly_return_array[i]-yearly_invest_array[i]
        irr_inputs.append(net_year)

    print(f"irr_input_array{irr_inputs}")
    irr_float = numfi.irr(irr_inputs)
    print(irr_float)

    return irr_inputs, irr_float

# yearly_invest_array, yearly_return_array = create_lists(months_until_completion=14,term_of_asset=8,yearly_return_amount=200_000,investment=10_000)

# irr_process(yearly_invest_array=yearly_invest_array,yearly_return_array=yearly_return_array)