from os import name, getuid
from sys import argv
import click
from .ex_functions import listd, resetit

msuc = '# USB device got reset.'
merr = '# Error: could not reset usb device'
mwin = '# Error: wrong input'


@click.command()
@click.option("--reset",
              help="reset USB device with its idVendor and idProduct",
              default=(None, None),
              type=(str, str), nargs=2)
@click.option("--list", help="list connected USB devices", is_flag=True)
@click.option("--filter",
              help="filter list of devices with USB class number", type=int,
              default=0)
def listt(reset, list, filter):
    if list or filter:
        lid = listd(gui=True)
        if filter != 0:
            lid = listd([filter], True)
        li = 0
        if len(lid) > 0:
            for ll in lid:
                print(str(li) + ". " + str(ll))
                li += 1
        else:
            print("# No USB devices were found")
    else:
        if resetit(',' + reset[0] + ',' + reset[1]):
            print(msuc)
        else:
            print(merr)


def intera():
    l = listd(gui=True)
    ll = 0
    for ld in l:
        print('[' + str(ll) + '] ' + ld)
        ll += 1
    i = input("\n\t Enter device nuber to reset : ")
    try:
        i = int(i)
        if i not in range(len(l)):
            print(mwin)
            return False
    except:
        print(mwin)
        return False
    if resetit(l[i]):
        print(msuc)
    else:
        print(merr)


def cli():
    if name != 'nt' and getuid() != 0:
        print('#' * 4 + ' You must use sudo for this to work properly ' +
              '#' * 4)
    if len(argv) > 1:
        listt()
    else:
        intera()


if __name__ == '__main__':
    cli()
