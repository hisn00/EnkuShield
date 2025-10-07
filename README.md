# 🛡️ EnkuShield

███████╗███╗   ██╗██╗  ██╗██╗   ██╗███████╗██╗  ██╗██╗██╗     ███████╗██████╗ ██╔════╝████╗  ██║██║ ██╔╝╚██╗ ██╔╝██╔════╝██║  ██║██║██║     ██╔════╝██╔══██╗ █████╗  ██╔██╗ ██║█████╔╝  ╚████╔╝ ███████╗███████║██║██║     █████╗  ██████╔╝ ██╔══╝  ██║╚██╗██║██╔═██╗   ╚██╔╝  ╚════██║██╔══██║██║██║     ██╔══╝  ██╔══██╗ ███████╗██║ ╚████║██║  ██╗   ██║   ███████║██║  ██║██║███████╗███████╗██║  ██║ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝

> Decode. Encode. Protect.  
> *A smart customizable encryption toolkit for developers, students and CTF enthusiasts.*

EnkuShield is an interactive cryptography tool designed for encoding and decoding text or files using multiple algorithms from common Base64 and Caesar Cipher to custom mathematical encryption formulas.

Built with 💻 Python it combines simplicity, power and flexibility.  
Perfect for:  
- 🧠 Learning cryptography  
- 🔐 CTF (Capture The Flag) competitions  
- 📁 File protection and text encryption  
- ⚙️ Creating your own encryption logic

---

## ✨ Features

- ✅ 15+ encryption/decryption methods — including Base64, Hex, ROT13, Binary, URL, Base32, ASCII, Caesar Cipher, Atbash Cipher, XOR Cipher, Unicode Shift Cipher, Multiplicative Cipher, Substitution Cipher, Reverse+XOR, Base64 (URL Safe)  
- ✅ Custom Formula Mode — add your own math based encryption rule (e.g., (ord(c) + key * 2) % 256)  
- ✅ File encryption support    
- ✅ Fast and simple Flask backend  
- ✅ CTF ready — instantly encode/decode with all the common algorithms used in competitions  

---

## 🧩 How It Works

1. Choose an encryption method (Base64, XOR, etc.)  
2. Enter your text or file  
3. Hit Encrypt / Decrypt  
4. For Custom Formula, enter a mathematical rule:

(ord(c) + key * 3) % 256

> You can define how each character is transformed mathematically.  

---

## 🛠️ Installation

Clone the repository and install Flask:

`bash
git clone https://github.com/yourusername/EnkuShield.git
cd EnkuShield
pip install flask

Run the app:

python app.py

Then open your browser and go to:

http://127.0.0.1:5000

---

🧠 Example Use

Encrypting a secret message:

Text:  "HELLO"
Method: Base64
Output: "SEVMTE8="

Or use your own formula:

Formula: (ord(c) + 7) % 256

---

💡 Inspiration

> The name EnkuShield comes from “Enku” meaning pearl or treasure symbolizing valuable protection.
Just like a shield it guards your data with layers of encryption and creativity.

---

🎮 Use in Capture The Flag (CTF)

EnkuShield is a powerful all in one CTF helper whether you’re reversing Base64, decoding ROT13 or testing XOR encryptio it’s got you covered.
You can quickly test multiple ciphers when analyzing encoded strings or create your own encryption puzzles using custom formulas.


---

🧾 License

This project is licensed under the MIT License.

---

🤝 Contribute

Want to add your own cipher or formula idea?
Fork the repo and submit a pull request!
Let’s make EnkuShield smarter together 🧠💪

---

💬 Author

👩‍💻 Hisnul Mohammed
✨ Passionate about cybersecurity, AI, and creative encryption systems.
📫 Reach out: LinkedIn | GitHub


---

⭐ If you like this project, give it a star on GitHub and share it with your fellow CTF players!

---
