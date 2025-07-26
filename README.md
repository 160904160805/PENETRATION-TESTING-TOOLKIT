# ⚔️✨ Penetration Testing Toolkit

A sleek, modular **Flask-based toolkit** for hands-on penetration testing — designed for **ethical hackers**, **cybersecurity learners**, and **network defenders**.

Perform **Port Scanning** and **Brute-force Attacks** through a clean, interactive dashboard — all from your browser!

---

## 🌟 Key Features

- 🎯 **One-page Tabbed UI** — Easy toggling between tools  
- 🔍 **Port Scanner**  
  - Scan custom IPs and port ranges  
  - Detect common protocols (HTTP, FTP, SSH)  
  - Real-time result display  
- 💥 **Brute-force Login Module**  
  - Target custom login forms  
  - Upload `.txt` wordlists  
  - Smart response matching  
- 🔁 Live spinners during scan/attack  
- 🛡️ Input validation (IPs, URLs, ports)  
- 🔧 Fully customizable for your needs  

---

## 🗂️ Project Structure

```bash
pen-test-toolkit/
├── app/
│   ├── routes.py             # Flask route logic
│   ├── modules/
│   │   ├── port_scanner.py   # Port scan logic
│   │   └── brute_forcer.py   # Brute-force logic
│   ├── static/
│   │   └── style.css         # Styling
│   ├── templates/
│   │   └── index.html        # UI layout
│   └── uploads/              # Wordlist uploads
├── run.py                    # Flask app launcher
├── requirements.txt          # Dependencies
└── README.md                 # This file!
```

---

## 🛠️ Technologies Used

- 🐍 **Python 3.x**
- 🔥 **Flask** (Backend Web Framework)
- 🔌 **Socket** (for port scanning)
- 📡 **Requests** (for login brute-force)
- 🧽 **BeautifulSoup** (optional HTML parsing)
- 🎨 **HTML5 + CSS3 + JavaScript** (Frontend)

---

## ⚙️ How to Run the Toolkit Locally

### 📥 1. Clone the Repository

```bash
git clone https://github.com/your-username/pen-test-toolkit.git
cd pen-test-toolkit
```

### 🧪 2. (Optional) Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # Mac/Linux
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🚀 4. Start the Flask Server

```bash
python run.py
```

Then open your browser at: **http://localhost:5000**

---

## 💻 How to Use the Toolkit

### 🕵️‍♂️ Port Scanner

- Enter a valid IP address (e.g. `127.0.0.1`)
- Set a port range (e.g. `20-100`)
- Click **Scan**
- See real-time results with open ports and detected protocols

### 🔓 Brute-force Login

- Enter the login page URL (e.g. `http://localhost/login.php`)
- Input a known username (e.g. `admin`)
- Upload a `.txt` wordlist
- Click **Attack** to brute-force
- Results display the cracked password (if found)

---

## 🧾 Wordlist Sample Format

```text
admin
123456
password
letmein
secret123
qwerty
qwerty123
```

---

## 🧪 Dummy Login Page for Testing

Create a file like `login.php` (for local XAMPP/Apache testing):

```php
<?php
$correct_user = "admin";
$correct_pass = "secret123";

if ($_POST["username"] === $correct_user && $_POST["password"] === $correct_pass) {
    echo "Login success";
} else {
    echo "Invalid credentials";
}
?>
```

---

## 📋 requirements.txt

```text
Flask
requests
```

---

## ⚠️ Disclaimer

> 🚨 This tool is for **educational purposes only**.  
> Do **not** scan or attack systems without **explicit permission**.  
> Unauthorized access is **illegal** and **unethical**.

---


## 💡 Future Upgrades

- 🔍 Directory brute-forcing  
- 🧬 SQL Injection & XSS vulnerability detection  
- 🔑 Authenticated brute-force module  
- 🛡️ SSL/HTTPS protocol checks  
- 🗂️ Export scan results to `.txt` or `.csv`  

