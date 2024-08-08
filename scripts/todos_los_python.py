import os

def combine_python_files(output_filename='combined_scripts.txt'):
    # Obtener la lista de archivos en el directorio actual
    files = [f for f in os.listdir() if f.endswith('.py')]
    
    with open(output_filename, 'w') as outfile:
        for filename in files:
            outfile.write(f'=== {filename} ===\n')
            with open(filename, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n\n')  # Separador entre archivos

if __name__ == "__main__":
    combine_python_files()
