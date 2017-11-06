from initialisers.logging import create_hourly_rotating_log
from conf import mil_conf

log_path = mil_conf.log_dir + mil_conf.log_file
create_hourly_rotating_log(log_path, mil_conf.log_level)
initialise_database_connection(mil_conf.database)