from sys import exit, exc_info
from app import cli

try:
    run()
except Exception:
    print(exc_info()[1])
    print("Error: something went wrong ..")
exit(0)
