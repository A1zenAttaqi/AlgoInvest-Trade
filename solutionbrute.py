import itertools
import time
import csv
from tqdm import tqdm
start_time = time.time()


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
                    share = {
                        'name': row[0],
                        'cost': float(row[1]),
                        'profit': float(row[2]) / 100  
                    }
                    shares_list.append(share)

            return shares_list

    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist. Please try again.\n")


def brute_force_investment(actions, max_budget):
    best_combination = None
    max_profit = 0

    for r in tqdm(range(1, len(actions) + 1)):
        combinations = itertools.combinations(actions, r)
        for combination in combinations:
            total_cost = sum(action['cost'] for action in combination)
            if total_cost <= max_budget:
                total_profit = sum(action['cost'] * action['profit'] for action in combination)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_combination = combination

    return best_combination, max_profit


def main():
    file_path = 'actions_data.csv'
    actions = read_csv(file_path)
    max_budget = 500
    print(f"\nProcessing {len(actions)} shares for {max_budget}€ :")


    best_combination, max_profit = brute_force_investment(actions, max_budget)

    if best_combination:
        print(f"\nMost profitable investment ({len(best_combination)} shares) :\n")
        for action in best_combination:
            print(f"{action['name']} - Cost: {action['cost']} €, Profit: {action['cost'] * action['profit']} €")

        print(f"\nTotal Cost: {sum(action['cost'] for action in best_combination)} €")
        print(f"Profit after 2 years : + {max_profit} €")
    else:
        print("No valid combination found within the budget.")

    print("\nTime elapsed : ", time.time() - start_time, "seconds")


if __name__ == "__main__":
    main()