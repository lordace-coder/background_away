from rembg import remove

def remove_background(img_path,output_path):
    with open(img_path,"rb") as img:
        with open(output_path,"wb") as output:
            file = img.read()
            output.write(remove(file))


