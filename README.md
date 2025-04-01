# 🎉 AutoMailCertificates  

A Python automation script to generate and send certificates via email to participants of an event. Whether it's a small workshop or a large-scale competition, **AutoMailCertificates** makes certificate distribution effortless!  

[![GitHub stars](https://img.shields.io/github/stars/mantejjosan/automailcertificates?style=social)](https://github.com/mantejjosan/automailcertificates/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/mantejjosan/automailcertificates?style=social)](https://github.com/mantejjosan/automailcertificates/network/members)  
[![GitHub issues](https://img.shields.io/github/issues/mantejjosan/automailcertificates)](https://github.com/mantejjosan/automailcertificates/issues)  
[![GitHub last commit](https://img.shields.io/github/last-commit/mantejjosan/automailcertificates)](https://github.com/mantejjosan/automailcertificates/commits/main)  
![Views](https://komarev.com/ghpvc/?username=mantejjosan&color=brightgreen)  

---

## 🚀 Getting Started  

### 🔹 Installation  

#### 1️⃣ Clone the repository  

- **Using SSH:**  
  ```bash
  git clone git@github.com:mantejjosan/automailcertificates.git
  ```
- **Using HTTPS:**  
  ```bash
  git clone https://github.com/mantejjosan/automailcertificates.git
  ```

Then, navigate into the cloned repository:  
```bash
cd automailcertificates
```

#### 2️⃣ Set Up Required Files  

- Create the necessary environment and configuration files:  
  ```bash
  cp required_files/.env.example .env
  cp required_files/participants_data.example.csv participants_data.csv
  cp required_files/certificate_template.example.jpeg certificate_template.jpeg
  ```

- Open `.env`, `participants_data.csv`, and `certificate_template.jpeg` and modify them as needed.  

#### 3️⃣ Install Dependencies  

Ensure you have Python installed (recommended: Python 3.10+). Then, install required packages:  
```bash
pip install -r requirements.txt
```

---

## ⚡ Working  

### 1️⃣ Generate Certificates  

Run the following command to generate certificates for all participants:  
```bash
python index.py
```
Certificates will be saved in the `generated_certificates/` folder.  

### 2️⃣ Send Certificates via Email  

> NOTE: Before sending the emails check the csv file path and the generated certificates path
> in mail_participants.py file.
> 
> CSV_FILE = "participants_data.csv"  
> PDF_FOLDER = "generated_certificates"
>
> Change the line 15, 16 in mail_participants.py file to the above two lines of code and then run the below command.

Once the certificates are generated, send them via email using:  
```bash
python mail_participants.py
```

And that's it! ✅ Your participants will receive their certificates automatically.  

---

## 📌 Features  

✅ Generates high-quality PDF certificates  
✅ Uses a CSV file to dynamically insert participant details  
✅ Sends certificates via email with **just one command**  
✅ Fully customizable certificate template  
✅ Supports large-scale distributions  

---

## 🛠️ Environment Variables  

AutoMailCertificates requires an `.env` file to securely store email credentials.  
Example `.env` file:  

```env
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_app_password

```

> ⚠️ **Important:** If using Gmail, enable "Less Secure Apps" or generate an **App Password** for better security.  

---

## 🌟 Contributing  

Have an idea for improvement? Found a bug? Contributions are welcome!  

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added a new feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a pull request 🚀  

---

## 📄 License  

This project is open-source and available under the **MIT License**.  

---

## 📧 Contact  

For queries, suggestions, or collaborations, reach out to:  
📩 mantejjosan@example.com  

If you like this project, don't forget to ⭐ the repo! 😊