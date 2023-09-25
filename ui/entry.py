from . import find_args
from .gui.application import Application


def help():
    args = find_args()
    app = Application([])
    # print(f'Вы ввели {", ".join([str(s) for s in args.ELEMENT])}; их сумма {sum(args.ELEMENT)}')
    quit(app.exec())
