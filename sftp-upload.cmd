REM *************************************************
REM ***    	Global variables 		*****
REM *************************************************
@echo off

REM *************************************************
REM ***    	SFTP Processing 		*****
REM *************************************************
SET JOBSCRIPTPATH="C:\Program Files\Git\git\subproc"
SET WINSCPPATH="C:\Program Files (x86)\WinSCP"
SET DATASOURCEPATH="C:\Program Files\Git\git\subproc\upload"

cd %DATASOURCEPATH%

REM *****  Uploading all files to SFTP ******
%WINSCPPATH%\winscp.com /script=%JOBSCRIPTPATH%\run-sftp.txt /log=%JOBSCRIPTPATH%\upload.log