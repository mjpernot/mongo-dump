#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
test/unit/mongo_db_dump/get_req_options.py
test/unit/mongo_db_dump/help_message.py
test/unit/mongo_db_dump/main.py
test/unit/mongo_db_dump/mongo_dump.py
test/unit/mongo_db_dump/mongo_generic.py
test/unit/mongo_db_dump/run_program.py
test/unit/mongo_db_dump/sync_cp_dump.py
