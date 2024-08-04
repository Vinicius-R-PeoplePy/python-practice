import os 
import shutil 
import logging 

# Configure logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to organize files into directories by extension 
def organize_files(directory):
    try:
        # Get list of files in the directory 
        files = os.listdir(directory)
        
        # Create a dictionary to hold file lists by extension 
        extension_map = {} 
        
        # Iterate through each file 
        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                # Split the file into name and extension 
                _, extension = os.path.splitext(file)
                
                # Remove the '.' from extension 
                extension = extension [1:] # removes the leading dot (.)
                
                # Create a directory for the extension if it doesn't exist 
                if not os.path.exists(os.path.join(directory, extension)):
                    os.makedirs(os.path.join(directory, extension))
                    
                # Get full path of the file 
                src_path = os.path.join(directory, file)
                dest_path = os.path.join(directory, extension, file)
                
                # Attempt to change file permissions 
                try: 
                    os.chmod(src_path, 0o755) # Set permissions to rwxr-xr-x
                except Exception as e:
                    logger.error(f"Failed to move {file}: {str(e)}")
                    
                # Move the file to the directory corresponding to its extension
                try: 
                    shutil.move(src_path, dest_path)
                    logger.info(f"MOved {file} to '{extension}' directory")
                except Exception as e:
                    logger.error(f"Failed to move {file}: {str(e)}")
                    
                
                # Optionally, store the file path in the extension map 
                if extension not in extension_map:
                    extension_map[extension] = [] 
                extension_map[extension].append(file)
                
        # Print summary of organization 
        logger.info("Files organized succesfully!")
        for ext, files in extension_map.items():
            logger.info("Moved {len(files)} files to '{ext}' directory")
            
    except Exception as e:
        logger.error(f"Error organizing files: {str(e)}")
        
# Example usage: 
if __name__ == "__main__":
    directory = '/home/ovni/Área de trabalho'
    organize_files(directory)
    
'''

-> os.chmod(): Added a 'try-except' block to attempt changing file permissions
('0o775' corresponds to 'rwxr-xr-x' permissions).

-> Error Handling: Added error handling around the 'shutil.move()' operation to log and handle any exceptions that occur during file movement. 

-> Logging: Enhanced logging to provide more detailed information about permission changes and file movements. 


'''