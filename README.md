# usb-resetter-cli
#### basic USB resetting tool with simple command-line interface based on [PyUSB][a43ff9d9] and [Click][20250980]

  [a43ff9d9]: https://github.com/pyusb/pyusb "pyusb"
  [20250980]: https://github.com/pallets/click "Click"

### Run it :
#### `(with Python3.6) pip install requirements.txt && python run.py`

### Commands :
#### `python run.py --help`
#### `python run.py --list`
#### `python run.py --list --filter 3`
#### `python run.py --reset 0x5986 0x55e # idVendor and idProduct`

### Setup:
> Check out the documentation for setting up the USB drivers on:
> https://github.com/mrf345/usb-resetter
