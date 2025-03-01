import tkinter as tk
from tkinter import scrolledtext
from lexer import Lexer
from parse import Parser
import sys
import io

def run_code():
    code = editor.get("1.0", tk.END).strip()
    if not code:
        return
    
    # Redirect stdout to capture output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        tokenizer = Lexer(code)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        tree = parser.parse()
        
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, tree)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")
    finally:
        sys.stdout = old_stdout

# Create main window
root = tk.Tk()
root.title("Jo# IDE - Community Version 1")
root.geometry("600x500")

# Text editor
editor = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
editor.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Run button
run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack(pady=5)

# Output area
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, bg="#f4f4f4")
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Start GUI loop
root.mainloop()
