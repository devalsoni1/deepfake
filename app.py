import torch
import shutil
import os
import subprocess

print("CUDA available:", torch.cuda.is_available())

# For Colab-style interactive inputs (use terminal or handle with defaults)
flush_repo = input("Do you want to flush the existing repository and start fresh? (yes/no): ").strip().lower()

if flush_repo == 'yes':
    print("Flushing the repository folder locally...")
    subprocess.run(["rm", "-rf", "/content/ROOP-FLOYD"])

    # Check if Drive is mounted
    if os.path.exists('/content/drive'):
        delete_drive_repo = input("Do you also want to delete the repository from Google Drive? (yes/no): ").strip().lower()
        if delete_drive_repo == 'yes':
            drive_repo_path = '/content/drive/MyDrive/ROOP-FLOYD'
            if os.path.exists(drive_repo_path):
                print("Deleting the repository from Google Drive...")
                shutil.rmtree(drive_repo_path)
            else:
                print("No repository found on Google Drive.")
else:
    print("Keeping the existing repository folder.")

# Clone the repository
subprocess.run(["git", "clone", "https://codeberg.org/Cognibuild/ROOP-FLOYD.git"])
os.chdir("ROOP-FLOYD")

# Install dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"])
subprocess.run(["pip", "install", "gradio==5.13.0", "--upgrade"])
subprocess.run(["pip", "install", "--upgrade", "fastapi"])
subprocess.run(["pip", "install", "--force-reinstall", "pydantic==2.10.6"])
subprocess.run(["pip", "install", "numpy<2.0"])

# Mount Google Drive (only works in Colab)
if not os.path.exists('/content/drive'):
    save_to_drive = input("Do you want to save the repository to Google Drive? (yes/no): ").strip().lower()

    if save_to_drive == 'yes':
        from google.colab import drive
        drive.mount('/content/drive')
        subprocess.run(["cp", "-r", "/content/ROOP-FLOYD", "/content/drive/MyDrive/ROOP-FLOYD"])
        print("Repository saved to Google Drive.")
else:
    print("Google Drive is already mounted.")

# Run the script
subprocess.run(["python", "run.py"])
