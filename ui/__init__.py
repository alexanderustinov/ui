import argparse


def find_args():
    parser = argparse.ArgumentParser(
        prog='ui',
        description='Программа складывает переданные аргументы')
    parser.add_argument('ELEMENT', type=int, nargs='+')
    return parser.parse_args()
