import tkinter
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
import logging
from ttkbootstrap.constants import *
from ttkbootstrap import utility
utility.enable_high_dpi_awareness()


class TextboxHandler(logging.Handler):
	def __init__(self, label):
		logging.Handler.__init__(self)
		self.label = label
		self.history = []

	def emit(self, record):
		message = self.format(record)
		self.history.append(message)
		self.label.config(text='\n'.join(self.history))


class TwitterUi:
	def __init__(self):
		self.log_frame_ = None
		self.log_frame = None
		self.log = logging.Logger('l')
		self.log.setLevel('INFO')
		self.id_ = 0
		self.handler = None
		self.text_box = None
		self.sleep_label = None
		self.sub_frame_2 = None
		self.sleep_entry = None
		self.sleep_button = None
		self.times_button = None
		self.times_entry = None
		self.times_label = None
		self.sub_frame_1 = None
		self.dir_button = None
		self.dir_entry = None
		self.dir_label = None
		self.dir_frame = None
		self.setting_frame = None
		self.other_frame = None
		self.win = tkinter.Tk()
		self.win.title('Adi Twitter Downloader')
		self.win.geometry('850x850')
		self.win.resizable(False, False)

		self.setup_frame = None
		self.input_id_entry = None
		self.input_id_label = None
		self.input_id_button = None
		self.input_id = None
		self.input_token_button = None
		self.input_token_entry = None
		self.input_token_label = None
		self.input_token = None
		self.entry_frame = None

		self.build_entry()
		self.build_setting()
		self.build_logging()
		self.start = ttk.Button(self.win, text='START')
		self.start.pack(side=TOP, fill=X, pady=10, padx=10)

	def build_entry(self):
		self.entry_frame = ttk.Labelframe(self.win, text='User info')

		self.input_token = ttk.Frame(self.entry_frame)
		self.input_token_label = ttk.Label(self.input_token, text='Twitter API Token:')
		self.input_token_entry = ttk.Entry(self.input_token)
		self.input_token_button = ttk.Button(self.input_token, text='OK')

		self.input_token_label.pack(side=LEFT, padx=(15, 0))
		self.input_token_entry.pack(side=LEFT, expand=YES, padx=5, fill=X)
		self.input_token_button.pack(side=LEFT, padx=5)

		self.input_id = ttk.Frame(self.entry_frame)
		self.input_id_label = ttk.Label(self.input_id, text='Twitter ID:')
		self.input_id_entry = ttk.Entry(self.input_id)
		self.input_id_button = ttk.Button(self.input_id, text='OK')

		self.input_id_label.pack(side=LEFT, padx=(15, 0))
		self.input_id_entry.pack(side=LEFT, expand=YES, padx=5, fill=X)
		self.input_id_button.pack(side=LEFT, padx=5)

		self.input_token.pack(fill=X, expand=YES)
		self.input_id.pack(fill=X, expand=YES, pady=10)
		self.entry_frame.pack(fill=BOTH, expand=NO, padx=10, side=TOP)

	def build_setting(self):
		self.setting_frame = ttk.Labelframe(self.win, text='Setting')

		self.dir_frame = ttk.Frame(self.setting_frame)
		self.dir_label = ttk.Label(self.dir_frame, text='Save path:')
		self.dir_entry = ttk.Entry(self.dir_frame)
		self.dir_button = ttk.Button(self.dir_frame, text='View path')

		self.dir_label.pack(side=LEFT, padx=(15, 0))
		self.dir_entry.pack(side=LEFT, expand=YES, padx=5, fill=X)
		self.dir_button.pack(side=LEFT)

		self.other_frame = ttk.Frame(self.setting_frame)
		self.sub_frame_1 = ttk.Frame(self.other_frame)
		self.times_label = ttk.Label(self.sub_frame_1, text='Number of cycles:')
		self.times_entry = ttk.Entry(self.sub_frame_1)
		self.times_button = ttk.Button(self.sub_frame_1, text='OK')

		self.times_label.pack(side=LEFT, padx=5)
		self.times_entry.pack(side=LEFT, expand=YES, padx=5, fill=X)
		self.times_button.pack(side=LEFT)

		self.sub_frame_2 = ttk.Frame(self.other_frame)
		self.sleep_label = ttk.Label(self.sub_frame_2, text='Interval time(min):')
		self.sleep_entry = ttk.Entry(self.sub_frame_2)
		self.sleep_button = ttk.Button(self.sub_frame_2, text='OK')

		self.sleep_label.pack(side=LEFT, padx=5)
		self.sleep_entry.pack(side=LEFT, expand=YES, padx=5, fill=X)
		self.sleep_button.pack(side=LEFT)

		self.sub_frame_1.pack(side=LEFT, padx=5, fill=X, expand=YES)
		self.sub_frame_2.pack(side=LEFT, padx=YES, fill=X, expand=YES)

		self.dir_frame.pack(padx=5, pady=5, fill=X, expand=YES)
		self.other_frame.pack(padx=5, pady=5, fill=X, expand=YES)
		self.setting_frame.pack(side=TOP, padx=10, pady=10, fill=BOTH, expand=NO)

	def build_logging(self):
		self.log_frame_ = ttk.Labelframe(self.win, text='Log')
		self.log_frame = ScrolledFrame(self.log_frame_)
		self.text_box = ttk.Label(self.log_frame, anchor=NW, font=('Consolas', 14, 'bold'))

		self.text_box.pack(padx=5, pady=5, fill=BOTH, expand=YES)
		self.log_frame.pack(fill=BOTH, expand=YES)
		self.log_frame_.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

		self.handler = TextboxHandler(self.text_box)
		self.log.addHandler(self.handler)
