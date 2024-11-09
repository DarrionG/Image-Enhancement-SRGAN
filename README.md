# Image Enhancing Using SRGAN

This project is to test the capabilites of the SRGAN machine learning model. The end goal is to integrate the model with a small 1080p Raspberry Pi Camera Module V2-8 to enhance the images to a resolution of 2K. The image size of a 1080p picture is 1920 pixels wide by 1080 pixels tall. The hope is that the model will predict what a higher resolution image would look like, in this case the new image size will be 2560 pixels wide by 1440 pixels tall.

## Building the Dataset

The data set used to train and test the model consists of {quantity of images} images. The data set was be split into two parts, 80% is for training and 20% is for testing. Each original 2k image was reduced to a lower resolution 1080p version each with the same name in different directories. As apart of both the training and testing phase, the output image was verfied against the original 2k image.

The file structure that was used for this project is as follows:

     .
     │
     ├── SRGAN/
     │  │
     │  ├── HR_Data/    # Original 2K imgs
     │  │   │
     │  │   ├── img 1
     │  │   ├── img 2
     │  │   └── img 3
     │  │
     │  └── LR_Data/    # Transformed 1080p imgs
     │      │
     │      ├── img 1
     │      ├── img 2
     │      └── img 3


## Constructor Class

## Discriminator Class

## Training the Model

## Testing the Model

## Libraries Used
