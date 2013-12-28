python-acpi
===========

Python acpi parser library

__Author__: Ondrej Sika, <http://ondrejsika.com>, <ondrej@ondrejsika.com>

__GitHub__: <https://github.com/ondrejsika/python-acpi>

__PyPI__: <http://pypi.python.org/pypi/acpi>


Documentation
-------------

### Installation

```
pip install acpi
```

### Functions
#### acpi.acpi()

Response is list tuples of batteries. Each tuple includes battery name, status, battery level in percent, remaining time in seconds and strin uptime.
`

### Usage
``` python
>>> import acpi
>>> acpi.acpi()
[('Battery 0', 'Discharging', 99, 10942, "08:13:45")]
```
