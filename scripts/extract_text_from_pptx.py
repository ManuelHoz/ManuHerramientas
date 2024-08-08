import os
from pptx import Presentation

def extract_text_from_pptx(pptx_path):
    prs = Presentation(pptx_path)
    text_runs = []

    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text_runs.append(shape.text)

    return "\n".join(text_runs)

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def extract_text_from_all_pptx_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pptx"):
            pptx_path = os.path.join(directory, filename)
            text = extract_text_from_pptx(pptx_path)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            txt_path = os.path.join(directory, txt_filename)
            save_text_to_file(text, txt_path)
            print(f"Extracted text from {filename} to {txt_filename}")

if __name__ == "__main__":
    directory = os.getcwd()  # Current directory
    extract_text_from_all_pptx_in_directory(directory)
