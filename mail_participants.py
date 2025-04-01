import os
import smtplib
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Email credentials (Use environment variables for security)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") # Use App Password if using Gmail

# Paths
CSV_FILE = "test_participants.csv"
PDF_FOLDER = "test_certificates"

def load_email_mapping(csv_file):
    """Load URN to Email mapping from CSV file"""
    df = pd.read_csv(csv_file)
    urn_email_map = dict(zip(df["urn"].astype(str), df["email"]))  # Ensure URN is a string
    return urn_email_map

def send_email(to_email, subject, body, pdf_path):
    """Send email with the PDF attachment"""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(body)

    # Attach the PDF
    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:  # Use SMTP_SSL for security
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"Sent email to {to_email} with {os.path.basename(pdf_path)}")

def main():
    urn_email_map = load_email_mapping(CSV_FILE)

    for i, (key, val) in enumerate(urn_email_map.items()):
        print(f"{i+1}. URN: {key}, Email: {val}")

    final_validation = input(f"Found {len(urn_email_map)} emails. Mail all? (y/n): ").lower()[0]

    if final_validation == 'n':
        print("Cancelling event...")
        return
    
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            urn = filename.split("_")[-2]  # Extract URN from filename
            if urn in urn_email_map:
                email = urn_email_map[urn]
                pdf_path = os.path.join(PDF_FOLDER, filename)
                
                # Send email
                send_email(
                    to_email=email,
                    subject="Your Participation Certificate from NSS",
                    body="Dear participant,\n\nPlease find attached your certificate.\n\nBest regards,\nEvent Team",
                    pdf_path=pdf_path
                )
            else:
                print(f"Warning: No email found for URN {urn}")

if __name__ == "__main__":
    main()
