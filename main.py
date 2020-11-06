from tkinter import *
from tkinter import filedialog
from pytube import YouTube


def explore_files():
	files = [('video_files', '*.mp4*'), ]
	file = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
	download(file)

def download(path):

	url = entry.get()
	youtube = YouTube(url)
	stream = youtube.streams.first()
	stream.download(path)


def main():
	global entry

	root = Tk()
	root.geometry('600x400')
	root.resizable(False, False)
	root.title('Youtube Downloader')
	root.configure(background='grey')

	frame = Frame(root, bg='grey')

	label = Label(frame,
		text='Enter the video URL: ',
		font=('Times', 20, 'underline'),
		bg='grey'
	)

	entry = Entry(frame,
		width=34,
		font=('Times', 20),
		bd=3,
		fg='Green'
	)

	exitButton = Button(frame,
		text='exit',
		width=12, 
		bd=3,
		fg='white',
		bg='red',
		font=('Times', 15, 'bold'),
		command=root.quit
	)

	downloadButton = Button(frame,
		text='download',
		width=12, 
		bd=3,
		fg='white',
		bg='LightGreen',
		font=('Times', 15, 'bold'),
		command=explore_files
	)

	frame.pack(padx=10)

	label.grid(row=0, column=0, pady=20)
	entry.grid(row=1, column=0, columnspan=2, pady=20)
	exitButton.grid(row=3, column=0, pady=60)
	downloadButton.grid(row=3, column=1)

	root.mainloop()	

main()
