import cv2
import csv

img = cv2.imread('sample.jpg') 
height, width, channels = img.shape 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv_gray_img = cv2.bitwise_not(gray_img)

# cv2.imshow('Gray image', gray)
dice_per_row = 120

z_fill_len = len(str(dice_per_row))

csv_row_columns = [str(element).zfill(z_fill_len) for element in list(range(1, dice_per_row+1))]

dice_side_dimension = int(width / dice_per_row)

x1, y1 = 0, 0
x2, y2 = dice_side_dimension, dice_side_dimension

max_gray = 255
min_gray = 0

start_range = min_gray
step_range = int(max_gray / 6)  # 6 dice faces
end_range = min_gray + step_range

dice_faces = []

for _ in range(0,6):
    dice_faces.append((start_range, end_range + 1 if end_range <= max_gray else max_gray + 1))
    start_range = end_range + 1
    end_range += step_range + 1

def draw_dice(x1, x2, y1, y2, dice_face):
    cv2.rectangle(inv_gray_img, (x1, y1), (x2, y2), int(240), -1)    
    cv2.rectangle(inv_gray_img, (x1, y1), (x2, y2), (255,0,0), 1)

    if dice_face == 1:
        c1 = (int(x1 + (x2-x1) / 2), int(y1 + (y2-y1) / 2))
        cv2.circle(inv_gray_img, c1, 4, int(255/dice_face), -1)
    
    if dice_face == 2:
        c1 = int(x1 + int((x2-x1) / 2)), int(y1 + int((y2 - y1) / 6))
        c2 = int(x1 + int((x2-x1) / 2)), int(y2 - int((y2 - y1) / 6))

        cv2.circle(inv_gray_img, c1, 2, int(255/dice_face), -1)
        cv2.circle(inv_gray_img, c2, 2, int(255/dice_face), -1)
    
    if dice_face == 3:
        c1 = int(x1 + int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 3))
        c2 = int(x1 + int((x2-x1) / 2)), int(y1 + int((y2 - y1) / 2))
        c3 = int(x2 - int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 3))

        cv2.circle(inv_gray_img, c1, 2, int(255/dice_face), -1)
        cv2.circle(inv_gray_img, c2, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c3, 2, int(255/dice_face), -1) 

    if dice_face == 4:
        c1 = int(x1 + int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 3))
        c2 = int(x2 - int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 3))
        c3 = int(x1 + int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 3))
        c4 = int(x2 - int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 3))

        cv2.circle(inv_gray_img, c1, 2, int(255/dice_face), -1)
        cv2.circle(inv_gray_img, c2, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c3, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c4, 2, int(255/dice_face), -1)
    
    if dice_face == 5:
        c1 = int(x1 + int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 6))
        c2 = int(x2 - int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 6))
        c3 = int(x1 + int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 6))
        c4 = int(x2 - int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 6))
        c5 = int(x1 + int((x2-x1) / 2)), int(y1 + int((y2 - y1) / 2))

        cv2.circle(inv_gray_img, c1, 2, int(255/dice_face), -1)
        cv2.circle(inv_gray_img, c2, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c3, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c4, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c5, 2, int(255/dice_face), -1) 
    
    if dice_face == 6:
        c1 = int(x1 + int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 6))
        c2 = int(x2 - int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 6))
        c3 = int(x1 + int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 6))
        c4 = int(x2 - int((x2-x1) / 3)), int(y2 - int((y2 - y1) / 6))
        c5 = int(x1 + int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 2))
        c6 = int(x2 - int((x2-x1) / 3)), int(y1 + int((y2 - y1) / 2))

        cv2.circle(inv_gray_img, c1, 2, int(255/dice_face), -1)
        cv2.circle(inv_gray_img, c2, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c3, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c4, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c5, 2, int(255/dice_face), -1) 
        cv2.circle(inv_gray_img, c6, 2, int(255/dice_face), -1) 


for row in range(1, int(height / dice_side_dimension) + 1):
    csv_row_values = []

    while x2 < width:
        cv2.rectangle(gray_img, (x1, y1), (x2, y2), (255,0,0), 1)
        cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 1)
        cv2.rectangle(inv_gray_img, (x1, y1), (x2, y2), (255,0,0), 1)

        # sub_image = img[y:y+h, x:x+w]
        x = x1
        y = y1
        w = x2-x1
        h = y2-y1
        dice_val = 1

        mean_val = cv2.mean(inv_gray_img[y:y+h, x:x+w])

        for ran in dice_faces:
            if int(mean_val[0]) in range(ran[0], ran[-1]):
                dice_val = dice_faces.index(ran) + 1
                cv2.putText(gray_img, str(dice_val), (int(x+dice_side_dimension/3),int(y-dice_side_dimension/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 0))
                cv2.putText(img, str(dice_val), (int(x+dice_side_dimension/3),int(y-dice_side_dimension/2)), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 0))

                draw_dice(x1, x2 , y1, y2, dice_val)

                break

        x1 += dice_side_dimension
        x2 += dice_side_dimension

        csv_row_values.append(str(dice_val).zfill(z_fill_len))
   
    x1 = 0
    x2 = dice_side_dimension

    y1 = dice_side_dimension * row
    y2 = dice_side_dimension * row + dice_side_dimension

    with open('output.csv', "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        
        writer.writerow([row, '-'] + csv_row_columns) 
        writer.writerow([row, '-'] + csv_row_values) 
        writer.writerow('')



cv2.imwrite('output-on-gray.png',gray_img)
cv2.imwrite('output-on-color.png',img)
cv2.imwrite('output-to-dices.png',inv_gray_img)

total_dice = (int(height / dice_side_dimension) + 1) * dice_per_row
print('you will need {} dices. {} dice per row with {} rows'.format(total_dice, dice_per_row, int(height / dice_side_dimension) + 1))

# cv2.waitKey(0)
# cv2.destroyAllWindows()