# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = float(meal_cost*tip_percent)/100
    tax_cost = float(meal_cost*tax_percent)/100
    return '{0:.0f}'.format(meal_cost+tip_cost+tax_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())
    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
