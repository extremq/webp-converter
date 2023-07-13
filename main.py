import tkinter as tk
from tkinter import filedialog
from PIL import Image


def select_images():
    file_paths = filedialog.askopenfilenames()
    return file_paths


def convert_images(file_paths):
    if file_paths:
        for file_path in file_paths:
            img = Image.open(file_path)
            output_path = file_path.rsplit('.', 1)[0] + '.webp'
            img.save(output_path, 'webp')
        tk.messagebox.showinfo('Success',
                               f'Images converted successfully!\nCheck the original locations for the .webp files.')
    else:
        tk.messagebox.showwarning('No File', 'No file selected. Please select an image file.')


root = tk.Tk()
root.geometry('300x200')
root.title('Image to WebP Converter')

select_button = tk.Button(root, text='Select Images', command=lambda: convert_images(select_images()))
select_button.pack(expand=True)

root.mainloop()
