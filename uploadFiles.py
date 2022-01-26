import dropbox
from dropbox.files import WriteMode
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for files in files:
                local_file = files
                print(local_file)
                relative_path = os.path.relpath(local_file,file_from)
                relative_files = os.path.join(file_from,local_file)
                dropbox_path = os.path.join(relative_path,file_to)
                with open(relative_files, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
                    print("This file has been uploaded successfully\n")

            for dirs in dirs:
                local_dirs = dirs
                print(local_dirs)
                print("This is directory\n")
                file_from = os.path.join(file_from,local_dirs)

def main():
    access_token = 'sl.BA1RL6jahq63axw1M4RsQYB2unwEAgt5avrg1L_xUuX5DTkGCZEZXBDNTIkVLly-E65mhprQzQao0xVRzl1cteF1_fsD-ZmKR6ct4GwXr9YwFowX35Wab0JzUB2UqRfiAyKH4l7tUD8W'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to upload: ")
    file_to = '/upload_files'
     # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()