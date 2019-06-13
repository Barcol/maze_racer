import cv2


def read_bmp(image_path: str):
    image = cv2.imread(image_path)
    text_output = open("maze.txt", "w+")
    x, y = 0.0, 0.0
    for row in image:
        for pixel in row:
            text_output.write(f"{x:0.2f},{y:0.2f} ")
            if (pixel[0] > 250) and (pixel[1] > 250) and (pixel[2] > 250):
                text_output.write("WHITE")
            elif (pixel[0] < 10) and (pixel[1] < 10) and (pixel[2] < 10):
                text_output.write("BLACK")
            elif (pixel[0] > pixel[1]) and (pixel[0] > pixel[2]):
                text_output.write("RED")
            elif (pixel[1] > pixel[0]) and (pixel[1] > pixel[2]):
                text_output.write("GREEN")
            elif (pixel[2] > pixel[1]) and (pixel[2] > pixel[0]):
                text_output.write("BLUE")
            text_output.write("\n")
            x += 0.1
        y += 0.1
        x = 0
    text_output.close()
