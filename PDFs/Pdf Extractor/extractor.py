from PyPDF2 import PdfReader, PdfWriter
import os

def extract_pages(input_pdf_path, output_pdf_name, start_page, end_page):
    # Create PDF reader object
    reader = PdfReader(input_pdf_path)
    
    # Create PDF writer object
    writer = PdfWriter()
    
    # Add pages to writer (subtract 1 from page numbers since PyPDF2 uses 0-based indexing)
    for page_num in range(start_page - 1, end_page):
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
    
    # Save the output PDF
    if not output_pdf_name.endswith('.pdf'):
        output_pdf_name += '.pdf'
    
    with open(output_pdf_name, 'wb') as output_file:
        writer.write(output_file)
    print(f"Created: {output_pdf_name}")

def main():
    # Get the input PDF file
    while True:
        input_pdf = input("Enter the path to your input PDF file: ")
        if os.path.exists(input_pdf):
            break
        print("File not found. Please try again.")

    # Get number of sections
    while True:
        try:
            num_sections = int(input("How many sections do you want to extract? "))
            if num_sections > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Process each section
    for i in range(num_sections):
        print(f"\nSection {i + 1}:")
        output_name = input("Enter output file name: ")
        
        while True:
            try:
                start_page = int(input("Enter starting page number: "))
                end_page = int(input("Enter ending page number: "))
                if start_page > 0 and end_page >= start_page:
                    break
                print("Invalid page numbers. Start page must be positive and end page must be >= start page.")
            except ValueError:
                print("Please enter valid numbers.")
        
        try:
            extract_pages(input_pdf, output_name, start_page, end_page)
        except Exception as e:
            print(f"Error processing section {i + 1}: {str(e)}")

if __name__ == "__main__":
    main()
