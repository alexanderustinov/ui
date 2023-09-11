from . import find_args

def help():
    args = find_args()
    print(f'Вы ввели {", ".join([str(s) for s in args.ELEMENT])}; их сумма {sum(args.ELEMENT)}')