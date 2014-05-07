"""
Tests added by robertmuil.
"""
from acpi import adapters

def adapters_test():
    data = adapters()
    assert(len(data)>0)
    assert(data[0][0] == 'Adapter 0')
    assert(data[0].name == 'Adapter 0')

# vim: expandtab:sw=4:ts=4
