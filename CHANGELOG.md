# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [4.0.1] - 2025-03-11
- Added support for Mongo 7.0
- Added capability to connect directly to single server in replica set.
- Updated mongo-lib v4.5.1

### Fixed
- Fixed pre-header where to determine which python version to use.

### Changed
- Added direct_connect to config/mongo.py configuration file.
- Documentation changes.

### Removed
- Mongo 3.4 support.


## [4.0.0] - 2025-01-28
Breaking Changes

- Removed support for Python 2.7.
- Add pre-header check on allowable Python versions to run.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Updated python-lib v4.0.0
- Updated mongo-lib v4.4.0

### Changed
- Converted strings to f-strings.
- mongo_generic: Added encoding argument to open calls.
- Documentation changes.

### Deprecated
- Support for Mongo 3.4


## [3.3.7] - 2024-11-20
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Deprecated
- Support for Python 2.7


## [3.3.6] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson==3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.5


## [3.3.5] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [3.3.4] - 2024-04-22
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- Documentation changes.


## [3.3.3] - 2024-04-17
- Added TLS capability
- Updated mongo-lib to v4.3.0

### Changed
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS connection entries and type of connection entry.
- Documentation changes.


## [3.3.2] - 2024-02-26
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [3.3.1] - 2023-10-11
- Upgraded mongo-lib to v4.2.7 to fix an error in the create_cmd call.


## [3.3.0] - 2023-09-21
- Upgraded python-lib to v2.10.1
- Replaced the arg_parser code with gen_class.ArgParser code.

### Changed
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main, mongo_generic: Removed gen_libs.get_inst call.


## [3.2.3] - 2023-05-25
- Added -i option to turn off TLS checking if using SSL.

### Fixed
- main: Added "-i" option to the opt_arg_list list.


## [3.2.2] - 2022-12-01
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded mongo-lib to v4.2.2
 
### Changed
- Converted imports to use Python 2.7 or Python 3.
- mongo_dump, mongo_export, get_req_options: Converted dictionary keys() call to list.


## [3.2.1] - 2022-04-04
- Upgraded mongo-lb to v4.2.1

### Changes
- mongo_generic: Added standard error output for dump process and call process_log_file function.
- mongo_dump: Added error log file for any errors produced during dump.
- mongo_export: Added error log file for any errors produced during export.
- config/mongo.py.TEMPLATE: Removed use_arg and use_uri configuration entries.
- Documentation changes.

### Add
- process_log_file: Checks and processes the log file to standard out and mail.


## [3.2.0] - 2020-12-16
- Added Mongo export capability.

### Fixed
- mongo_generic:  Passed option instead of directory path mongo_libs.create_cmd call.

### Added
- mongo_export:  Setup Mongo Export call.
- mongo_generic:  Create a mongo dump/export command and execute it.

### Changed
- mongo_generic:  Passing in password via a second standard-in pipe.
- config/mongo.py.TEMPLATE:  Added SSL configuration entries.
- get_req_options:  Removed \*\*kwargs is not required.
- mongo_dump:  Refactored function to use the mongo_generic function for dumping.
- main:  Removed "-A" from opt_con_req_list as "-o" option is now a required option.
- main:  Replaced arg_parser.arg_req_xor with arg_parser.arg_xor_dict to allow for multiple Xor checks.
- main:  Added "-E" option to execute mongoexport.
- Documentation updates.


## [3.1.0] - 2020-08-13
- Verified to work with pymongo v3.8.0.
- Updated to be used in FIPS 140-2 environment.
- Added authentication mechanism for logging into Mongo.
- Replaced "-a" option with Mongo configuration file setting.

### Added
- Added standard out suppression option.
- Added program lock to prevent multiple dump runs concurrently.
- Added email capability to allow standard out and standard error to be emailed.

### Fixed
- run_program:  Removed the standard out suppression for error printing.
- main:  Made "-o" option a required argument.
- main:  Fixed handling command line arguments from SonarQube scan finding.

### Changed
- run_program:  Capture and process connection status.
- get_req_options:  Assigns configuration entry values to required options.
- run_program:  Added call to create required options list and pass to function.
- main:  Removed "-a" options from system variables.
- main:  Added arg_req_dict which contains link between config entry and required option.
- run_program:  Replaced cmds_gen.disconnect with mongo_libs.disconnect.
- mongo_dump:  Added err_flag and err_msg status variables.
- config/mongo.py.TEMPLATE:  Added authentication mechanism entries to config file.
- mongo_dump, run_program: Added standard out suppression code.
- mongo_dump:  Add email capability for dumps for standard out and error reporting.
- mongo_dump:  Redirected subprocess stderr to file for printing to standard out.
- mongo_dump:  Replaced cmds_gen.run_prog with subprocess code to run dump command.
- sync_cp_dump:  Add email capability for dumps error/warnings detected.
- run_program:  Setup and configured email.
- main:  Added -e and -s options for email capability.
- main:  Added -y option and program lock instance.
- run_program:  Change variable to standard naming convention.
- Documentation updates.

### Removed
- Removed "-a" option, replaced with entry in configuration file.
- lib.cmds_gen library module - no longer required.


## [3.0.2] - 2019-09-30
### Fixed
- sync_cp_dump, mongo_dump, run_program:  Fixed problem with mutable default arguments issue.

### Changed
- main:  Refactored "if" statements.
- sync_cp_dump, mongo_dump, run_program:  Changed variable to standard naming convention.
- Documentation changes.


## [3.0.1] - 2018-11-29
### Changed
- Documentation changes.


## [3.0.0] - 2018-04-24
Breaking Change

### Changed
- Changed "mongo_libs" calls to new naming schema.
- Changed "cmds_gen" calls to new naming schema.
- Changed "gen_libs" calls to new naming schema.
- Changed "arg_parser" calls to new naming schema.
- Changed function names from uppercase to lowercase.
- Setup single-source version control.


## [2.2.0] - 2018-04-24
Breaking change

### Added
- Changed "svr_mongo" to "mongo_class" module reference.
- Changed "cmds_mongo" to "mongo_libs" module reference.
- Added single-source version control.


## [2.1.0] - 2017-08-17
### Update
- Help_Message:  Replace docstring with printing the programs \_\_doc\_\_.
- Change single quotes to double quotes.
- Convert program to use local libraries from ./lib directory.


## [2.0.0] - 2017-01-20
Breaking change

### Added
- New Option:  Changed the quiet mode from off being default to on being default.  Set up as -q option.
- New Option:  Include users and roles in dumps on individual dumps. Set up as -r option.
- New Option:  Allow for dumping of individual collections.  Set up as -t option.

### Changed
- Made a number of major modifications.
- Moved from old libraries to new libraries and removed local functions to use library functions instead and removed multiple sys.exit commands.
- Set up error conditions processing for several functions.
- Removed Crt_Dump_Cmd function and several libraries as they are no longer required.

### Fixed
- To dump a individual database requires --authenticationDatabase option to be set, this is being included as the -a option.


## [1.0.0] - 2016-02-09
- Initial creation.

