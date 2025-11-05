import tkinter as tk
from tkinter import Text, messagebox
from cryptography.fernet import Fernet

# Function to generate a key for encryption and decryption


def generate_key():
    return Fernet.generate_key()

# Function to encrypt the text


def encrypt_text():
    try:
        text = text_input.get("1.0", tk.END).strip()  # Get the input text
        if text == "":
            messagebox.showerror(
                "Input Error", "Please enter some text to encrypt.")
            return
        key = key_input.get()
        if key == "":
            messagebox.showerror("Key Error", "Please provide a valid key.")
            return
        fernet = Fernet(key)
        encrypted_text = fernet.encrypt(text.encode()).decode()
        # Enable text widget to show the result
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)  # Clear previous output
        # Insert the encrypted text
        result_output.insert(tk.END, encrypted_text)
        # Disable text widget to avoid editing
        result_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to decrypt the text


def decrypt_text():
    try:
        text = text_input.get("1.0", tk.END).strip()  # Get the input text
        if text == "":
            messagebox.showerror(
                "Input Error", "Please enter some text to decrypt.")
            return
        key = key_input.get()
        if key == "":
            messagebox.showerror("Key Error", "Please provide a valid key.")
            return
        fernet = Fernet(key)
        decrypted_text = fernet.decrypt(text.encode()).decode()
        # Enable text widget to show the result
        result_output.config(state=tk.NORMAL)
        result_output.delete("1.0", tk.END)  # Clear previous output
        # Insert the decrypted text
        result_output.insert(tk.END, decrypted_text)
        # Disable text widget to avoid editing
        result_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

        import tkinter
        from tkinter import PhotoImage
        image_path = PhotoImage(
            file=r"C:\\Users\\pcsah\\OneDrive\\Desktop\\INCYRPT\\background.jpg")
        bg_image = tkinter.Label(window, image=image_path)
        bg_image.pack()


# Create the main window
window = tk.Tk()
window.title("SecureText - Text Encryption & Decryption Tool by Sahal Khan")
window.geometry("600x500")
window.configure(bg="#f0f4f5")  # Light background color

# Add a title label
title_label = tk.Label(window, text="SecureText - Text Encryption & Decryption Tool",
                       font=("Georgia", 25, "bold"), bg="#f0f4f5")

title_label.pack(pady=10)


# Add a key input label and entry
key_label = tk.Label(window, text="Enter Key (For Encryption/Decryption):",
                     font=("Georgia", 15), bg="#f0f4f5")
key_label.pack(pady=5)
key_input = tk.Entry(window, font=("Georgia", 12), width=40)
key_input.pack(pady=5)

# Add an instruction label for the text input
instruction_label = tk.Label(
    window, text="Enter Text to Encrypt or Decrypt:", font=("Georgia", 15), bg="#f0f4f5")
instruction_label.pack(pady=5)

# Add a text input area for the user
text_input = tk.Text(window, font=("Georgia", 12),
                     height=6, width=50, wrap=tk.WORD)
text_input.pack(pady=10)

# Buttons for encryption and decryption
encrypt_button = tk.Button(window, text="Encrypt Text", font=(
    "Georgia", 15, "bold"), command=encrypt_text, bg="#4CAF50", fg="white", width=20)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Decrypt Text", font=(
    "Georgia", 15, "bold"), command=decrypt_text, bg="#FF6347", fg="white", width=20)
decrypt_button.pack(pady=5)

# Add a result output area
result_label = tk.Label(window, text="Result (Encrypted or Decrypted Text):", font=(
    "Georgia", 15), bg="#f0f4f5")
result_label.pack(pady=10)

result_output = tk.Text(window, font=("Georgia", 15),
                        height=6, width=50, wrap=tk.WORD, state=tk.DISABLED)
result_output.pack(pady=5)

# Generate a sample key and show it to the user


def show_sample_key():
    key = generate_key()
    key_input.delete(0, tk.END)
    key_input.insert(tk.END, key.decode())  # Insert the key as text


# Add a "Generate Key" button
generate_key_button = tk.Button(window, text="Generate Sample Key", font=(
    "Georgia", 12, "bold"), command=show_sample_key, bg="#FFD700", fg="black", width=20)
generate_key_button.pack(pady=10)

# Run the main loop of the application
window.mainloop()
