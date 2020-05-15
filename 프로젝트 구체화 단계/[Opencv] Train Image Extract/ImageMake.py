import cv2

step = 20

def videoToimage(file_path, save_path):
    video = cv2.VideoCapture(file_path)
    count = 0
    while True:
        ret, image = video.read()
        if ret == False:
            print("Video read is Failed.")
            break
        if count % step == 0:
            fname = "frame_{}_image.jpg".format(count)
            cv2.imwrite(save_path+fname, image)
            print("{} image saved.".format(count))
        count += 1

