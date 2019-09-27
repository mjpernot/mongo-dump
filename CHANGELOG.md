# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


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
- Help_Message:  Replace docstring with printing the programs __doc__.
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
