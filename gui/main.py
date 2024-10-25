import tkinter as tk
from PIL import ImageTk, Image
import MainForm

root = tk.Tk()

upload_logo = Image.open("upload.png")
upload_logo = upload_logo.resize((60, 50))
upload_logo = ImageTk.PhotoImage(upload_logo)

logo = Image.open("Beans.png")
logo = logo.resize((300, 300))
logo = ImageTk.PhotoImage(logo)
root.state("zoomed")
root.title("Dry Beans Classification")
root['background'] = '#0e1118'
main = MainForm.DryBeanClassifierApp(root, logo, upload_logo)
root.mainloop()
