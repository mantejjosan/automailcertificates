from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd
import os

# Register fonts if needed
# pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

def generate_certificates(csv_file, output_folder, background_image=None, refno=None):
    """
    Generate certificates from a CSV file with center-aligned text fields.
    
    Parameters:
    - csv_file: Path to the CSV file containing participant data
    - output_folder: Folder to save the generated certificates
    - background_image: Path to certificate background image (optional)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Read CSV data
    df = pd.read_csv(csv_file)
    
    # Page settings
    page_width, page_height = landscape(A4)
    
    # Process each row in the CSV file
    for idx, row in df.iterrows():
        name = row['name']
        branch = row['branch']
        urn = str(row['urn'])
        
        # Generate filename for the certificate
        pdf_filename = f"{name.replace(' ', '_')}_{urn}_certificate.pdf"
        pdf_path = os.path.join(output_folder, pdf_filename)
        
        # Create canvas for the certificate
        c = canvas.Canvas(pdf_path, pagesize=landscape(A4))
        
        # Add background image if provided
        if background_image and os.path.exists(background_image):
            c.drawImage(background_image, 0, 0, width=page_width, height=page_height)
        
        # Set font
        c.setFont("Helvetica-Bold", 16)
        
        # Draw the ref no.
        c.drawCentredString(page_width/8 +68, page_height/2 + 119, refno)
        # Draw the name (centered)
        c.drawCentredString(page_width/2, page_height/2 + 10, name)
        
        # Draw the branch (centered)
        c.setFont("Helvetica", 14)
        c.drawCentredString(page_width/8 + 60, page_height/2 - 25, f"{urn}")
        
        # Draw the URN (centered)
        c.drawCentredString(page_width/2, page_height/2 - 25, f"{branch}")
        
        # Save the certificate
        c.save()
        print(f"Generated certificate for {name} (URN: {urn})")

# Example usage
if __name__ == "__main__":
    csv_file = "participants_data.csv"
    output_folder = "generated_certificates"
    background_image = "certificate_template.jpeg"  # Your certificate background
    refno = 'GNDEC/NSS/19/25/01'
    generate_certificates(csv_file, output_folder, background_image, refno)