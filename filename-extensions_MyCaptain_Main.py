filename = input("Please Enter a Filename: ")
extension = filename.split(".")[-1]
if extension == "py":
    print("Extension is Python")
elif extension == "txt":
    print("Extension is text")
elif extension == "png":
    print("Extension is High Quality Image")
elif extension == "pdf":
    print("Extension is Portable Document Format")
elif extension == "xls":
    print("Extension is Microsoft Excel Workbook")
elif extension == "bmp":
    print("Extension is Bitmap Image")
elif extension == "tiff":
    print("Extension is Tag Image File Format")
elif extension == "jpg":
    print("Extension is Compressed Image")
else:
    print("Other Extension")
    
