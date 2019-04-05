I included two new versions of milestone 3 and 4 in this zip file.

For "findCoins", I implemented a pretty complex and slow iterating through pixels method. In version 2, I used adaptive thresholding which just solves so many problems and allows me to further implement some morphological filters to produce some cleaner edge detections.

For "houghCircle", I am still struggling with tweaking the parameters for the cv2.HoughCircles a little bit and it kept producing more circles than I wanted. At first I tried the method of doing binary thresholding and inverse binary thresholding and then combining the two but was not very successful. Now, with more morphological filters added and blurs applied, the program is able to produce a binary image with an acceptable accuracy.

I think adaptive thresholding performed surprisingly well when separating coins from background. My strange way of looking at three channels of BGR also worked pretty well but was too slow.