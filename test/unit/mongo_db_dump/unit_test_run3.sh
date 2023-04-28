#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 test/unit/mongo_db_dump/get_req_options.py
/usr/bin/python3 test/unit/mongo_db_dump/help_message.py
/usr/bin/python3 test/unit/mongo_db_dump/main.py
/usr/bin/python3 test/unit/mongo_db_dump/mongo_dump.py
/usr/bin/python3 test/unit/mongo_db_dump/mongo_export.py
/usr/bin/python3 test/unit/mongo_db_dump/mongo_generic.py
/usr/bin/python3 test/unit/mongo_db_dump/process_log_file.py
/usr/bin/python3 test/unit/mongo_db_dump/run_program.py
/usr/bin/python3 test/unit/mongo_db_dump/sync_cp_dump.py
