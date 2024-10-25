import tkinter as tk
from tkinter import messagebox
from gui import CustomButton, MainForm, FileForm
import pandas as pd


class PredictRow:
    def __init__(self, root, logo_img, upload):
        self.prediction_label = None
        self.frame = tk.Frame(root, width=1050, height=450, highlightbackground="#272731", highlightthickness=2,
                              bg="#0e1118")
        self.panel = tk.Frame(root, width=350, height=900, bg="#262730")
        self.root = root
        self.logo_img = logo_img
        self.upload = upload
        self.header = tk.Label(root, text="Enter Feature Values", bg="#0e1118", fg="white",
                               font=('Helvetica', 24, 'normal'))
        self.features = {}
        self.model = None
        self.create_gui()

    def create_gui(self):
        self.create_side_panel()
        self.create_frame()

    def create_side_panel(self):

        self.panel.place(x=0, y=0)

        tk.Label(self.panel, image=self.logo_img, border=0).place(x=23, y=100)
        tk.Label(self.panel, text="Dry Bean Classifier", bg="#262730", fg="#fff", font=("bold", 18), border=0).place(
            x=70,
            y=430)
        self.create_buttons(self.panel)

    def create_buttons(self, panel):
        row_prediction_button = CustomButton.CustomButton(panel, "Get File Prediction")
        row_prediction_button.btn.config(command=self.ToFilePrediction)
        row_prediction_button.place(x=80, y=550)

        build_model_button = CustomButton.CustomButton(panel, "      Build Model      ")
        build_model_button.btn.config(command=self.ToBuildModel)
        build_model_button.place(x=80, y=650)

    def ToFilePrediction(self):
        self.destroy()
        obj = FileForm.FileForm(self.root, self.upload, self.logo_img)
        obj.model = self.model

    def ToBuildModel(self):
        self.destroy()
        obj = MainForm.DryBeanClassifierApp(self.root, self.logo_img, self.upload)
        obj.model_built = True
        obj.model = self.model

    def create_frame(self):

        self.frame.place(x=420, y=200)

        self.header.place(x=800, y=180)
        self.create_input_fields(self.frame)
        self.create_prediction_button(self.frame)

    def create_input_fields(self, frame):
        self.features["Area"] = self.create_entry_field(frame, "Area", 50, 40)
        self.features["Perimeter"] = self.create_entry_field(frame, "Perimeter", 400, 40)
        self.features["MajorAxisLength"] = self.create_entry_field(frame, "Major Axis Length", 750, 40)
        self.features["MinorAxisLength"] = self.create_entry_field(frame, "Minor Axis Length", 50, 120)
        self.features["roundnes"] = self.create_entry_field(frame, "Roundnes", 400, 120)

    def create_entry_field(self, frame, label_text, x, y):
        label = tk.Label(frame, text=label_text, bg="#0e1118", fg="white", font=14)
        label.place(x=x, y=y)

        entry = tk.Entry(frame, bg='#272731', fg='white', insertbackground='white', borderwidth=5,
                         font=('Helvetica', 14, 'normal'), relief=tk.FLAT)
        entry.place(x=x, y=y + 30)
        return entry

    def create_prediction_widgets(self, frame):
        self.create_prediction_button(frame)
        self.create_prediction_label(frame)
        self.create_confidence_label(frame)

    def create_prediction_button(self, frame):
        predict_button = CustomButton.CustomButton(frame, "    Predict    ")
        predict_button.btn.config(background='#0e1118', command=self.predict)
        predict_button.place(x=450, y=250)

    def create_prediction_label(self, frame, predicted_feature):
        label2 = tk.Label(frame, text="The predicted class is : ", bg="#0e1118", fg="white", font=14)
        label2.place(x=50, y=335)

        self.prediction_label = tk.Label(frame, text=predicted_feature, bg="#0e1118", fg="white", font=14)
        self.prediction_label.place(x=260, y=335)

    def create_confidence_label(self, frame):
        label3 = tk.Label(frame, text="with confidence of : ", bg="#0e1118", fg="white", font=14)
        label3.place(x=50, y=380)

        confidence_percentage = "99.67117206258837"
        confidence_label = tk.Label(frame, text=confidence_percentage, bg="#0e1118", fg="white", font=14)
        confidence_label.place(x=260, y=380)

    def destroy(self):
        self.panel.destroy()
        self.frame.destroy()
        self.header.destroy()

    def predict(self):
        try:
            for key, value in self.features.items():
                if len(value.get()) == 0:
                    raise Exception()
            tmp = {}
            for key, value in self.features.items():
                tmp[key] = value.get()
            df = pd.DataFrame(tmp, columns=self.features.keys(), index=range(len(self.features)))
            df = self.model.preprocess_x(df)
            pred = self.model.model.predict(df)
            if pred[0] == -1:
                for i in range(len(pred)):
                    pred[i] = 0
            if self.prediction_label is not None:
                self.prediction_label.destroy()
            self.create_prediction_label(self.frame, self.model.label_encoder.inverse_transform(pred)[0])
        except:
            messagebox.showerror("value error", "please enter right data")
