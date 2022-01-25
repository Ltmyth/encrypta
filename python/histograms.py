import matplotlib.pyplot as plt
import cv2 as cv
import os.path


def draw_image_histogram(src,dest):
    # read image
    img= cv.imread(src)
    
    if os.path.isfile(dest) and os.access(dest, os.R_OK):
        print("File exists,Deleting and recreating")
        os.remove(dest)
    else:
       print("File doesnot exist, Creating")

    hist = cv.calcHist([img],[0],None,[256],[0,256])
    plt.title("Image Histogram")
    plt.xlabel("Value")
    plt.ylabel("Pixels")
    plt.plot(hist, label='Original Image')  
    plt.savefig(dest)
    print("Histogram added successfully")

draw_image_histogram('images/kids.png','images/kids_histogram.png')
draw_image_histogram('encrypted/lsb_encoded_kids.png','images/kids_lsb_histogram.png')

draw_image_histogram('images/journey.png','images/journey_histogram.png')
draw_image_histogram('encrypted/lsb_encoded_journey.png','images/journey_lsb_histogram.png')

draw_image_histogram('images/girafe.png','images/girafe_histogram.png')
draw_image_histogram('encrypted/lsb_encoded_girafe.png','images/girafe_lsb_histogram.png')






