import img2pdf
import os
import zipfile

# Specify the folder containing your CBZ files and the output folder for PDFs
input_folder = 'input/folder/of/cbzs'
output_folder = 'output_pdfs'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a list of all CBZ files in the folder
cbz_files = [file for file in os.listdir(input_folder) if file.lower().endswith('.cbz')]

# Sort the list of CBZ files if needed
cbz_files.sort()

# Iterate through each CBZ file and convert it to PDF
for cbz_file in cbz_files:
    cbz_path = os.path.join(input_folder, cbz_file)
    pdf_name = os.path.splitext(cbz_file)[0] + '.pdf'
    pdf_path = os.path.join(output_folder, pdf_name)
    
    with zipfile.ZipFile(cbz_path, 'r') as cbz_archive:
        image_files = [file for file in cbz_archive.namelist() if file.lower().endswith('.png')]
        image_files.sort()
        
        image_paths = [cbz_archive.extract(image_file, path=output_folder) for image_file in image_files]
        
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(img2pdf.convert(image_paths))
        
        for image_path in image_paths:
            os.remove(image_path)
    
    print(f"CBZ to PDF conversion complete: {pdf_name}")

print("All CBZ files converted to PDFs.")
