#!/bin/env/py

from src.server import run
import logging
import logging.config

logging.config.fileConfig('logging.conf')

if __name__ == "__main__":
    import sys
    run()



