import tkinter as tk
from gui import CustomButton, FileForm, PredictRow
from tkinter import messagebox
from models import BuildModel
from models import Adaline
from models import Perceptron



class DryBeanClassifierApp:
    def __init__(self, root, logo, upload):
        self.epochs = 0
        self.learning_rate = 0
        self.threshold = 0
        self.root = root
        self.logo = logo
        self.upload = upload
        self.panel = tk.Frame(self.root, width=350, height=900, bg="#272731")
        self.frame = tk.Frame(self.root, width=1170, height=780, highlightbackground="#272731", bg="#0e1118")
        self.checkboxDict = {}
        self.checkboxValue = {}
        self.algorithm_var = 0
        self.bias_value = -1
        self.model_data = {}
        self.model_built = False
        self.model = None
        self.acc_label1 = None
        self.acc_label2 = None
        self.create_gui()

    def create_gui(self):
        self.create_side_panel()
        self.create_frame()

    def create_side_panel(self):

        self.panel.place(x=0, y=0)

        tk.Label(self.panel, image=self.logo, border=0).place(x=23, y=100)
        tk.Label(self.panel, text="Dry Bean Classifier", bg="#262730", fg="#fff", font=("bold", 18), border=0).place(
            x=70, y=430)
        self.create_buttons(self.panel)

    def create_buttons(self, panel):
        row_prediction_button = CustomButton.CustomButton(panel, "Get row prediction")
        row_prediction_button.btn.config(command=self.PredictRow)
        row_prediction_button.place(x=80, y=550)

        get_file_btn = CustomButton.CustomButton(panel, "Get file prediction")
        get_file_btn.btn.config(command=self.ToFilePrediction)
        get_file_btn.place(x=80, y=650)

    def ToFilePrediction(self):
        try:
            if self.model_built == False:
                raise Exception()
            self.destroy()
            obj = FileForm.FileForm(self.root, self.upload, self.logo)
            obj.model = self.model
        except:
            messagebox.showerror("model error", "please, build the model first!")


    def PredictRow(self):
        try:
            if self.model_built == False:
                raise Exception()
            self.destroy()
            obj = PredictRow.PredictRow(self.root, self.logo, self.upload)
            obj.model = self.model
        except:
            messagebox.showerror("model error", "please, build the model first!")

    def create_frame(self):

        self.frame.place(x=360, y=5)

        self.create_feature_checkboxes(self.frame)
        self.create_category_checkboxes(self.frame)
        # Algorithm.get() >> 1 = perceptron , 2 = adaline
        self.create_algorithm_selection(self.frame)
        self.create_learning_parameters(self.frame)
        self.create_data_entry_button(self.frame)
        self.create_show_graph_button(self.frame)

        self.bias_value = tk.IntVar()
        checkBox_bias = tk.Checkbutton(self.frame,
                                       text="Add bais ",
                                       variable=self.bias_value,
                                       bg='#0e1118',
                                       fg='white',
                                       selectcolor='#0e1118',
                                       activebackground='#0e1118',
                                       activeforeground='white',
                                       disabledforeground='grey',
                                       font=('Helvetica', 18, 'bold'),
                                       cursor="hand2")
        checkBox_bias.place(x=10, y=450)

    def create_feature_checkboxes(self, frame):
        tk.Label(frame, text="Select two features:", bg='#0e1118', fg='white', font=('Helvetica', 18, 'bold')).place(
            x=10, y=10)
        self.create_checkbox(frame, "Area", 10, 50)
        self.create_checkbox(frame, "Perimeter", 160, 50)
        self.create_checkbox(frame, "MajorAxisLength", 360, 50)
        self.create_checkbox(frame, "MinorAxisLength", 640, 50)
        self.create_checkbox(frame, "roundnes", 910, 50)
        lst = ["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", "roundnes"]
        for j in lst:
            self.checkboxDict[j].config(command=self.features_checked)

    def features_checked(self):
        lst = ["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", "roundnes"]
        i = 0
        for j in lst:
            if self.checkboxValue[j].get() == 1:
                i += 1

        if i >= 2:
            for j in lst:
                if self.checkboxValue[j].get() != 1:
                    self.checkboxDict[j].config(state='disabled')
        else:
            for j in lst:
                self.checkboxDict[j].config(state='normal')

    def categories_checked(self):
        lst = ["Bombay", "Cali", "Sira"]
        i = 0
        for j in lst:
            if self.checkboxValue[j].get() == 1:
                i += 1

        if i >= 2:
            for j in lst:
                if self.checkboxValue[j].get() != 1:
                    self.checkboxDict[j].config(state='disabled')
        else:
            for j in lst:
                self.checkboxDict[j].config(state='normal')

    def create_category_checkboxes(self, frame):
        tk.Label(frame, text="Select two categories:", bg='#0e1118', fg='white', font=('Helvetica', 18, 'bold')).place(
            x=10, y=130)
        self.create_checkbox(frame, "Bombay", 10, 170)
        self.create_checkbox(frame, "Cali", 210, 170)
        self.create_checkbox(frame, "Sira", 410, 170)
        lst = ["Bombay", "Cali", "Sira"]
        for j in lst:
            self.checkboxDict[j].config(command=self.categories_checked)

    def create_checkbox(self, frame, text, x, y, cmd=None):
        checkbox_value = tk.IntVar(frame)
        checkbox = tk.Checkbutton(frame, text=text, variable=checkbox_value, bg='#0e1118', fg='white',
                                  selectcolor='#0e1118', activebackground='#0e1118', activeforeground='white',
                                  disabledforeground='grey', font=('Helvetica', 16, 'normal'), cursor="hand2",
                                  command=cmd)
        checkbox.place(x=x, y=y)
        self.checkboxDict[text] = checkbox
        self.checkboxValue[text] = checkbox_value

    def create_algorithm_selection(self, frame):
        tk.Label(frame, text="Select Algorithm:", bg='#0e1118', fg='white', font=('Helvetica', 18, 'bold')).place(x=10,
                                                                                                                  y=330)
        self.algorithm_var = tk.IntVar(frame)
        perceptron_radio = self.create_radio_button(frame, "Perceptron", self.algorithm_var, 1, 10, 370)
        adaline_radio = self.create_radio_button(frame, "Adaline", self.algorithm_var, 2, 210, 370)

    @staticmethod
    def create_radio_button(frame, text, variable, value, x, y):
        radio_button = tk.Radiobutton(frame, text=text, variable=variable, value=value, bg='#0e1118', fg='white',
                                      selectcolor='#0e1118', activebackground='#0e1118', activeforeground='white',
                                      disabledforeground='grey', font=('Helvetica', 16, 'normal'), cursor="hand2")
        radio_button.place(x=x, y=y)
        return radio_button

    def create_learning_parameters(self, frame):
        tk.Label(frame, text="Learning Rate", bg='#0e1118', fg='white', font=14).place(x=10, y=240)
        self.learning_rate = self.create_entry(frame, 10, 270)

        tk.Label(frame, text="Number of Epochs", bg='#0e1118', fg='white', font=14).place(x=360, y=240)
        self.epochs = self.create_entry(frame, 360, 270)

        tk.Label(frame, text="MSE Threshold", bg='#0e1118', fg='white', font=14).place(x=710, y=240)
        self.threshold = self.create_entry(frame, 710, 270)

    @staticmethod
    def create_entry(frame, x, y):
        entry = tk.Entry(frame, bg='#272731', fg='white', insertbackground='white', borderwidth=5,
                         font=('Helvetica', 14, 'normal'), relief=tk.FLAT)
        entry.place(x=x, y=y)
        return entry

    def create_data_entry_button(self, frame):
        btn = CustomButton.CustomButton(frame, "           Enter Data           ")
        btn.btn.config(background='#0e1118', command=self.create_model)
        btn.place(x=270, y=550)

    def create_show_graph_button(self, frame):
        btn = CustomButton.CustomButton(frame, "           Show Graph           ")
        btn.btn.config(background='#0e1118', command=self.plt)
        btn.place(x=570, y=550)

    def plt(self):
        if self.model_built==True:
            self.model.plot()
        else:
            messagebox.showerror("error", "please build the model first!")

    def create_accuracy_label(self, accuracy):
        self.acc_label1 = tk.Label(self.frame, text="Accuracy : ", bg='#0e1118', fg='white', font=('Helvetica', 18, 'normal'))
        self.acc_label1.place(x=10,y=650)
        self.acc_label2 = tk.Label(self.frame, text=str(accuracy)+" %", bg='#0e1118', fg='white', font=('Helvetica', 18, 'normal'))
        self.acc_label2.place(x=160, y=650)


    def destroy(self):
        self.frame.destroy()
        self.panel.destroy()

    def create_model(self):
        features = ["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", "roundnes"]
        labels = ["Bombay", "Cali", "Sira"]
        self.model_data['features'] = []
        self.model_data['labels'] = []

        for j in features:
            if self.checkboxValue[j].get() == 1:
                self.model_data['features'].append(j)

        for j in labels:
            if self.checkboxValue[j].get() == 1:
                self.model_data['labels'].append(j)
        try:
            if len(self.model_data['features']) < 2 or len(self.model_data['labels']) < 2:
                raise Exception()
            # print(self.model_data['features'])
            # print(self.model_data['labels'])
            # print(float(self.epochs.get()))
            # print(float(self.learning_rate.get()))
            if self.algorithm_var.get() == 0:
                raise Exception()
            # print(self.algorithm_var.get())
            # print(self.bias_value.get())
            self.model = BuildModel.BuildModel()
            self.model.features = self.model_data['features']
            self.model.labels = [x.upper() for x in self.model_data['labels']]
            tmp = False
            if self.bias_value.get() == 1:
                tmp = True
            self.model.include_bias = tmp
            if self.algorithm_var.get() == 1:
                self.model.model = Perceptron.Perceptron(float(self.learning_rate.get()), int(self.epochs.get()), tmp)
            else:
                self.model.model = Adaline.Adaline(float(self.learning_rate.get()), int(self.epochs.get()), tmp)
            if len(self.threshold.get()) != 0:
                self.model.model.threshold = float(self.threshold.get())
            self.model.build()
            self.model_built = True
            if self.acc_label1 != None:
                self.acc_label1.destroy()
                self.acc_label2.destroy()
            self.create_accuracy_label(self.model.accuracy * 100)
        except:
            messagebox.showerror("value error", "please enter right data")


