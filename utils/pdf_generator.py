from fpdf import FPDF

def create_pdf(content, filename="resume.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)
    return filename