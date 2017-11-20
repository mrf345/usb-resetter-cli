from sys import exit, exc_info
from app import cli

try:
    cli()
except Exception:
    print(exc_info()[1])
    print("Error: something went wrong ..")
    print("Tell me about it: https://github.com/mrf345/usb-resetter-cli")
exit(0)
