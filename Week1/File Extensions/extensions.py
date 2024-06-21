def main():

    file_name = input("File name: ")

    file_name = file_name.strip()

    file_name_lower = file_name.lower()

    if file_name_lower.endswith(".gif"):
        media_type = "image/gif"
    elif file_name_lower.endswith((".jpg", ".jpeg")):
        media_type = "image/jpeg"
    elif file_name_lower.endswith(".png"):
        media_type = "image/png"
    elif file_name_lower.endswith(".pdf"):
        media_type = "application/pdf"
    elif file_name_lower.endswith(".txt"):
        media_type = "text/plain"
    elif file_name_lower.endswith(".zip"):
        media_type = "application/zip"
    else:
        media_type = "application/octet-stream"

    print(media_type)

main()
