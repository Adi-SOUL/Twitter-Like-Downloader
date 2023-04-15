from subprocess import Popen, PIPE, SW_HIDE, STARTUPINFO, CREATE_NEW_CONSOLE, STARTF_USESHOWWINDOW
from time import asctime
import os


async def download(dir_name: str, url: str, dir_path: str = 'E:\\pictures\\Twitter_Pictures') -> str:
	powershell = r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe'
	path = f"{dir_path}\\{dir_name}/{asctime().replace(':', '-')}.png"
	if not os.path.exists(f"{dir_path}\\{dir_name}"):
		os.mkdir(f"{dir_path}\\{dir_name}")
	else:
		pass
	startupinfo = STARTUPINFO()
	startupinfo.dwFlags = CREATE_NEW_CONSOLE | STARTF_USESHOWWINDOW
	startupinfo.wShowWindow = SW_HIDE
	Popen(
		[powershell, f'wget -O "{path}" "{url}"'],
		stdout=PIPE,
		stderr=PIPE,
		startupinfo=startupinfo
	)
	return path
