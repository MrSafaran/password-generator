# 🔐 Streamlit Password Generator

A lightweight and interactive dashboard built with [Streamlit](https://streamlit.io/) for generating secure and customizable passwords.  
This project provides three types of password generation:  
- **Pin Code** (numeric code)  
- **Random Password** (randomized string with numbers and punctuations)  
- **Memorable Password** (human-readable passphrases made of words)  


## ✨ Features

- **Numeric PIN Codes**  
  Generate secure PIN codes with a customizable length (4–32 digits).  

- **Random Passwords**  
  Create randomized strings with flexible length (8–100 characters) and options to include:  
  - ✅ Uppercase & lowercase letters  
  - ✅ Numbers  
  - ✅ Punctuation symbols  

- **Memorable Passphrases**  
  Generate human-readable passphrases built from real English words (sourced from `nltk.corpus.words`).  
  Options include:  
  - Custom separators (e.g., `---` or `====`)  
  - Optional capitalization of words  
  - Flexible length (8–64 words)  

- **Interactive Streamlit Dashboard**  
  Clean and user-friendly UI with sliders, toggles, and text inputs for quick customization.  


## 📦 Requirements

- Python **3.8+** (recommended)
- [Streamlit](https://streamlit.io/)  
- [NLTK](https://www.nltk.org/)  

To install the required packages, run:

```bash
pip install -r requirements.txt
```


## ⚙️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/streamlit-password-generator.git
cd streamlit-password-generator
```
2. **Create a virtual enviroment(Optional)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
3. **Install the required packages**
```bash
pip install -r requirements.txt
```
4. **Run the Sreamlit app**
```bash
streamlit run app.py
```


## 🗂️ Project Structure
```bash
streamlit-password-generator/
│
├── README.md # Project overview and instructions
├── LICENSE 
├── requirements.txt # Project dependencies
└── src/ 
    ├── app.py # Main Streamlit application
    ├── password_generator.py # Password generation logic
    └── image/ 
        └── download.png # Example image displayed in the dashboard
```

## 🛠️ Built With

- **Streamlit** – Framework for building the interactive dashboard  
- **NLTK** – Natural Language Toolkit for generating memorable passwords  
- **Python** – Programming language used for logic and app execution  


## 🤝 Contributing

Contributions are welcome! If you want to improve this project, you can:

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make your changes  
4. Commit your changes (`git commit -m 'Add some feature'`)  
5. Push to the branch (`git push origin feature-name`)  
6. Open a Pull Request  

Please make sure your code follows the existing style and is well-tested.


## ⚖️ License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

## 👤 Authors 

- **Mohammadreza Safaran** – [GitHub](https://github.com/MrSafaran)
