from sys import exit

from ui import find_args
from ui.gui.application import Application


def help():
    args = find_args()
    app = Application([])
    # print(f'Вы ввели {", ".join([str(s) for s in args.ELEMENT])}; их сумма {sum(args.ELEMENT)}')
    exit(app.exec())
