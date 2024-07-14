import os
import io
from PIL import Image
from rembg import remove, new_session
from tqdm import tqdm

# Define your directories
input_dir = "/home/fabi/Temporary/Downloads/test/"
output_dir = "/home/fabi/Temporary/Downloads/"

# Create output_dir if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Create a new session with the isnet-general-use model
model_name = "isnet-general-use"
session = new_session(model_name)

# Get the total number of JPEG files
total_files = sum([len(files) for r, d, files in os.walk(input_dir) if any(fname.endswith('.jpg') for fname in files)])

# Initialize the progress bar
progress_bar = tqdm(total=total_files, unit="file", ncols=70)

# Loop over all directories in input_dir
for dir_name in os.listdir(input_dir):
    # Get the full paths to the input and output directories for this subdirectory
    input_subdir = os.path.join(input_dir, dir_name)
    output_subdir = os.path.join(output_dir, dir_name)

    # Create the output subdirectory if it does not exist
    os.makedirs(output_subdir, exist_ok=True)

    # Loop over all files in the input subdirectory
    for file_name in os.listdir(input_subdir):
        # Only process JPEG files
        if file_name.lower().endswith(".jpg"):
            # Get the full paths to the input and output files
            input_file = os.path.join(input_subdir, file_name)
            output_file = os.path.join(output_subdir, file_name)

            # Set the description to the current file name
            progress_bar.set_description(f"Processing {file_name}")

            # Open the input file, remove the background using the isnet-general-use model, and save the result
            with open(input_file, 'rb') as i:
                img_data = remove(i.read(), session=session)
                
            # Load the image without background as a PIL.Image
            img_no_bg = Image.open(io.BytesIO(img_data))
            
            # Create a new image with white background
            img_white_bg = Image.new("RGBA", img_no_bg.size, "WHITE")
            img_white_bg.paste(img_no_bg, (0, 0), img_no_bg)

            # Save the final image as JPEG
            img_white_bg.convert("RGB").save(output_file, format='jpeg')

            # Update the progress bar
            progress_bar.update()

            # Clear the description for the next file
            progress_bar.set_postfix(clear=True)

# Close the progress bar
progress_bar.close()

