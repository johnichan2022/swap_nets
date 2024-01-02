import sys
import os

def replace_values(lookup_filename, file_to_modify):
    try:
        # Read the lookup file and create a dictionary with second column as keys and third column as values
        lookup_dict = {}
        with open(lookup_filename, 'r') as lookup_file:
            for line in lookup_file:
                columns = line.strip().split('\t')
                if len(columns) >= 2:
                    lookup_dict[columns[0]] = columns[1]

        # Add the line to print the dictionary
        print("Lookup Dictionary:")
        for key, value in lookup_dict.items():
            print(f"{key}: {value}")

              # Read the file to be modified and replace values based on the lookup dictionary
        modified_lines = []
        output_file_name = f"{os.path.splitext(file_to_modify)[0]}_modified{os.path.splitext(file_to_modify)[1]}"

        with open(file_to_modify, 'r') as input_file:
            for line in input_file:
                columns = line.strip().split()
                modified_columns = [lookup_dict.get(column, column) for column in columns]
                modified_lines.append(' '.join(modified_columns))

        # Write the modified content to a new file
        with open(output_file_name, 'w') as output_file:
            output_file.write('\n'.join(modified_lines))

        print(f"Values replaced successfully. Modified content saved to {output_file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py lookup_file.txt file_to_modify.txt")
    else:
        lookup_file = sys.argv[1]
        file_to_modify = sys.argv[2]
        replace_values(lookup_file, file_to_modify)
