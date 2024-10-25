import tkinter as tk
from PIL import ImageTk, Image
from gui import MainForm
from models import BuildModel
from models import Adaline
from models import Perceptron
from models.Evaluation import *

root = tk.Tk()

upload_logo = Image.open("gui/upload.png")
upload_logo = upload_logo.resize((60, 50))
upload_logo = ImageTk.PhotoImage(upload_logo)

logo = Image.open("gui/Beans.png")
logo = logo.resize((300, 300))
logo = ImageTk.PhotoImage(logo)
root.state("zoomed")
root.title("Dry Beans Classification")
root['background'] = '#0e1118'
main = MainForm.DryBeanClassifierApp(root, logo, upload_logo)
root.mainloop()

# model = BuildModel.BuildModel()
# model.model = Adaline.Adaline()
# model.labels = ['BOMBAY', 'SIRA']
# model.features = ['roundnes', 'MinorAxisLength']
# model.include_bias = False
# model.model.include_bias = False
# model.build()
#
#
# model.plot()

# class1 = 'BOMBAY'
# class2 = 'SIRA'
