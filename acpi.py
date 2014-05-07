"""

Updated by robertmuil
 - allow options to be passed to command.
 - added ac adapter function.
 - added namedtuple ability to acpi function
 - aliased acpi to batteries

"""
import os
import time
from collections import namedtuple

Battery = namedtuple('Battery', ['name', 'status', 'level', 'uptime', 'str_uptime'])
Adapter = namedtuple('Adapter', ['name', 'status'])

#TODO: should ensure that this calls the system command to avoid
# possible problems and security issues with user environment
acpi_cmd="acpi"

def raw_acpi(options=[]):
    cmd=" ".join([acpi_cmd]+options)
    return os.popen(cmd).read()

def acpi(acpi_str=None, use_namedtuple=True):
    if not acpi_str:
        acpi_str = raw_acpi()
    data = []
    for response in acpi_str.split("\n"):
        try:               battery, response = response.split(": ", 1)
        except ValueError: break
        status, response = response.split(", ", 1)
        if status in ("Full", "Unknown"):
            level = int(response.strip("%"))
            uptime = None
            str_uptime = None
        else:
            raw_level, response = response.split(", ", 1)
            level = int(raw_level.strip("%"))
            response_split = response.split(" ")
            try:
                str_uptime = response_split[0]
                struct_uptime = time.strptime(str_uptime, "%H:%M:%S")
                uptime = 3600*struct_uptime.tm_hour + 60*struct_uptime.tm_min + struct_uptime.tm_sec
            except ValueError:
                str_uptime = None
                uptime = None
        b = Battery(battery, status, level, uptime, str_uptime)
        data.append(b if use_namedtuple else tuple(b))
    return data
batteries = acpi #just alias the function name

def adapters(acpi_str=None, use_namedtuple=True):
    """

    This simply returns the data for the AC adapters in the
    system.

    >>> data = adapters()
    >>> len(data) > 0
    True
    >>> data[0][0]
    'Adapter 0'


    """
    if not acpi_str:
        acpi_str = raw_acpi(['-a'])
    data = []
    for response in acpi_str.split("\n"):
        try:
            adptr, status = response.split(": ", 1)
        except ValueError:
            break
        a = Adapter(adptr, status)
        data.append(a if use_namedtuple else tuple(a))
    return data

def on_ac():
    """
    Determines if the primary AC adapter is plugged in or not.
    """
    data = adapters()

    return data[0][1].lower() in ['online', 'on-line']

# vim: expandtab:sw=4:ts=4
