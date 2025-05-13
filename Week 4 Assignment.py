def modify_content(content):
    """Example modification: convert to uppercase and add header"""
    return f"Modified File:\n\n{content.upper()}"

def main():
    while True:
        try:
            # Get filename from user
            filename = input("\nEnter a filename to process (or 'q' to quit): ").strip()
            
            if filename.lower() == 'q':
                print("Exiting program...")
                break

            # Read file with error handling
            try:
                with open(filename, 'r') as file:
                    content = file.read()
            except FileNotFoundError:
                print(f"Error: The file '{filename}' does not exist.")
                continue
            except PermissionError:
                print(f"Error: Permission denied to read '{filename}'.")
                continue
            except IsADirectoryError:
                print(f"Error: '{filename}' is a directory, not a file.")
                continue
            except UnicodeDecodeError:
                print(f"Error: Could not decode '{filename}' as text file.")
                continue

            # Process content
            modified = modify_content(content)
            
            # Create new filename
            new_filename = f"{filename}_modified.txt"

            # Write to new file with error handling
            try:
                with open(new_filename, 'w') as new_file:
                    new_file.write(modified)
                print(f"Success! Modified file saved as '{new_filename}'")
                break
            except PermissionError:
                print(f"Error: Permission denied to write to '{new_filename}'.")
            except Exception as e:
                print(f"Unexpected error while writing: {str(e)}")

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()