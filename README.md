# Python project for dumping a database on a Mongo database.
# Classification (U)

# Description:
  This used to dump a database on a Mongo database server, to include running a sync/copy dump or dumping a Mongo database via mongodump program.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Description
  * Program Help Function
  * Help Message
  * Testing
    - Unit
    - Integration
    - Blackbox


# Features:
  * Dump Mongo database via sync/copy.
  * Dump Mongo database via mongodump program.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-dump.git
```

Install/upgrade system modules.

```
cd mongo-dump
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.

```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```


# Program Descriptions:
### Program: mongo_db_dump.py
##### Description: Performance monitoring program for a Mongo database.


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}/mongo-dump/mongo_db_dump.py -h
```


# Help Message:
  Below is the help message for the program.  Recommend running the -h option on the command line to see the latest help message.

    Program:  mongo_db_dump.py

    Description:  The mongo_db_dump program runs dumps against a Mongo database
        and depending on which type of dump is selected can dump individual
        databases.

    Usage:
        mongo_db_dump.py -c file -d path {-M [-z | -b name [-r | -t name] |
            -l] | -A} [-o name | -p path | -s | -z | -q] [-v | -h] 

    Arguments:
        -c file => Server configuration file.  Required arg.
        -d dir path => Directory path to config file (-c). Required arg.
        -o dir path => Directory path to dump directory.
        -p dir path => Directory path to mongo programs.  Only required if the
            mongo binary programs do not run properly.  (i.e. not in the $PATH
            variable.)
        -M => Run the mongodump program.
        -A => Run the Sync/Copy dump program.
            NOTE:  -A and -M are XOR required arguments.
        -z => Compress database dump.  Only for -M option.
        -l => Oplog option added to mongodump.  Only for -M option and
            database must also be part of a replica set.
        -b database => Database name.  Only for -M option.
        -t table => Collection name.  Only available for -b.
        -a database => Name of authenication database.  Required for -b.
        -r => Include user and roles in dump.  Only available for -b.
        -q => Turn quiet mode on.  By default, displays out log of dump.
        -v => Display version of this program.
        -h => Help and usage message.
            NOTE:  -v or -h overrides the other options.

    Notes:
        Mongo configuration file format (mongo.py).  The configuration
            file format for the Mongo connection used for inserting data into
            a database.  There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "root"
            passwd = "ROOT_PASSWORD"
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            port = PORT_NUMBER (default of mysql is 27017)
            conf_file = None
            auth = True

            2.)  Replica Set connection:  Same format as above, but with these
                additional entries at the end of the configuration file:
            
            repset = "REPLICA_SET_NAME"
            repset_hosts = "HOST1:PORT, HOST2:PORT, HOST3:PORT, [...]"
            db_auth = "AUTHENTICATION_DATABASE"

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_dump.py -a -c mongo -d config -o /db_dump -z -M -l


# Testing:


# Unit Testing:

### Description: Testing consists of unit testing for the functions in the mongo_db_dump.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-dump.git
```

Install/upgrade system modules.

```
cd mongo-dump
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Unit test runs for mongo_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-dump
```

### Unit:  help_message
```
test/unit/mongo_db_dump/help_message.py
```

### Unit:  
```
test/unit/mongo_db_dump/
```

### Unit:  
```
test/unit/mongo_db_dump/
```

### Unit:  run_program
```
test/unit/mongo_db_dump/run_program.py
```

### Unit:  main
```
test/unit/mongo_db_dump/main.py
```

### All unit testing
```
test/unit/mongo_db_dump/unit_test_run.sh
```

### Code coverage program
```
test/unit/mongo_db_dump/code_coverage.sh
```


# Integration Testing:

### Description: Testing consists of integration testing of functions in the mongo_db_dump.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-dump.git
```

Install/upgrade system modules.

```
cd mongo-dump
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.
```
cd test/integration/mongo_dump/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Integration test runs for mongo_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-dump
```


### Integration:  
```
test/integration/mongo_db_dump/
```

### All integration testing
```
test/integration/mongo_db_dump/integration_test_run.sh
```

### Code coverage program
```
test/integration/mongo_db_dump/code_coverage.sh
```


# Blackbox Testing:

### Description: Testing consists of blackbox testing of the mongo_db_dump.py program.

### Installation:

Install this project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-dump.git
```

Install/upgrade system modules.

```
cd mongo-dump
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

### Configuration:

Create Mongodb configuration file.

```
cd test/blackbox/mongo_dump/config
cp ../../../../config/mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"

  * If connecting to a Mongo replica set, otherwise set to None.
    - repset = "REPLICA_SET_NAME"
    - repset_hosts = "HOST_1:PORT, HOST_2:PORT, ..."
    - db_auth = "AUTHENTICATION_DATABASE"

```
vim mongo.py
chmod 600 mongo.py
```

# Blackbox test run for mongo_db_dump.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-dump
```

### Blackbox:  
```
test/blackbox/mongo_db_dump/blackbox_test.sh
```

