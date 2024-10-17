import os

def txt_to_csv(file_path, output_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        with open(output_path, 'w') as output:
            for i, line in enumerate(lines):
                if i == 0:
                    # Skip the first line
                    continue
                if i == 1:
                    # Delete the last space in the first line
                    line = line[:-2] + "\n"
                # Replace commas with dots for decimal points
                line = line.replace(',', '.')
                # Replace spaces with commas for CSV format
                output.write(line.replace(' ', ','))

def main():
    input_dir = 'datasets'
    output_dir = 'datasets_csv'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)
        if os.path.isdir(folder_path):
            output_folder_path = os.path.join(output_dir, folder)
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)
            
            for file in os.listdir(folder_path):
                if file.endswith('.txt'):
                    input_file_path = os.path.join(folder_path, file)
                    output_file_path = os.path.join(output_folder_path, file.replace('.txt', '.csv'))
                    txt_to_csv(input_file_path, output_file_path)

if __name__ == "__main__":
    main()
