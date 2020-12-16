#!/bin/bash
# Unit test code coverage for program module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#   that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/get_req_options.py
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/help_message.py
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/main.py
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/mongo_dump.py
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/run_program.py
coverage run -a --source=mongo_db_dump test/unit/mongo_db_dump/sync_cp_dump.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
