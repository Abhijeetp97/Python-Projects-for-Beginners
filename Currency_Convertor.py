# Rates as of 13.02.2025

def get_exchange_rates():
    # Exchange rates from USD to other currencies
    usd_rates = {
        'EUR': 0.96,
        'JPY': 153.26,
        'GBP': 0.80,
        'INR': 86.77,
        'CAD': 1.42,
        'AUD': 1.59,
        'CHF': 0.91,
        'CNY': 7.31,
        'SEK': 10.80
    }
    return usd_rates

# Calculate Rates for each currency
def calculate_rates(usd_rates):
    all_rates = {}
    for from_currency, from_rate in usd_rates.items():
        all_rates[from_currency] = {}
        for to_currency, to_rate in usd_rates.items():
            if from_currency == to_currency:
                all_rates[from_currency][to_currency] = 1.0
            else:
                # Round the calculated rate to two decimal places
                all_rates[from_currency][to_currency] = round(to_rate / from_rate, 2)
    # Add conversion rates from USD to other currencies
    all_rates['USD'] = usd_rates
    # Add conversion rates from other currencies to USD
    for currency, rate in usd_rates.items():
        all_rates[currency]['USD'] = round(1 / rate, 2)

    return all_rates

# Convert Currency
def currency_converter(amount, from_currency, exchange_rates):
    if from_currency not in exchange_rates:
        print("Invalid currency conversion.")
        return None

    converted_amounts = {}
    for to_currency, rate in exchange_rates[from_currency].items():
        converted_amounts[to_currency] = amount * rate
    
    return converted_amounts

# Main Function
def main():
    print("Currency Converter")
    usd_rates = get_exchange_rates()
    exchange_rates = calculate_rates(usd_rates)
    conversion_history = []

    while True:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the from currency (e.g., USD, EUR, JPY, GBP, INR): ").strip().upper()
        
        if from_currency not in exchange_rates:
            print("Invalid from currency. Please try again.")
            continue

        converted_amounts = currency_converter(amount, from_currency, exchange_rates)
        
        if converted_amounts is not None:
            print(f"{amount} {from_currency} is equivalent to:")
            for currency, amount in converted_amounts.items():
                print(f"{amount:.2f} {currency}")
                conversion_history.append(f"{amount:.2f} {from_currency} = {amount:.2f} {currency}")
        
        another_conversion = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if another_conversion != 'y':
            break

    print("\nConversion History:")
    for record in conversion_history:
        print(record)

if __name__ == "__main__":
    main()