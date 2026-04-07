import tkinter as tk
from transformers import pipeline

# Load AI model
classifier = pipeline("sentiment-analysis")

# ---------- WINDOW ----------
root = tk.Tk()
root.title("Mental Health Text Checker")
root.geometry("650x550")
root.config(bg="black")

# ---------- TITLE ----------
title = tk.Label(root, text="Mental Health Text Checker ❤️",
                 font=("Arial", 20, "bold"),
                 bg="black", fg="white")
title.pack(pady=10)

# ---------- INPUT ----------
input_box = tk.Text(root, height=6, width=70, bg="white", fg="black")
input_box.pack(pady=10)

# ---------- OUTPUT ----------
output = tk.Text(root, height=15, width=75, bg="lightyellow", fg="black")
output.pack(pady=10)

# ---------- FUNCTION ----------
def check_mental_health():
    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        output.insert(tk.END, "⚠ Please enter text\n\n")
        return

    result = classifier(text)[0]

    # Simple logic
    if result['label'] == "NEGATIVE":
        status = "⚠ Possible Stress / Negative Emotion"
        suggestion = "💡 Try to relax, talk to someone, or take a break."
        color = "red"
    else:
        status = "😊 Positive / Normal State"
        suggestion = "👍 Keep maintaining a healthy mindset!"
        color = "green"

    # Output
    output.insert(tk.END, "----- Analysis Result -----\n", "title")
    output.insert(tk.END, f"Sentiment: {result['label']} ({round(result['score'],2)})\n")
    output.insert(tk.END, f"{status}\n", color)
    output.insert(tk.END, f"{suggestion}\n\n")

# Clear
def clear():
    input_box.delete("1.0", tk.END)
    output.delete("1.0", tk.END)

# ---------- COLORS ----------
output.tag_config("title", foreground="blue", font=("Arial", 12, "bold"))
output.tag_config("red", foreground="red")
output.tag_config("green", foreground="green")

# ---------- BUTTONS ----------
tk.Button(root, text="Check Mental State", command=check_mental_health,
          bg="green", fg="white", width=25).pack(pady=5)

tk.Button(root, text="Clear", command=clear,
          bg="red", fg="white", width=25).pack(pady=5)

# ---------- RUN ----------
root.mainloop()


# I feel very sad and lonely I am happy and enjoying my day