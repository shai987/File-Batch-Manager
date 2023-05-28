import subprocess 
from tkinter import filedialog
import ttkbootstrap as ttk
import threading
import os

# subprocess.Popen = used to execute a command without to wait for it to complete.

def run_batch_file(file_path):
    # run the file in separately Command Prompt
    subprocess.Popen(args=['start', '/WAIT', 'cmd', '/C', 'call', file_path], shell=True)

def edit_file(file_path):
    # open the file in order to edit 
    subprocess.Popen(args=['notepad.exe', file_path], shell=True)

def delete_file(file_path):
    # delete file
    os.remove(file_path)

def select_file(command):
    # if the command is run_batch_file the file extension will be only .bat else .bat & .txt
    file_type = ".bat" if command == run_batch_file else ".bat .txt"
    # open a file dialog box and allow the user to select a batch file or text file depends on file_type
    file_paths = filedialog.askopenfilenames(filetypes=[("Batch Files", f"*{file_type}")])
    if file_paths:
        #  allows to iterate over multiple file paths and run multiple batch files concurrently, executing them simultaneously instead of sequentially.
        for file_path in file_paths:
            # helps to run tasks concurrently or perform operations in the background without blocking the main program's execution
            thread = threading.Thread(target=command, args=(file_path,))
            thread.start()

# window
window = ttk.Window(themename='united')
window.title('Batch runner')
window.geometry('400x220+0+0')
# window.iconbitmap('python.ico')

# window sizes
window.minsize(200, 200)

# window attributes
window.attributes('-topmost', True)

# title
title = ttk.Label(master=window, text='Run batch files', font='Ariel 20 bold')
title.pack()

# my frame
frame = ttk.Frame(master=window)

# run_button
run_button = ttk.Button(master=frame, text="Select Batch File", command=lambda: select_file(run_batch_file), width=20)
run_button.pack(pady=10)

# edit_button
edit_button = ttk.Button(master=frame, text="Edit File", command=lambda: select_file(edit_file), width=20)
edit_button.pack(pady=10)

# delete_button
delete_button = ttk.Button(master=frame, text="Delete File", command=lambda: select_file(delete_file), width=20)
delete_button.pack(pady=10)

frame.pack(pady=5)

# run
window.mainloop()
