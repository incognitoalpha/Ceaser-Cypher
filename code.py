import tkinter as tk

# Function to process input and shift value
def process_input():
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        shift = shift_slider.get()
        output_text = ''.join([chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() 
                              else chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() 
                              else char for char in input_text])
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output_text)

# Main window
root = tk.Tk()
root.title("Custom Tkinter GUI")

# Input box
tk.Label(root, text="Input Message:").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

# Shift value slider
tk.Label(root, text="Shift Value:").pack()
shift_slider = tk.Scale(root, from_=0, to=25, orient=tk.HORIZONTAL)
shift_slider.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=process_input)
submit_button.pack()

# Output box
tk.Label(root, text="Output Message:").pack()
output_box = tk.Text(root, height=5, width=50)
output_box.pack()

# Run the application
root.mainloop()
