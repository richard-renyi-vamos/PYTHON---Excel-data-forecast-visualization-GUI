import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            return df
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
    else:
        messagebox.showwarning("Warning", "No file selected")

def forecast(df):
    # Perform forecast using ARIMA model (you may need to adjust parameters)
    model = ARIMA(df, order=(5,1,0))
    fitted_model = model.fit()
    forecast = fitted_model.forecast(steps=10)  # Adjust steps as needed
    return forecast

def visualize(df, forecast):
    plt.plot(df.index, df.values, label='Actual Data')
    plt.plot(df.index[-1:], forecast, marker='o', color='red', label='Forecast')
    plt.title('Forecast')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def main():
    root = tk.Tk()
    root.title("Excel Forecast Tool")

    def on_load_data():
        df = load_data()
        if df is not None:
            messagebox.showinfo("Success", "Data loaded successfully!")
            forecast_button.config(state=tk.NORMAL)
            visualize_button.config(state=tk.DISABLED)

    def on_forecast():
        forecast_data = forecast(df)
        visualize(df, forecast_data)
        visualize_button.config(state=tk.NORMAL)

    load_button = tk.Button(root, text="Load Data", command=on_load_data)
    load_button.pack(pady=10)

    forecast_button = tk.Button(root, text="Perform Forecast", command=on_forecast, state=tk.DISABLED)
    forecast_button.pack(pady=5)

    visualize_button = tk.Button(root, text="Visualize Forecast", command=lambda: visualize(df, forecast_data), state=tk.DISABLED)
    visualize_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
