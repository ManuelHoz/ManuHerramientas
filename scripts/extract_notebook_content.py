import os
import nbformat

def extract_notebook_content(notebook_file):
    """Extract markdown and code cells from a Jupyter notebook."""
    with open(notebook_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    extracted_content = []
    for cell in nb.cells:
        if cell.cell_type == 'markdown' or cell.cell_type == 'code':
            extracted_content.append(cell.source)
    
    return '\n\n'.join(extracted_content)

def main():
    """Main function to extract and save notebook content."""
    notebook_dir = os.getcwd()  # Get current directory
    output_file = 'notebooks_content.txt'
    
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename in os.listdir(notebook_dir):
            if filename.endswith('.ipynb'):
                output.write(f"## {filename}\n\n")
                content = extract_notebook_content(filename)
                output.write(content)
                output.write("\n\n" + "#" * 80 + "\n\n")
    
    print(f"Content extracted and written to {output_file}")

if __name__ == "__main__":
    main()
