format = input("File name:").lower()
format = format.split('.')[1]

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
elif format == 'text':
    print(")