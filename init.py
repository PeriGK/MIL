from initialisers.logging import initialise_logging
from initialisers.database import initialise_database_connection
from conf import mil_conf

log_path = mil_conf.log_dir + mil_conf.log_file
initialise_logging(log_path, mil_conf.log_level)
initialise_database_connection(mil_conf.database)

command = input("What would you like to learn about?\n")