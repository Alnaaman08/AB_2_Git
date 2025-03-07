import tkinter as tk
from tkinter import ttk

class CurrencyC:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x350") 
        
        self.rates = {
            "USD": 1, "Euro": 0.96, "Yen": 150.55, "GBP": 0.79
        }

        self.texts = {
            "en": {
                "enter_amount": "Enter amount:",
                "from_label": "From:",
                "to_label": "To:",
                "convert_button": "Convert",
                "converted_label": "Converted: ",
                "invalid_input": "Invalid input"
            },
            "de": {
                "enter_amount": "Betrag eingeben:",
                "from_label": "Von:",
                "to_label": "Nach:",
                "convert_button": "Konvertieren",
                "converted_label": "Umgewandelt: ",
                "invalid_input": "Ungültige Eingabe"
            }
        }

        self.language = "en"
    
        self.label = tk.Label(root, text=self.texts[self.language]["enter_amount"])
        self.label.pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.from_label = tk.Label(root, text=self.texts[self.language]["from_label"])
        self.from_label.pack(pady=5)

        self.from_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.from_currency.pack(pady=5)
        self.from_currency.set("USD")

        self.to_label = tk.Label(root, text=self.texts[self.language]["to_label"])
        self.to_label.pack(pady=5)

        self.to_currency = ttk.Combobox(root, values=list(self.rates.keys()))
        self.to_currency.pack(pady=5)
        self.to_currency.set("Euro")

        self.button = tk.Button(root, text=self.texts[self.language]["convert_button"], command=self.on_click)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

        self.language_button = tk.Button(root, text="Change Language", command=self.change_language)
        self.language_button.pack(pady=10)

    def on_click(self):
        try:
            amount = float(self.entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            result = self.convert_currency(amount, from_curr, to_curr)
            self.result_label.config(text=f"{self.texts[self.language]['converted_label']} {result:.2f} {to_curr}")
        except ValueError:
            self.result_label.config(text=self.texts[self.language]["invalid_input"])

    def convert_currency(self, amount, currency_from, currency_to):
        if currency_from in self.rates and currency_to in self.rates:
            amount_in_usd = amount / self.rates[currency_from]  
            return amount_in_usd * self.rates[currency_to]  
        return amount

    def change_language(self):
        self.language = "de" if self.language == "en" else "en"

        self.label.config(text=self.texts[self.language]["enter_amount"])
        self.from_label.config(text=self.texts[self.language]["from_label"])
        self.to_label.config(text=self.texts[self.language]["to_label"])
        self.button.config(text=self.texts[self.language]["convert_button"])
        self.result_label.config(text="")
        self.language_button.config(text="Change Language")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyC(root)
    root.mainloop()
