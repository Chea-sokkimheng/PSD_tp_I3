#PROBLEM 9
def electricity_bill(kWh):
    if kWh < 0:
        return None

    tiers1 = min(kWh, 50)
    tiers2 = min(max(kWh - 50, 0), 150)
    tiers3 = max(kWh - 200, 0)

    cost = tiers1 * 480 + tiers2 * 610 + tiers3 * 730

    cost = cost + 2000

    bill = cost * 1.10

    return round(bill)

for kWh in [0, 35, 50, 120, 200, 350]:

    bill = electricity_bill(kWh)
    usd = bill / 4100

    print(f"{kWh:3} kWh -> {bill:3,} riel (≈{usd:,.2f} USD)")

kwh = float(input("Enter the electricity consumption in kWh: "))
bill = electricity_bill(kwh)
if bill is not None:
    print(f"{kwh:3} kWh -> {bill:3,} riel (≈{usd:,.2f} USD)")
else:
    print("Invalid consumption. Please enter a non-negative value.")



