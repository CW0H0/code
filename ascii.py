from PIL import Image

def get_char(r, g, b, alpha=256):
    ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' '
    gray = (2126 * r + 7152 * g + 722 * b) / 10000
    unit = 256 / len(ascii_char)
    return ascii_char[int(gray/unit)]

def convert_to_ascii(img_path, target_width=80):
    img = Image.open(img_path)
    
    width, height = img.size
    aspect_ratio = height/width
    
    target_height = int(target_width * aspect_ratio * 0.5)
    
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    txt = ""
    for i in range(target_height):
        for j in range(target_width):
            pixel = img.getpixel((j, i))
            if len(pixel) == 4:
                r, g, b, a = pixel
            else:
                r, g, b = pixel
                a = 256
            txt += get_char(r, g, b, a)
        txt += '\n'
    return txt

if __name__ == '__main__':
    img_path = r"C:\Users\Administrator\Desktop\code\your_image.png"
    result = convert_to_ascii(img_path, target_width=60)
    print(result)