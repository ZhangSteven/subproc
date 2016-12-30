# coding=utf-8
# 
# Call winscp from Python to do sftp job.
# 


from os.path import join
from subprocess import run, TimeoutExpired, CalledProcessError
from subproc.utility import logger, get_current_path, get_winscp_directory, \
							get_winscp_log_directory, dt_string_to_datetime


# The simplest working example to call WinSCP to download a file from a public
# sftp site. The site information is from:
# http://www.sftp.net/public-online-sftp-servers
#
# The run() method is the preferred way to invoke a subprocess since Python 3.5
# 
# The way to invoke a winscp.com program is from the bat file: sftp-upload.com
#
def get_file():
	args = [join(get_winscp_directory(), 'WinSCP.com'), \
			'/script={0}'.format(join(get_current_path(), 'run-sftp.txt')), \
			'/log={0}'.format(join(get_winscp_log_directory(), 'winscp.log'))]

	result = run(args)
	print(result)



def get_file_error():
	"""
	Get 3 files:
	file1 (good)
	file2 (does not exist)
	file3 (good)

	The observation: file1 get successfully, file2 cause error, sftp session
	then stops, so file3 not downloaded.
	"""
	args = [join(get_winscp_directory(), 'WinSCP.com'), \
			'/script={0}'.format(join(get_current_path(), 'run-sftp-error.txt')), \
			'/log={0}'.format(join(get_winscp_log_directory(), 'winscp.log'))]

	result = run(args, check=True)	# check for return code, if it is non-zero,
									# then raise CalledProcessError
	print(result)	# never executed due to exception raised, if check=False (default),
					# then we can see the result



def get_file_timeout():
	"""
	Get 2 files, but with a timeout of 3 seconds.
	"""
	args = [join(get_winscp_directory(), 'WinSCP.com'), \
			'/script={0}'.format(join(get_current_path(), 'run-sftp-2files.txt')), \
			'/log={0}'.format(join(get_winscp_log_directory(), 'winscp.log'))]

	result = run(args, timeout=25, check=True)	# check for time out and return
												# code.
	print(result)	# never executed due to exception raised



def read_log(winscp_log):
	"""
	Look for successful transfer records in the winscp logfile, then report
	which files are successfully transferred, and the date and time those
	transfers are completed.

	The successful transfer records are in the following format (get and put)

	> 2016-12-29 17:20:40.652 Transfer done: '<file full path>' [xxxx]

	The starting symbol can be '>', '<', '.', '!', depending on the type of
	the record.

	If it is a get, then 'file full path' will be the remote directory's
	file path. If it is a put, then 'file full path' will be the local
	directory's file path.
	"""
	result = {}
	with open(winscp_log) as f:
		for line in f:
			tokens = line.split()
			# print(tokens)
			if len(tokens) < 6:
				continue

			if tokens[3] == 'Transfer' and tokens[4] == 'done:':
				dt = dt_string_to_datetime(tokens[1] + ' ' + tokens[2].split('.')[0])
				result[tokens[5][1:-1]] = dt

	return result



if __name__ == '__main__':
	try:
		# get_file()
		get_file_timeout()
		# get_file_error()
		
		print('working OK')
	except TimeoutExpired as e:
		print('process timeout within {0} seconds'.format(e.timeout))
	except CalledProcessError as e:
		print('process error code {0}'.format(e.returncode))
		print('error message stdout: {0}'.format(e.stdout))	# does not get anything
		print('error message stderr: {0}'.format(e.stderr))	# does not get anything
	finally:
		print(read_log(join(get_winscp_log_directory(), 'winscp.log')))


