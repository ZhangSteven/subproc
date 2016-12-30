# coding=utf-8
# 
# from config_logging package, provides a config object (from config file)
# and a logger object (logging to a file).
# 

import configparser, os
from config_logging.file_logger import get_file_logger
from datetime import datetime



def get_current_path():
	"""
	Get the absolute path to the directory where this module is in.

	This piece of code comes from:

	http://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
	"""
	return os.path.dirname(os.path.abspath(__file__))



def _load_config(filename='subproc.config'):
	"""
	Read the config file, convert it to a config object. The config file is 
	supposed to be located in the same directory as the py files, and the
	default name is "config".

	Caution: uncaught exceptions will happen if the config files are missing
	or named incorrectly.
	"""
	path = get_current_path()
	config_file = path + '\\' + filename
	# print(config_file)
	cfg = configparser.ConfigParser()
	cfg.read(config_file)
	return cfg



# initialized only once when this module is first imported by others
if not 'config' in globals():
	config = _load_config()



def get_base_directory():
	"""
	The directory where the log file resides.
	"""
	global config
	directory = config['logging']['directory']
	if directory == '':
		directory = get_current_path()

	return directory



def _setup_logging():
    fn = get_base_directory() + '\\' + config['logging']['log_file']
    log_level = config['logging']['log_level']
    return get_file_logger(fn, log_level)



# initialized only once when this module is first imported by others
if not 'logger' in globals():
	logger = _setup_logging()



def get_winscp_directory():
	global config
	return config['directory']['winscp']



def get_winscp_log_directory():
	global config
	if config['directory']['winscp_log'] == '':
		return get_current_path()
	else:
		return config['directory']['winscp_log']



def dt_string_to_datetime(dt_string):
	"""
	Copied from reconciliation_helper.record.py.

	convert a string in 'yyyy-mm-dd hh:mm:ss' format to a datetime
	object.
	"""
	dt_token = dt_string.split()[0]
	tm_token = dt_string.split()[1]
	year, month, day = parse_string(dt_token, '-')
	hour, minute, second = parse_string(tm_token, ':')
	return datetime(year, month, day, hour=hour, minute=minute, second=second)



def parse_string(a_string, separator):
	"""
	Copied from reconciliation_helper.record.py.

	Convert string of form 'yyyy-mm-dd' or 'hh-mm-ss' into three
	integers.
	"""
	a_list = a_string.split(separator)
	return int(a_list[0]), int(a_list[1]), int(a_list[2])
