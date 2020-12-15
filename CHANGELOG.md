# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [3.1.0] - 2020-08-13
- Added authentication mechanism for logging into Mongo.
- Replaced "-a" option with Mongo configuration file setting.

### Added
- run_program:  Capture and process connection status.
- get_req_options:  Assigns configuration entry values to required options.
- Added standard out suppression option.
- Added program lock to prevent multiple dump runs concurrently.
- Added email capability to allow standard out and standard error to be emailed.

### Fixed
- run_program:  Removed the standard out suppression for error printing.
- main:  Made "-o" option a required argument.
- main:  Fixed handling command line arguments from SonarQube scan finding.

### Changed
- run_program:  Added call to create required options list and pass to function.
- main:  Removed "-a" options from system variables.
- main:  Added arg_req_dict which contains link between config entry and required option.
- run_program:  Replaced cmds_gen.disconnect with mongo_libs.disconnect.
- mongo_dump:  Added err_flag and err_msg status variables.
- config/mongo.py.TEMPLATE:  Added authentication mechanism entries to config file.
- mongo_dump: Added standard out suppression code.
- run_program: Added standard out suppression code.
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
- sync_cp_dump:  Fixed problem with mutable default arguments issue.
- mongo_dump:  Fixed problem with mutable default arguments issue.
- run_program:  Fixed problem with mutable default arguments issue.

### Changed
- main:  Refactored "if" statements.
- sync_cp_dump:  Changed variable to standard naming convention.
- mongo_dump:  Changed variable to standard naming convention.
- run_program:  Changed variable to standard naming convention.
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

