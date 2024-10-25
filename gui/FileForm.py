import tkinter as tk
from tkinter import ttk

import pandas as pd

from gui import CustomButton, PredictRow, MainForm
from tkinter import filedialog
from tkinter import messagebox
import os


class FileForm:
    def __init__(self, root, upload_logo, logo):
        self.table_frame = None
        self.root = root
        self.panel = tk.Frame(root, width=350, height=900, bg="#262730")
        self.tree = None
        self.scrollbar = None
        self.drag_drop_frame = tk.Frame(root, bg="#262730", width=800, height=100)
        self.logo = logo
        self.upload_logo = upload_logo
        self.root = root
        self.model = None
        self.file_flag = False
        s = ttk.Style()
        s.theme_use('clam')

        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#78878e")


        self.create_gui()

    def create_gui(self):
        self.create_main_panel()
        self.create_drag_drop_frame()

    def create_main_panel(self):
        self.panel.place(x=0, y=0)

        tk.Label(self.panel, image=self.logo, border=0).place(x=23, y=100)
        tk.Label(self.panel, text="Dry Bean Classifier", bg="#262730", fg="#fff", font=("bold", 18), border=0).place(
            x=70, y=430)

        row_prediction_button = CustomButton.CustomButton(self.panel, "Get Row Prediction")
        row_prediction_button.btn.config(command=self.PredictRow)
        row_prediction_button.place(x=80, y=550)

        build_model_button = CustomButton.CustomButton(self.panel, "      Build Model      ")
        build_model_button.btn.config(command=self.ToBuildModel)
        build_model_button.place(x=80, y=650)

    def PredictRow(self):
        self.destroy()
        obj = PredictRow.PredictRow(self.root, self.logo, self.upload_logo)
        obj.model = self.model

    def ToBuildModel(self):
        self.destroy()
        obj = MainForm.DryBeanClassifierApp(self.root, self.logo, self.upload_logo)
        obj.model_built = True
        obj.model = self.model

    def browse_file(self):
        try:
            if self.file_flag:
                self.scrollbar.destroy()
                self.table_frame.destroy()
                self.tree.destroy()

            file_path = filedialog.askopenfilename(
                filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")]
            )
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension == ".xlsx":
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)
            columns = list(df.columns)
            columns.append('Class')
            self.table_frame = tk.Frame(self.root, bg="white", width=800, height=44)
            self.tree = ttk.Treeview(self.table_frame, columns=columns, show='headings', height=20)
            self.scrollbar = ttk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tree.yview)
            self.create_table_frame(df)
            self.file_flag=True
        except:
            messagebox.showerror("error", "Something Wrong!")



    def create_drag_drop_frame(self):

        self.drag_drop_frame.place(x=550, y=100)

        tk.Label(self.drag_drop_frame, image=self.upload_logo, border=0).place(x=25, y=20)

        tk.Label(self.drag_drop_frame, text="Drag and drop file here", bg="#262730", fg="#fff", border=0).place(x=110, y=25)
        tk.Label(self.drag_drop_frame, text="Get instant classification for the whole file samples", bg="#262730",
                 fg="#78878e", border=0).place(x=110, y=50)

        btn = CustomButton.CustomButton(self.drag_drop_frame, "Browse Files")
        btn.btn.config(command=self.browse_file)
        btn.place(x=600, y=28)

    def create_table_frame(self, df):
        self.table_frame.place(x=550, y=300)

        columns = list(df.columns)
        columns.append('Class')


        j = 0
        for i in columns:
            self.tree.column(j, anchor=tk.CENTER, width=130)
            self.tree.heading(j, text=i, anchor=tk.CENTER)
            j+=1

        # generate sample data
        data = []
        j=0
        for idx in range(len(df)):
            row = pd.DataFrame(df.iloc[[idx]])
            row.reset_index(inplace=True, drop=True)
            # row = pd.DataFrame(row, columns=df.columns, index=[0])
            s = []
            print(row.head())
            for column in list(df.columns):
                s.append(row.loc[0, column])

            row = self.model.preprocess_x(row)


            pred = self.model.model.predict(row)
            if pred[0] == -1:
                for i in range(len(pred)):
                    pred[i] = 0
            tmp = self.model.label_encoder.inverse_transform(pred)[0]
            s.append(tmp)
            self.tree.insert('', tk.END, values=tuple(s))
            data.append(tuple(s))
            j+=1
            # data.append((f'{df[idx][df.columns]}', f'last {n}', f'email{n}@example.com', 'tmp1', 'tmp2', 'tmp3'))

        # add data to the treeview
        # for contact in data:
        #     self.tree.insert('', tk.END, values=contact)

        self.tree.grid(row=0, column=0, sticky='nsew')


        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')


    def destroy(self):
        self.panel.destroy()
        self.tree.destroy()
        self.drag_drop_frame.destroy()
        self.scrollbar.destroy()
        self.table_frame.destroy()


