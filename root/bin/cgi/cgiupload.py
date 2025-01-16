#!/usr/bin/env python3

import os
import cgi
import uuid

UPLOAD_DIR = os.getenv("UPLOAD_DIR")


def get_file_extension(content_type):
    # Map common content types to file extensions
    mime_map = {
        # Images
    "image/png": ".png",
    "image/jpg": ".jpg",
    "image/jpeg": ".jpeg",
    "image/gif": ".gif",
    "image/bmp": ".bmp",
    "image/webp": ".webp",
    "image/tiff": ".tiff",

    # Documents
    "application/pdf": ".pdf",
    "application/octet-stream": ".jpg",
    "application/msword": ".doc",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/vnd.ms-excel": ".xls",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
    "application/vnd.ms-powerpoint": ".ppt",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
    "text/plain": ".txt",
    "application/json": ".json",
    "text/csv": ".csv",
    "text/html": ".html",
    "application/xml": ".xml",

    # Audio
    "audio/mpeg": ".mp3",
    "audio/wav": ".wav",
    "audio/ogg": ".ogg",
    "audio/aac": ".aac",

    # Video
    "video/mp4": ".mp4",
    "video/mpeg": ".mpeg",
    "video/ogg": ".ogv",
    "video/webm": ".webm",

    # Archives
    "application/zip": ".zip",
    "application/x-tar": ".tar",
    "application/x-7z-compressed": ".7z",
    "application/x-rar-compressed": ".rar",
    "application/gzip": ".gz",

    # Fonts
    "font/ttf": ".ttf",
    "font/otf": ".otf",
    "font/woff": ".woff",
    "font/woff2": ".woff2"
    }
    return mime_map.get(content_type, ".")  # Default to no extension if unknown


def upload_file():
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)  # Ensure the upload directory exists

    # Get the form data
    form = cgi.FieldStorage()

    # Iterate over all fields in the form
    for field_name in form.keys():
        file_item = form[field_name]

        # Check if the field contains a file
        if file_item.file:
            try:
                # Determine the filename
                if file_item.filename:  # If a filename is provided
                    filename = os.path.basename(file_item.filename)
                else:  # If no filename is provided
                    content_type = file_item.type  # Get the content type
                    extension = get_file_extension(content_type)  # Get extension
                    filename = f"file_{uuid.uuid4().hex}{extension}"

                filepath = os.path.join(UPLOAD_DIR, filename)

                # Save the file content based on its type
                with open(filepath, 'wb' if file_item.type not in ["text/plain", "application/json"] else 'w') as f:
                    content = file_item.file.read()

                    # If the file type is text and the content is bytes, decode it
                    if file_item.type in ["text/plain", "application/json"]:
                        if isinstance(content, bytes):  # Decode only if content is bytes
                            content = content.decode('utf-8')
                        f.write(content)  # Write text content
                    else:
                        if isinstance(content, str):  # Encode to bytes if content is a string
                            content = content.encode('utf-8')
                        f.write(content)  # Write binary content

                # Send a success message
                print("<html><body>")
                print(f"<h2>File uploaded successfully!</h2>")
                print(f"<p>Field name: {field_name}</p>")
                print(f"<p>File saved as: {filename}</p>")
                print("</body></html>")
                print("<a href='/uploader.html'><button>Back</button></a>")
                return  # Exit after successful upload
            except Exception as e:
                # Handle any unexpected errors
                print("Content-Type: text/html\n")
                print("<html><body>")
                print(f"<h1>Error uploading file</h1>")
                print(f"<p>{str(e)}</p>")
                print("</body></html>")
                print("<a href='/uploader.html'><button>Back</button></a>")
                print("<a href='/index.html'><button>Front-Page</button></a>")
                return

    # If no file was uploaded
    print("<html><body><h1>No file uploaded. Please select a file to upload.</h1></body></html>")
    print("<a href='/uploader.html'><button>Back</button></a>")
    print("<a href='/index.html'><button>Front-Page</button></a>")


if __name__ == "__main__":
    upload_file()