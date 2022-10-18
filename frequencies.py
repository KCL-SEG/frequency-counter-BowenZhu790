"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in range(len(items)):
        modify_key = str(items[i])
        frequencies[modify_key] = frequencies.get(modify_key,0) + 1


    return frequencies
