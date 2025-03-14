def read_and_modify_file():
   
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename  

    try:
       
        with open(input_filename, 'r') as file:
            content = file.read() 
            modified_content = content.upper()  

        
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()
