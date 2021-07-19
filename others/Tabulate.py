# pip install tabulate

from tabulate import tabulate

def content():
    header = ["Planets", "Rain (Km)", "Mass (x 10 ^ 21 kg)"]
    return [colored(c, 'cyan', attrs=['bold']) for c in header]

def create_table():
    table = [
        ["Sol", 696000, 1989100000],
        ["Mercurie", 2439, 330],
        ["Venus", 6051, 641],
        ["Earth", 6371, 5973.6],
        ["Marte", 3390, 641.85],
        ["Jupiter", 69911, 1898600]]

    return [[colored(d[0], 'red', attrs=['bold']), d[1], d[2]] for d in table]

print(tabulate(create_table(), headers=content(), tablefmt="fancy_grid"))
