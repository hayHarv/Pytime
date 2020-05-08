import argparse
import pandas as pd
import calc_mean as cm
import calc_sum as cs

parser = argparse.ArgumentParser(description='Prints the mean of a column in a csv')

parser.add_argument('Path', metavar='path', type=str, help='path to csv') 
parser.add_argument('Column', metavar='column', type=str, help='column on which to perform calculation')
parser.add_argument('-c', '--calculation', metavar='calculation', required=True, help='which calculation to perform, `mean` or `sum`')

def read_csv(path):
    return pd.read_csv(path)

def main(path: str, column: str, calculation: str):

    calc_functions = {'mean': cm.calc_mean, 'sum': cs.calc_sum}
    calc_func = calc_functions[calculation]

    df = read_csv(path)
    result = calc_func(df, column)
    message = f"{calculation} for column {column}: {result}"
    print(message)


if __name__ == '__main__':
    args = parser.parse_args()
    var_args = vars(args)

    path = var_args["Path"]
    column = var_args["Column"]
    calculation = var_args["calculation"]

    main(path, column, calculation)

    