import csv

def escape_special_chars(text):
    """ Escape special characters for LaTeX and handle specific cases like π """
    if isinstance(text, str):
        text = text.replace('&', '\\&')  # Escape & for LaTeX
        text = text.replace('π', '$\\pi$')  # Replace π with LaTeX math mode
        text = text.replace('#', '\\#')
    return text

table_content = ''  
unique_iterations = set()  

with open('data.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        iteration = row['Iteration']
        if iteration in unique_iterations:
            continue  

        unique_iterations.add(iteration)  
        smiles = escape_special_chars(row['SMILES'])
        modification = escape_special_chars(row['Modification'])
        docking_score = row['Docking Score']

        table_content += f"{iteration} & {smiles} & {modification} & {docking_score} \\\\\n"
        
print(table_content)