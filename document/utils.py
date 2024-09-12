import docx
from docx.shared import Pt

def generator_file(file, data):
    doc = docx.Document(file)
    replace_dict = {}
    for item in data:
        replace_dict[item['key']] = item['answer']
    for paragraph in doc.paragraphs:
        for key, value in replace_dict.items():
            if key in paragraph.text:
                # Replace placeholder text with actual value
                paragraph.text = paragraph.text.replace(key, value)

            # Set the font of the entire paragraph to Times New Roman, size 12
                for run in paragraph.runs:
                    run.font.name = 'Times New Roman'
                    run.font.size = Pt(14)  # Set font size to 12 pt

# Save the modified document
        doc.save('gfg.docx')
