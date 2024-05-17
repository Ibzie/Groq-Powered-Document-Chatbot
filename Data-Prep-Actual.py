import os
import fitz

def extract_text_from_pdf(pdf_file_path):
    text = ''
    with fitz.open(pdf_file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def main():
    # Directory containing PDF files
    pdf_folder = 'Data'

    # Output file path
    output_file = 'output.txt'

    # Iterate over PDF files in the directory
    with open(output_file, 'a', encoding='utf-8') as f:
        for file_name in os.listdir(pdf_folder):
            if file_name.endswith('.pdf'):
                pdf_path = os.path.join(pdf_folder, file_name)
                text = extract_text_from_pdf(pdf_path)
                f.write(text + '\n\n')

    print("Text extracted from PDFs and saved to", output_file)

if __name__ == "__main__":
    main()
