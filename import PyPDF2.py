import PyPDF2

def extract_text_from_pdf(pdf_paths):
    """
    This function extracts text from a list of PDF files and returns the text as a string.
    """
    text = ''
    
    # Loop through each PDF file path in the list
    for pdf_path in pdf_paths:
        # Open the PDF file in read-binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Extract the text from each page of the PDF file
            numPages = len(pdf_reader.pages)
            for page_num in range(numPages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            
            # Close the PDF file
            pdf_file.close()
    
    return text



pdf_paths = ["Cancer_CT_Eligibility_Criteria_Prior_or_Concurrent_Malignan.pdf", "Pulmonary_Tuberculosis.pdf"]
text = extract_text_from_pdf(pdf_paths)

print(text)


