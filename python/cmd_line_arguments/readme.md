command_line_arguments and Environment variables

#Python Command Line Arguments provides a convenient way to accept some information at the command line while running the program

$ python script.py arg1 arg2 arg3

Here Python script name is script.py and rest of the three arguments - arg1 arg2 arg3 are command line arguments for the program.



Secure method of storing sensitive information is in Env_Variables

example:
Password
APIkey
Token
Certificate



Environment Variables


There is a fixed number of environment variables that Python recognizes and these generally are processed before the command line switches.

Environment variables play a crucial role in Python programming. They provide a way to store and access configuration values, system-specific information, and sensitive data

Use case
nvironment variables are commonly used in software development to configure applications based on the specific environment in which they are deployed. For example, an application may use environment variables to store database connection strings, API keys, file paths, or other settings that can vary across different environments (like development, staging, or production).

os is the modules used to interafct with the python script

The os.environ dictionary allows us to access all the environment variables set on our system


To retrieve an environment variable without causing an error if it doesn't exist, we can use the os.environ.get() method.