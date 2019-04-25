import glob
files = glob.glob("../fs/models/*.ini")
files += glob.glob("../fs/layout/*.ini")
files += glob.glob("../fs/media/*.ini")
files += glob.glob("../fs/template/*.ini")
files += glob.glob("../fs/*.ini")

for f in files:
    # Open
    fid = open(f, 'rb')
    data = fid.read()
    fid.close()

    # Replace
    data = data.replace(b'\x00',b'')
    data = data.replace(b'\r\n',b'\n')
    data = data.replace(b'\n\r',b'\n')

    while data[len(data)-1] == 10:
        data = data[0:len(data)-1]
    data += b'\n'

    print(len(data))

    #write
    #print(data)
    fid = open(f, 'wb')
    fid.write(data)
    fid.close()