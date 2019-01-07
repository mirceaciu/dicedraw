# dicedraw
Create a dice portrait of yourself with the help of this script.

Point it to a portrait photo (color or grayscale) and set the desired number of dice per row. 

It will calculate how many dice you will need to recreate the portrait and will output several helping files:
 
 - color image with dice numbers grid overlay
 - grayscale image with dice numbers grid overlay
 - grayscale image of actual dice faces rendering
 - csv file with row by row mapping of dice placement
 
 
 ## output rendering
  
  ![full_dice_rendering](https://github.com/mirceaciu/dicedraw/blob/master/output-to-dice.png)

 
 ## dice rendering close-up
 
 ![dice_rendering_close_up](https://github.com/mirceaciu/dicedraw/blob/master/cropped-dice.png)


Each row of the portrait has two rows in the csv file:

```
1,-,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
1,-,01,01,01,01,01,01,01,01,01,02,01,01,01,01,01,01,01,01,01,01
```

First csv column is the portrait row number. First row is the portrait column number and the second is the corresponding die face number. 

Each portrait row from the csv file is separated by a new line:

```
1,-,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
1,-,01,01,01,01,01,01,01,01,01,02,01,01,01,01,01,01,01,01,01,01

2,-,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
2,-,01,01,01,01,01,01,01,02,05,05,04,02,01,01,01,01,01,01,01,01

3,-,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
3,-,01,01,01,01,01,01,03,04,05,05,05,05,04,02,01,01,01,01,01,01

4,-,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20
4,-,01,01,01,01,01,02,05,06,05,06,06,06,05,04,02,01,01,01,01,01
```

Built with Python3.5 and OpenCv on Ubuntu16.04. Check [this link](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/) for a guide on how to install OpenCv.
