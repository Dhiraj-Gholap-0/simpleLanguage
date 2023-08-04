import tkinter as tk
from tkinter import filedialog  # Add this import statement
import subprocess

def open_file():

    file_path = filedialog.askopenfilename(filetypes=[("Simple Files", "*.simple")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, content)

def run_python_file():
    try:
        output_text.configure(state=tk.NORMAL)  # Set state to normal to enable editing
        output_text.delete(1.0, tk.END)  # Clear the content from the first character to the end
        result = subprocess.run(["python", "C:/Users/kruti/Desktop/GUI/SimpleFileVersion.py"], capture_output=True, text=True)
        output_text.insert(tk.END, result.stdout)
        output_text.insert(tk.END, result.stderr)
        output_text.configure(state=tk.DISABLED)
    except FileNotFoundError:
        output_text.insert(tk.END, "Error: File not found.")

def auto_save():
    file_path = "Demo.simple"
    current_content = text_widget.get(1.0, tk.END)

    with open(file_path, "r") as file:
        previous_content = file.read()

    if current_content != previous_content:
        with open(file_path, "w") as file:
            file.write(current_content)

    text_widget.after(1000, auto_save)  # Call this function again after 1000ms (1 second)

# Create the main application window
app = tk.Tk()
app.title("Python File Runner")

# Create the "Open File" button
open_button = tk.Button(app, text="Open File", command=open_file)
open_button.pack(pady=5)

# Create a text widget to display the code
text_widget = tk.Text(app, height=15, width=50)
text_widget.pack()

# Create the "Run" button
run_button = tk.Button(app, text="Run", command=run_python_file)
run_button.pack(pady=10)

# Create a text widget to display the output
output_text = tk.Text(app, height=10, width=50)
output_text.pack()

# Start the auto_save function to automatically save the content every second
text_widget.after(1000, auto_save)

# Run the main event loop
app.mainloop()





