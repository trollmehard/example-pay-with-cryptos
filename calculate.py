#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://github.com/trollmehard/example-pay-with-cryptos.git

Calculation of whether it was profitable to convert a portion of its daily
expenditure into cryptographic currencies in 2017 and pay for it.

The results will be displayed in the console.

By https://steemit.com/@chkoenig 2018
'''

# Set to True for some more output in the console
SHOW_DETAILS = True

# Assumptions

# the fee to buy cryptocurrencies from fiat money
FEE = 0.06
# The money spend each month in your currency
MONEY = 100  # Euro / USD / ...
# Only for displaying the results
CURRENCY = "$"
# The ratio split between Bitcion und Ethereum 
# change to 0.4 for 40% Bitcoin and 60% Ethereum
RATIO = 0.5  # float between 0 and 1
# The money avalaibale in BTC and ETH each month
MONEY = {
	"BTC": MONEY * RATIO,
	"ETH": MONEY * (1 - RATIO)
}

FEE = {
	"BTC": MONEY["BTC"] * FEE,
	"ETH": MONEY["ETH"] * FEE
}

AVAILABLE_CYPTOS = ["BTC", "ETH"]

# All prices are taken from https://coinmarketcap.com in US Dollar
# from 1. January 2017 to 1. January 2018 - 13 months

# Prices of Bitcoin and Ethereum
PRICE = {
	"BTC": [960, 977, 1185, 1069, 1307, 2376, 2466, 2701, 4812, 4298, 6622, 10660, 13400],
	"ETH": [8.15, 10.79, 15.77, 49.73, 80.04, 228.5, 285.2, 222.6, 389.8, 299.9, 298.2, 470.2, 768.9]
}

# The template and the dividers to display the results
DIVIDER = 30 * "-"
TEMPLATE = "> {0}: Profit for month: {1} ---> {2} {3} / Remaining coins: {4} {0}"


def monthly_profit(crypto, month, reinvest, remaining_coins):
	"""
	Return the profit for each month.
	
	crypto (string): cryptocurrency - "BTC" or "ETH".
	month (int): 0 - January 2017; 1 - February 2017 and so on.
	reinvest (bool): If you spend the cryptos or if you reinvest them
	remaining_coins (float): amount if reinvested crypto for this month.
	"""

	# calculate the amount of the cryptocurrency you get for the MONEY
	# e.g. (50$ - 3$ (FEE)) / 960 $/BTC = 0.05 BTC
	coins = (MONEY[crypto] - FEE[crypto]) / PRICE[crypto][month]
	# add the remeining crypto, no fees needed (already bought)
	coins += remaining_coins
	# reassign remaining_coins with the amount after one month
	remaining_coins = coins - (MONEY[crypto] / PRICE[crypto][month + 1])
	# calculate the price difference between both months == the profit
	profit = remaining_coins * PRICE[crypto][month + 1]  # can be negative

	if SHOW_DETAILS:
		print(TEMPLATE.format(
			crypto, (month + 1), round(profit, 2), CURRENCY, remaining_coins))

	return remaining_coins, profit


def calculate(reinvest=False):
	"""Return the profit made for this crypto the complete time."""
	# Assign the complete profit
	profit_complete = 0
	for crypto in AVAILABLE_CYPTOS:
		# assign some empty variables
		profit_crypto = 0  # the profit of the crypto (BTC/ETH)
		remaining_coins = 0  # 
		for index, price in enumerate(PRICE[crypto][:-1]):
			remaining_coins, profit = monthly_profit(
				crypto, index, reinvest, remaining_coins)
			
			if reinvest is False:
				# if you spend all money you have no remaining coin but profit
				profit_crypto += profit
				remaining_coins = 0

		if reinvest:
			# Therefore, if you reinvest also calculate the profit
			profit_crypto = profit

		profit_complete += profit_crypto

		if SHOW_DETAILS:
			print(DIVIDER)
			print(TEMPLATE.format(
				crypto, "ALL", round(profit_crypto, 2),CURRENCY,remaining_coins))
			print(DIVIDER)

	return profit_complete


def display_results():

	print("\n## Profit if you don\'t reinvest the money\n")
	print("That means if you make +20 {0} gains, you spend 120 {0} this "
		  "month\n".format(CURRENCY))

	print(TEMPLATE.format("ALL", "ALL", round(calculate(), 2), CURRENCY, 0))

	print("\n\n## Profit if you reinvest the money\n")
	print("That means if you make +20 {0} gains, you only spend 100 {0} this "
		  "month and take the profit to the next month\n".format(CURRENCY))
	
	print(TEMPLATE.format(
		"ALL", "ALL", round(calculate(reinvest=True), 2), CURRENCY, 0))


if __name__ == "__main__":
	"""First function that gets called."""
	display_results()
