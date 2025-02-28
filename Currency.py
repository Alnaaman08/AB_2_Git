import tkinter as tk
from tkinter import ttk

class CurrencyC:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x250")

        self.rates = {
            "USD": 1, "Euro": 0.96, "Yen": 150.55, "GBP": 0.79
        }

        self.label = tk.Label(root, text="Enter amount:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.from_label = tk.Label(root, text="From:")
        self.from_label.pack(pady=5)

        self.from_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.from_currency.pack(pady=5)
        self.from_currency.set("USD")

        self.to_label = tk.Label(root, text="To:")
        self.to_label.pack(pady=5)

        self.to_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.to_currency.pack(pady=5)
        self.to_currency.set("Euro")

        self.button = tk.Button(root, text="Convert", command=self.on_click)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def on_click(self):
        try:
            amount = float(self.entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            result = self.convert_currency(amount, from_curr, to_curr)
            self.result_label.config(text=f"Converted: {result:.2f} {to_curr}")
        except ValueError:
            self.result_label.config(text="Invalid input")

    def convert_currency(self, amount, currency_from, currency_to):
        if currency_from in self.rates and currency_to in self.rates:
            amount_in_usd = amount / self.rates[currency_from]  
            return amount_in_usd * self.rates[currency_to]  
        return amount

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyC(root)
    root.mainloop()