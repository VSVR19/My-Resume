import sys


class BestTimeToBuyAndSellStock:

    def __init__(self):
        pass

    @staticmethod
    def determine_max_profit_brute_force(stock_prices):
        maximum_profit = 0
        for outer_indexer in range(0, len(stock_prices)):
            for inner_indexer in range((outer_indexer + 1), len(stock_prices)):
                cost_price = stock_prices[outer_indexer]
                selling_price = stock_prices[inner_indexer]
                print("Cost price is: {0} and selling price is: {1}.".format(cost_price, selling_price))

                if cost_price > selling_price:
                    break

                if cost_price <= selling_price:
                    result = selling_price - cost_price
                    print("Result is: {0}.".format(maximum_profit))

                    if result >= maximum_profit:
                        maximum_profit = result

        print("Maximum profit is: {0}.".format(maximum_profit))
        return maximum_profit

    @staticmethod
    def determine_max_profit(stock_prices):
        maximum_profit = 0
        length_stock_prices = len(stock_prices)

        if length_stock_prices <= 1:
            maximum_profit = 0
        # elif length_stock_prices == 1:
        #     maximum_profit = stock_prices[0]
        else:
            minimum_price = sys.maxsize

            for indexer in range(length_stock_prices):
                current_element = stock_prices[indexer]

                if current_element <= minimum_price:
                    minimum_price = current_element

                elif (current_element - minimum_price) >= maximum_profit:
                    maximum_profit = (current_element - minimum_price)

        return maximum_profit


ObjectBestTimeToBuyAndSellStock = BestTimeToBuyAndSellStock
# print(ObjectBestTimeToBuyAndSellStock.determine_max_profit_brute_force([7, 1, 5, 3, 6, 4]))
# print(ObjectBestTimeToBuyAndSellStock.determine_max_profit_brute_force([7, 6, 4, 3, 1]))

print(ObjectBestTimeToBuyAndSellStock.determine_max_profit([7, 1, 5, 3, 6, 4]))
print(ObjectBestTimeToBuyAndSellStock.determine_max_profit([7, 6, 4, 3, 1]))