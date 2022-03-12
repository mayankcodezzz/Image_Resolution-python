#find the resolution of the image
def jpeg_res(filename):
    with open (filename,'rb') as img_file:
        #height of img is at position 164th
        img_file.seek(163)

        #read the 2 bytes
        a=img_file.read(2)
        print(a[0],a[1])
        #height calulation
        height=(a[0]<<8)+a[1]
        #next 2 bytes
        a=img_file.read(2)
        #width calculation
        width=(a[0]<<8)+a[1]
        print(type(a))
        print(type(height),type(width))
        print(a[0],a[1])
    print("the resoltion of the image is :",width,"x",height)
jpeg_res("img3.jpg")
