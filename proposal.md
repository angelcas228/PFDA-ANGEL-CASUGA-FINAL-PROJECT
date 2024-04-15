# Random Watermark Generator

## Repository
<(https://github.com/angelcas228/PFDA-ANGEL-CASUGA-FINAL-PROJECT.git)>

## Description
A program that will randomly place a watermark, lower its opacity, and randomly place it on any picture you're uploading. It's useful for watermarking
your artwork faster to prevent someone from stealing your artwork or not being credited when uploading work online.

## Features
- Feature 1
	- Will lower the opacity of the watermark. Will either be set to a fixed opacity or a random opacity from a set range
- Feature 2
	- Will randomly place the watermark within the parameters of the picture's size

## Challenges
- In order for the watermark to not get cut off on the page, I will have to make sure the watermark can only be placed in a scaled down rectangle within the actual picture
- Figuring out how to set the random range within the scaled down rectangle
- While I can randomly place the watermark with random.randrange, it will have to round the smaller rectangle parameters to whole numbers OR being rounded to the 0.01 and see if that
  allows for more random placement of the image
- If able to, find out better ways to blend in the watermark than just lowering the opacity
- If able to, scaling the watermark up or down depending on the size of the drawing and the watermark's size
- User input, if the user wants to scale up the watermark or doesn't want to, they can choose Y/N

## Outcomes
Ideal Outcome:
- Can put a watermark within the desired image without being cut off, blended into the image with a lowered opacity, and can export the new image into a desired folder. Can also
  successfully calculate the parameters inside the desired image with user input

Minimal Viable Outcome:
- Program is able to randomly place watermark in the image and lower the opacity of watermark. Can export the image into a file

## Milestones

- Week 1
  1. Figure out how many functions minimum will be used in the program
  2. Outline basic functions to be used in the program

- Week 2
  1. Figuring out the needed math and calculations to scale the parameters of the desired image 
  2. Watermark can be generated within these parameters

- Week 3 (Final)
  1. Lowering the opacity of the watermark, option for a fixed number or within a set range
  2. scaling the watermark up or down if desired
