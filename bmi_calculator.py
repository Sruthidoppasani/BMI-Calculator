import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight 😕"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight 😊"
        elif 25 <= bmi < 29.9:
            category = "Overweight 😐"
        else:
            category = "Obese 😟"

        # Show result
        label_result.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

# Title
tk.Label(root, text="BMI Calculator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Weight Entry
tk.Label(root, text="Enter Weight (kg):", bg="#f0f0f0").pack()
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Height Entry
tk.Label(root, text="Enter Height (cm):", bg="#f0f0f0").pack()
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="blue", fg="white").pack(pady=15)

# Result Label
label_result = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
label_result.pack(pady=10)

# Run the app
root.mainloop()