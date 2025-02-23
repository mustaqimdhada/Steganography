import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import binascii


# Function to hide the text in the image (Encryption)
def encrypt_image(image_path, text, passcode):
    try:
        # Open image
        image = Image.open(image_path)
        pixels = image.load()

        # Convert the text to binary
        binary_text = ''.join(format(ord(i), '08b') for i in text)
        # Add a termination sequence (8 zeros, '00000000') to signal the end of the hidden text
        binary_text += '00000000'  

        length = len(binary_text)
        
        # Passcode to modify position
        start_position = sum(ord(ch) for ch in passcode) % image.size[0]

        # Insert binary text into the image's LSBs
        idx = 0
        for i in range(start_position, image.size[0]):
            for j in range(image.size[1]):
                if idx < length:
                    pixel = list(pixels[i, j])

                    # Replace the LSB of each color component with the message bits
                    for k in range(3):  # R, G, B channels
                        if idx < length:
                            pixel[k] = pixel[k] & 0xFE | int(binary_text[idx])  # Clear LSB and set the message bit
                            idx += 1
                    
                    pixels[i, j] = tuple(pixel)

        # Save the image with the hidden text
        image.save("encrypted_image.png")
        messagebox.showinfo("Success", "Text hidden in image successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to extract the hidden text from the image (Decryption)
def decrypt_image(image_path, passcode):
    try:
        # Open the image
        image = Image.open(image_path)
        pixels = image.load()

        # Passcode to modify position
        start_position = sum(ord(ch) for ch in passcode) % image.size[0]

        # Extract binary data from LSBs
        binary_text = ''
        for i in range(start_position, image.size[0]):
            for j in range(image.size[1]):
                pixel = list(pixels[i, j])
                for k in range(3):  # R, G, B channels
                    binary_text += str(pixel[k] & 1)  # Extract the LSB

        # Convert binary to text, stopping at the termination sequence '00000000'
        termination_sequence = '00000000'
        binary_text = binary_text.split(termination_sequence)[0]  # Remove anything after the termination sequence

        # Convert binary to text
        text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))

        return text

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI for user interaction
class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography - Hide and Reveal Text")

        self.text_label = tk.Label(root, text="Enter the text to hide:")
        self.text_label.grid(row=0, column=0)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=1)

        self.passcode_label = tk.Label(root, text="Enter a passcode:")
        self.passcode_label.grid(row=1, column=0)

        self.passcode_entry = tk.Entry(root, width=50)
        self.passcode_entry.grid(row=1, column=1)

        self.select_image_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_image_button.grid(row=2, column=0, columnspan=2)

        self.encrypt_button = tk.Button(root, text="Encrypt Text into Image", command=self.encrypt)
        self.encrypt_button.grid(row=3, column=0, columnspan=2)

        self.decrypt_button = tk.Button(root, text="Decrypt Text from Image", command=self.decrypt)
        self.decrypt_button.grid(row=4, column=0, columnspan=2)

        self.selected_image = None

    def select_image(self):
        # Open file dialog to select image
        self.selected_image = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    def encrypt(self):
        # Encrypt text into image
        text = self.text_entry.get()
        passcode = self.passcode_entry.get()

        if not text or not passcode or not self.selected_image:
            messagebox.showerror("Error", "Please fill in all fields and select an image.")
            return

        encrypt_image(self.selected_image, text, passcode)

    def decrypt(self):
        # Decrypt text from image
        passcode = self.passcode_entry.get()

        if not passcode or not self.selected_image:
            messagebox.showerror("Error", "Please enter a passcode and select an image.")
            return

        text = decrypt_image(self.selected_image, passcode)
        messagebox.showinfo("Decrypted Text", text)


if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
