import tkinter as tk
import random

# Dramatic sentences to show when he clicks "No"
dramatic_lines = [
    "💔 Oh no... my heart is breaking!",
    "😢 How could you say no to me?",
    "🌹 Without you, Valentine's loses its meaning...",
    "💕 Please... say YES, my love!"
]
line_index = 0

def draw_hearts(canvas, num_hearts=120):
    colors = ["red", "pink", "purple", "magenta", "hot pink", "violet"]
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    for _ in range(num_hearts):
        x = random.randint(20, width-40)
        y = random.randint(20, height-40)
        size = random.randint(15, 40)
        color = random.choice(colors)
        # Draw a simple heart using two circles and a triangle
        canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
        canvas.create_oval(x+size, y, x+2*size, y+size, fill=color, outline=color)
        points = [x, y+size//2, x+2*size, y+size//2, x+size, y+2*size]
        canvas.create_polygon(points, fill=color, outline=color)

def on_yes():
    result_label.config(text="💖 Yay! You said YES! 💖", fg="red", font=("Segoe Script", 32, "bold"))

def on_no():
    global line_index
    # Cycle through dramatic lines
    result_label.config(text=dramatic_lines[line_index], fg="purple", font=("Segoe Script", 26, "italic"))
    line_index = (line_index + 1) % len(dramatic_lines)

# Create main window in full screen
root = tk.Tk()
root.title("Happy Valentine's Day!")
root.attributes("-fullscreen", True)  # Full screen mode
root.configure(bg="light pink")

# Create canvas for hearts
canvas = tk.Canvas(root, bg="light pink", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Draw colorful hearts after window loads
root.update()
draw_hearts(canvas, num_hearts=120)

# Add beautiful background text
canvas.create_text(root.winfo_screenwidth()//2, 150,
                   text="💝 Happy Valentine's Day 💝\nForever Yours ❤️",
                   font=("Segoe Script", 48, "bold"),
                   fill="white", justify="center")

canvas.create_text(root.winfo_screenwidth()//2, 300,
                   text="Will you be my Valentine?",
                   font=("Segoe Script", 36, "bold"),
                   fill="dark red")

# Buttons for Yes/No
yes_button = tk.Button(root, text="Yes 💕", font=("Segoe Script", 24), bg="lightgreen", command=on_yes)
no_button = tk.Button(root, text="No 💔", font=("Segoe Script", 24), bg="lightcoral", command=on_no)

canvas.create_window(root.winfo_screenwidth()//2 - 100, 380, window=yes_button)
canvas.create_window(root.winfo_screenwidth()//2 + 100, 380, window=no_button)

# Label to show result
result_label = tk.Label(root, text="", font=("Segoe Script", 28, "bold"), bg="light pink")
canvas.create_window(root.winfo_screenwidth()//2, 480, window=result_label)

root.mainloop()
