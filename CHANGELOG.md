# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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

