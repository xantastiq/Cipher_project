# 🔐 Vigenère Cipher Tool

A simple Python implementation of the Vigenère Cipher, one of the classic techniques of symmetric encryption. This script allows you to both encrypt and decrypt messages using a custom keyword.

---

## 📚 What is the Vigenère Cipher?

The **Vigenère cipher** is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. It was originally described in the 16th century and is known for being significantly more secure than the Caesar cipher when used properly.

### Example:
- **Plaintext**: `helloworld`
- **Key**: `key`
- **Encrypted**: `rijvsuyvjn`

---

## 🚀 Features

- 🔐 **Encryption**: Convert your message into a cipher using a keyword.
- 🔓 **Decryption**: Convert the cipher back to the original message using the same keyword.
- ✅ **Handles non-letter characters**: Spaces, punctuation, and numbers are preserved.
- 🔄 **Case-insensitive**: All input is converted to lowercase for simplicity.

---

## 📁 Project Structure

```
vigenere-cipher-tool/
├── vigenere_cipher.py  # Main script with encryption/decryption functions
└── README.md           # Project documentation
```

---

## 🧪 Example Usage

```python
text = 'mrttaqrhknsw ih puggrur'
key = 'happycoding'

decrypted = decrypt(text, key)
print(decrypted)
```

### 🔎 Output:
```
Encrypted text: mrttaqrhknsw ih puggrur
Key: happycoding
Decrypted text: welcomeback to cryptlab
```

---

## ▶️ Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/vigenere-cipher-tool.git
cd vigenere-cipher-tool
```

2. Run the script:

```bash
python vigenere_cipher.py
```

3. Modify the `text` and `key` variables in the script to try your own inputs.

---

## 🛠 Functions Overview

### `encrypt(message, key)`
Encrypts the provided message using the Vigenère cipher.

### `decrypt(message, key)`
Decrypts a Vigenère-encrypted message using the original key.

---

## ⚙️ How It Works

1. Each letter in the message is shifted forward in the alphabet by the position of the corresponding letter in the key.
2. If the character is not a letter (e.g., space, punctuation), it is preserved.
3. Decryption shifts letters **backwards** by the same amount.

---

## 🧠 Limitations

- Only works with lowercase alphabetic characters.
- The key must be composed of lowercase letters only.
- Designed for educational and demonstration purposes—not secure for real-world encryption needs.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 🙋‍♂️ Author

Developed by Taswar Eshraq.
Thanking Freecodecamp for the guidance and teaching me Python.

Feel free to reach out or connect on GitHub!
