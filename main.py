import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

# Function to generate QR code
def generate_qr():
    name = name_entry.get()
    member_id = id_entry.get()
    phone = phone_entry.get()

    if not name or not member_id or not phone:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Combine data into a single string
    data = f"Name: {name}\nID: {member_id}\nPhone: {phone}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code as an image file
    qr_img.save("member_qr.png")

    # Display QR code in GUI
    qr_img_tk = ImageTk.PhotoImage(qr_img)
    qr_label.config(image=qr_img_tk)
    qr_label.image = qr_img_tk

    messagebox.showinfo("Success", "QR Code generated and saved as 'member_qr.png'.")

# Set up the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

# Labels and Entry fields for member details
name_label = tk.Label(root, text="Member Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

id_label = tk.Label(root, text="Member ID:")
id_label.pack(pady=5)
id_entry = tk.Entry(root, width=30)
id_entry.pack(pady=5)

phone_label = tk.Label(root, text="Telephone Number:")
phone_label.pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Label to display the QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
