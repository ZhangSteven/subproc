# coding=utf-8
# 
# Call winscp from Python to do sftp job.
# 


from os.path import join
from subprocess import run
from subproc.utility import logger, get_current_path, get_winscp_directory, \
							get_winscp_log_directory


# The simplest working example to call WinSCP to download a file from a public
# sftp site. The site information is from:
# http://www.sftp.net/public-online-sftp-servers
#
# The run() method is the preferred way to invoke a subprocess since Python 3.5
# 
# The way to invoke a winscp.com program is from the bat file: sftp-upload.com
#
args = [join(get_winscp_directory(), 'WinSCP.com'), \
		'/script={0}'.format(join(get_current_path(), 'run-sftp.txt')), \
		'/log={0}'.format(join(get_winscp_log_directory(), 'upload.log'))]

result = run(args)
# result = run(args, timeout=2)
print(result)