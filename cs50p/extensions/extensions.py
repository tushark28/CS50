format = input("File name: ").lower().strip(" ")
format = format.split('.')
format = format[len(format) - 1]

if format == 'gif':
    print("image/gif")
elif format == 'jpg' or format == 'jpeg':
    print('image/jpeg')
elif format == 'zip':
    print('application/zip')
elif format == 'pdf':
    print('application/pdf')
elif format == 'png':
    print("image/png")
elif format == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")