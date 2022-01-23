import matplotlib.pyplot as plt
import cv2 as cv
import os
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

draw_image_histogram('images/ugflag.jpg','images/ugflag_histogram.jpg')
draw_image_histogram('images/ugflag_aes_encoded.jpg','images/ugflag_aes_histogram.jpg')
draw_image_histogram('images/ugflag_lsb_encoded.png','images/ugflag_lsb_histogram.jpg')
draw_image_histogram('images/ugflag_rsa_encoded.jpg','images/ugflag_rsa_histogram.jpg')
draw_image_histogram('images/journey.jpg','images/journey_histogram.jpg')
draw_image_histogram('images/journey_aes_encoded.jpg','images/journey_aes_histogram.jpg')
draw_image_histogram('images/journey_lsb_encoded.png','images/journey_lsb_histogram.jpg')
draw_image_histogram('images/journey_rsa_encoded.jpg','images/journey_rsa_histogram.jpg')
draw_image_histogram('images/kla.jpeg','images/kla_histogram.jpeg')
draw_image_histogram('images/kla_aes_encoded.jpg','images/kla_aes_histogram.jpeg')
draw_image_histogram('images/kla_lsb_encoded.png','images/kla_lsb_histogram.jpg')
draw_image_histogram('images/kla_rsa_encoded.jpeg','images/kla_rsa_histogram.jpg')






