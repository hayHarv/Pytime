import pandas as pd
import argparse 

parser = argparse.ArgumentParser(description='Prints the sum of a column in a csv')

parser.add_argument('Path', metavar='path', type=str, help='path to csv')
parser.add_argument('Column', metavar='column', type=str, help='column for which to caclulate sum')

def calc_sum(df, column):
    return df[column].sum()

if __name__ == '__main__':

    args = parser.parse_args()

    file_path = args.Path
    column = args.Column

    print(file_path)
    print(column)

    print(pd.read_csv(args.Path)[column].sum())