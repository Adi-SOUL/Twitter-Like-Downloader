import asyncio
import os
import threading
from info_from_twitter.get_img_link import get_links
from info_from_twitter.get_id import get_id_through_name
from info_from_twitter.get_liked import write_like
from info_from_twitter.download import download
from requests.exceptions import ConnectTimeout, SSLError
from time import sleep, asctime
from UI import *
from tkinter.filedialog import askdirectory
import json

os.environ['BEARER_TOKEN'] = ''
os.environ['TWITTER_ID'] = ''


class TwitterDownloader(TwitterUi):
	def __init__(self):
		super().__init__()
		self.event = threading.Event()
		self.stop = False
		self.started = False
		self.t = None
		self.json_dict = {}
		self.load_json()

		self.token = ttk.StringVar()
		self.input_token_entry.configure(textvariable=self.token, show='*')
		self.token.set(self.json_dict["TOKEN"])

		self.tw_id = ttk.StringVar()
		self.input_id_entry.configure(textvariable=self.tw_id)
		self.tw_id.set(self.json_dict["ID"])

		self.dir = ttk.StringVar()
		self.dir_entry.configure(textvariable=self.dir)
		self.dir.set(self.json_dict["DIR"])

		self._sleep = ttk.StringVar()
		self.sleep_entry.configure(textvariable=self._sleep)
		self._sleep.set(self.json_dict["SLEEP"])

		self.times = ttk.StringVar()
		self.times_entry.configure(textvariable=self.times)
		self.times.set(self.json_dict["TIMES"])

		self.start.configure(command=self.token_button_func)

	def load_json(self) -> None:
		with open('./config.json', 'r', encoding='utf-8') as json_file:
			self.json_dict = json.load(json_file)
		try:
			os.environ['BEARER_TOKEN'] = self.json_dict["TOKEN"]
			try:
				os.environ['TWITTER_ID'] = self.json_dict[self.json_dict["ID"]]
			except KeyError:
				twitter_id = get_id_through_name(self.json_dict["ID"])
				self.json_dict[self.json_dict["ID"]] = twitter_id
				os.environ['TWITTER_ID'] = twitter_id
		except Exception as e:
			if self.json_dict["TOKEN"] == "" or self.json_dict["ID"] == "":
				pass
			else:
				self.log.error(e)

	def token_button_func(self, info: bool = True) -> None:
		if self.started:
			return
		token = self.token.get()
		os.environ['BEARER_TOKEN'] = token
		self.json_dict["TOKEN"] = token
		if info:
			self.log.info('SUCCESS')

	def id_button_func(self, info: bool = True) -> None:
		if self.started:
			return
		name = self.tw_id.get()
		try:
			os.environ['TWITTER_ID'] = self.json_dict[name]
			if info:
				self.log.info('SUCCESS')
		except KeyError:
			os.environ['TWITTER_ID'] = get_id_through_name(name)
			self.json_dict["ID"] = name
			if info:
				self.log.info('SUCCESS')
		except Exception as e:
			self.log.error(e)

	def dir_button_func(self) -> None:
		if self.started:
			return
		_dir = askdirectory()
		if _dir:
			self.dir.set(_dir)
			self.json_dict["DIR"] = _dir

	def sleep_button_func(self) -> None:
		if self.started:
			return
		self.json_dict["SLEEP"] = self._sleep.get()

	def times_button_func(self) -> None:
		if self.started:
			return
		self.json_dict["TIMES"] = self.times.get()

	async def one_loop(self) -> None:
		save_path = self.dir.get()
		try:
			path_list = []
			legal_id = []
			self.log.info(f'[{asctime()}]: [Info]Getting img urls...')
			res = get_links()
			if not res:
				return
			for items in res:
				urls = items[0]
				name = items[1]
				_id = items[2]
				for url in urls:
					self.log.info(f'[{asctime()}]: [Info]Downloading from: \n{url}\nThe author is:{name}.')
					path = await download(dir_name=name, url=url, dir_path=save_path)
					path_list.append((path, _id))

			self.log.info(f'[{asctime()}]: [Info]Checking for downloads...')
			sleep(30)
			flag = False
			for path, _id in path_list:
				if os.path.exists(path):
					if _id not in legal_id:
						legal_id.append(_id)
					else:
						pass
				else:
					self.log.error(f'[{asctime()}]: [Error]Something went wrong...')
					flag = True
					break

			if not flag:
				self.log.info(f'[{asctime()}]: [Info]Download Finished.')
				write_like(legal_id)

		except (ConnectTimeout, SSLError):
			self.log.error(f'[{asctime()}]: [Error]Can not connect to Twitter.')

	def main_func(self) -> None:
		__loop = asyncio.new_event_loop()
		times = int(self.times.get()) if int(self.times.get()) != -1 else 2147483647
		sleep_min = self._sleep.get()
		index = 1
		while True:
			if self.stop:
				break
			asyncio.set_event_loop(__loop)
			__loop.run_until_complete(self.one_loop())
			index += 1
			if index > times:
				self.started = False
				self.log.info(f'[{asctime()}]: [Info]ALL FINISHED')
				break
			self.log.info(f'[{asctime()}]: [Info]Sleeping...')
			self.event.wait(float(sleep_min) * 60)

	def loop(self):
		if self.started:
			return

		self.token_button_func(False)
		self.id_button_func(False)

		self.started = True
		self.t = threading.Thread(target=self.main_func)
		self.t.start()

	def __close(self) -> None:
		with open('./config.json', 'w', encoding='utf-8') as json_file:
			json.dump(self.json_dict, json_file, indent=4)
		self.win.destroy()
		self.stop = True
		self.event.set()
		exit()

	def run(self):
		self.input_token_button.configure(command=self.token_button_func)
		self.input_id_button.configure(command=self.id_button_func)
		self.dir_button.configure(command=self.dir_button_func)
		self.sleep_button.configure(command=self.sleep_button_func)
		self.times_button.configure(command=self.times_button_func)

		self.win.protocol("WM_DELETE_WINDOW", self.__close)
		self.start.configure(command=self.loop)
		self.win.mainloop()


if __name__ == '__main__':
	downloader = TwitterDownloader()
	downloader.run()
