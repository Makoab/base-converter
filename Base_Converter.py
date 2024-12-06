import tkinter as tk
from tkinter import messagebox

def convert(number, from_base, to_base):
    try:
        number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Create letter dict
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # Letter to number
        letter_dict = {}
        start = 10
        for i in range(len(english_alphabet)):
            letter_dict[english_alphabet[i]] = start
            start += 1

        # Number to letter dict
        number_dict = {}
        for i in range(len(english_alphabet)):
            number_dict[i + 10] = english_alphabet[i]

        # From any base to decimal
        b = len(number)
        final_number = 0

        for i in range(b):
            if number[-1 * (i + 1)].isdigit():
                final_number += int(number[-1 * (i + 1)]) * pow(from_base, i)
            else:
                final_number += letter_dict[number[-1 * (i + 1)]] * pow(from_base, i)

        # From decimal to any base
        divider = final_number
        final2 = ""
        while abs(divider - to_base) >= 0 and divider > 0:
            qaliq = divider % to_base
            if qaliq >= 10:
                final2 += number_dict[qaliq]
            else:
                final2 += str(qaliq)
            divider //= to_base

        return final2[::-1]
    except Exception as e:
        return f"Error: {str(e)}"

# Tkinter App
def run_app():
    def on_convert():
        number = number_entry.get().strip().lower()
        try:
            from_base = int(from_base_entry.get())
            to_base = int(to_base_entry.get())
            if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
                raise ValueError("Bases must be between 2 and 36.")
            result = convert(number, from_base, to_base)
            messagebox.showinfo("Result", f"Converted Number: {result}")
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    # Create the main window
    root = tk.Tk()
    root.title("Base Converter")

    # Input fields
    tk.Label(root, text="Number:").grid(row=0, column=0, padx=5, pady=5)
    number_entry = tk.Entry(root, width=20)
    number_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="From Base:").grid(row=1, column=0, padx=5, pady=5)
    from_base_entry = tk.Entry(root, width=20)
    from_base_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="To Base:").grid(row=2, column=0, padx=5, pady=5)
    to_base_entry = tk.Entry(root, width=20)
    to_base_entry.grid(row=2, column=1, padx=5, pady=5)

    # Convert button
    convert_button = tk.Button(root, text="Convert", command=on_convert)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Run the application
    root.mainloop()

run_app()
