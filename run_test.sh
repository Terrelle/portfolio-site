#!/bin/bash

# add to the existing tests to ensure all the new features are 
# working as expected and old features remain fully functional.

$PWD/python3venv/bin/python -m unittest discover -v tests/