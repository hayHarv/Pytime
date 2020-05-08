import argparse
import calc_mean
import calc_sum

parser = argparse.ArgumentParser(description='Prints the mean of a column in a csv')

parser.add_argument('Path', metavar='path', type=str, help='path to csv') 
parser.add_argument('Column', metavar='column', type=str, help='column on which to perform calculation')


if __name__ == '__main__':
    args = parser.parse_args()