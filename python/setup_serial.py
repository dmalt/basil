from __future__ import annotations
import sys
from typing import Optional

from serial.tools import list_ports  # type: ignore

BAUDRATE = 9600
TIMEOUT = 0.1


class NoAvailablePortsError(Exception):
    pass


def choose_port(choice: Optional[int] = None) -> list_ports.SysFS:
    ports = list_ports.comports()
    ports.sort()
    if not ports:
        print("No ports found")
        raise NoAvailablePortsError()
    if choice is not None and choice <= len(ports):
        return ports[choice]
    print("\t".join(f"{i + 1} -> {p}" for i, p in enumerate(ports)))
    while response := input("Choose port ('q' for exit): ") != "q":
        try:
            i_port = int(response) - 1
            return ports[i_port]
        except (ValueError, IndexError):
            pass
    return sys.exit(1)


port = choose_port(0)
