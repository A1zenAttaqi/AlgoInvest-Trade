import time
import csv
from tqdm import tqdm

start_time = time.time()

MAX_BUDGET = 500

def read_csv(filename):
    try:
        with open(filename) as csvfile:
            shares_file = csv.reader(csvfile, delimiter=',')
            shares_list = []
            next(csvfile)
            for row in shares_file:
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    share = (
                        row[0],                         # name
                        int(float(row[1]) * 100),       # cost
                        float(float(row[1]) * float(row[2]) / 100)  # profit
                    )
                    shares_list.append(share)

            return shares_list

    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist. Please try again.\n")


def knapsack(shares_list):
    max_inv = int(MAX_BUDGET * 100)     # capacity
    shares_total = len(shares_list)
    cost = []       # weights
    profit = []     # values

    for share in shares_list:
        cost.append(share[1])
        profit.append(share[2])

    ks = [[0 for x in range(max_inv + 1)] for x in range(shares_total + 1)]

    for i in tqdm(range(1, shares_total + 1)):

        for w in range(1, max_inv + 1):
            if cost[i-1] <= w:
                ks[i][w] = max(profit[i-1] + ks[i-1][w-cost[i-1]], ks[i-1][w])
            else:
                ks[i][w] = ks[i-1][w]

    # Retrieve combination of shares from optimal profit
    best_combo = []

    while max_inv >= 0 and shares_total >= 0:

        if ks[shares_total][max_inv] == \
                ks[shares_total-1][max_inv - cost[shares_total-1]] + profit[shares_total-1]:

            best_combo.append(shares_list[shares_total-1])
            max_inv -= cost[shares_total-1]

        shares_total -= 1

    return best_combo

def display_results(best_combo):
    print(f"\nMost profitable investment ({len(best_combo)} shares) :\n")
    cost = []
    profit = []
    for action in best_combo:
        print(f"{action[0]} | {action[1] / 100} € | +{action[2]} €")
        cost.append(action[1] / 100)
        profit.append(action[2])

    print("\nTotal cost : ", sum(cost), "€")
    print("Profit after 2 years : +", sum(profit), "€")
    print("\nTime elapsed : ", time.time() - start_time, "seconds\n")    
    

def main():
    file_path = 'actions_data.csv'
    actions = read_csv(file_path)
    print(f"\nProcessing  ({len(actions)} valid shares) for {MAX_BUDGET}€ :")
    display_results(knapsack(actions))


if __name__ == "__main__":
    main()
