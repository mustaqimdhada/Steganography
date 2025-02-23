# 🕵️‍♂️ Steganography

## 📌 Overview
This project implements Steganography, a technique for hiding secret messages within images. The goal is to conceal data in a way that is undetectable to the human eye while ensuring secure transmission.

## ✨ Features
- 🖼️ Hide and extract secret messages within images
- 📷 Support for various image formats (PNG, JPG, BMP, etc.)
- 💻 User-friendly command-line interface (CLI)
- 🔒 Ensures minimal distortion to the original image

## ⚙️ Installation
### 📋 Prerequisites
- 🐍 Python 3.x
- 📦 Required Python libraries

### 🚀 Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/mustaqimdhada/Steganography.git
   ```
2. Navigate to the project folder:
   ```sh
   cd Steganography
   ```
3. Install dependencies manually:
   ```sh
   pip install pillow numpy opencv-python
   ```

## 🛠️ Usage
### 🔍 Hiding and Extracting a Message
## 📝 Example

### 🔒 Encrypting a Message
1. Run the script:
   ```sh
   python stego.py
   ```
2. A GUI window will appear where you can:
   - ✍️ Enter the secret message to hide
   - 🔑 Provide a passcode for encryption
   - 📂 Click "Select Image" to choose an image file
   - 🔒 Click "Encrypt Text into Image" to hide the message
   - 🔓 Click "Decrypt Text from Image" to extract the hidden message
3. After encryption, a confirmation message will appear: "Text hidden in image successfully!"

### 🔓 Decrypting a Message
1. Run the script:
   ```sh
   python stego.py
   ```
2. In the GUI window:
   - 🔑 Enter the passcode used during encryption
   - 📂 Click "Select Image" and browse the encrypted image
   - 🔓 Click "Decrypt Text from Image" to reveal the hidden message
3. A confirmation window will display the decrypted text.

## 🎥 Demo Video
A demonstration video showcasing the encoding and decoding process is shown below.


https://github.com/user-attachments/assets/1ea727ee-cb9b-404e-b850-51453e045fb9

