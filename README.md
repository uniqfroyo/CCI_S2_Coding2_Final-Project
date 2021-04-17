# CCI_S2_Coding2_Final-Project

## Project Summary

Use opencv, numpy, matplot, scikit-image in Python to create different image filters to show the beautiful scenery of London, then use dash to show before after as an album.

‘When a man is tired of London, he is tired of life.’  Everytime I walk on the streets of London, I feel that every landscape is an oil painting. This reminds me of one of my favourite impressionism artists -Claude Monet. 

As a overseas student, the life of studying in London is a memory that I will never forget in my life.  So I hope to record the beautiful scenery of London in the form of paintings and make it into 'an album'.

![image](https://miro.medium.com/max/1400/1*8-M1SqpIR4UpcLnscn7WWw.png)

## Process

**Oil Painting Effect filter** [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_Oil%20Painting%20Effect)

It is included in cv2.xphoto() which also has several other cool functions like image inpainting, white balance, image denoising, etc.
Step 1: Superpixel segmentation of the area
Step 2: Substitute the original pixel for the material sample of the segmented area

![image](https://miro.medium.com/max/1400/1*r7_dhyCAC6mPncjOHk7dMQ.png)


**Pointillist Art filter** [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_Pointillist%20Art)

To do this in Python, our first step is to compute the most used colors for which Kmeans is used. I used a color palette of 20 which means that the dots will be made by 20 most used colors will be present in the image. A suitable radius size is calculated for the dots according to the image size. Then we loop over the image and find the color closest to the dot, using which the circle is drawn.

![image](https://miro.medium.com/max/1400/1*VfvGC5eNRuYeQsJizL7Jsg.png)


**Frosted glass filter** [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_Frosted%20glass)

The double layer circulates through each pixel of the image, and then uses the defined random number to replace the color of each neighborhood pixel.

![image](https://miro.medium.com/max/1400/1*ie1b0x8yxKmloAI0YSd0Aw.png)


**Pencil sketch filter** [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_%20Pencil%20sketch)

The cv2.bilateralFilter() function is called to perform bilateral filtering on the original image. The filter can effectively remove noise while ensuring clear boundary and shorten pixel value to one value every 7 gray levels. It uses both spatial Gaussian weight and gray similarity Gaussian weight to ensure that the boundary will not be blurred.

![image](https://miro.medium.com/max/1400/1*_6J_nq__k5HLbH3AO2sgNA.png)


**Light ripple filter**  [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_Light%20ripple)

Calculate the center position of wave, and then call np.sin() function to calculate the wave transfer function, and finally form the light wave special effect.

![image](https://miro.medium.com/max/1400/1*uS8T0rLg45ZP5prHZ06aRw.png)

## Final Outcome

I use dash to visualize them in Reactive Web Apps. You’ll find a [getting started guide here](https://plotly.com/dash/) and the [Dash code on GitHub here](https://github.com/plotly/dash).
Dash is a user interface library for creating analytical web applications. Those who use Python for data analysis, data exploration, visualization, modelling, instrument control, and reporting will find immediate use for Dash. [link](https://github.com/YIDAI1111/CCI_S2_Coding2_Final-Project/tree/main/image_Light%20ripple)

I choose 'streets of London' as my BGM. I hope this can takes you back to your London memories.

[More details in blog](https://www.froyodai.com/post/cci-s2-coding2_final-project_my-album-of-london)

[Video](https://www.youtube.com/watch?v=HIquP0WDUDQ&t=11s)


## Useful resource：


[OpenCV with Python tutorial](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq&index=2))

[Python image manipulation tools](https://opensource.com/article/19/3/python-image-manipulation-tools)

Opencv library: https://github.com/opencv/opencv-python 

Dash introduction: https://medium.com/plotly/introducing-dash-5ecf7191b503 

Dash core component library: 

https://github.com/plotly/dash-core-components

https://dash.plotly.com/dash-core-components/graph 

Machine learning in creating art and music 

Create Pointillism Art from Digital Images

[python-opencv displays blur, beautification, watercolor and other effects on videos and images ](https://www.programmersought.com/article/77574934129/)
 

