#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 32
print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) 