"""Main function of load module
"""
from .literature import load_authors
from .literature import load_literature
from .literature import load_has_authored

def main():
    load_authors()
    load_literature()
    load_has_authored()