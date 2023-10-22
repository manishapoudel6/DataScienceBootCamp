import cv2
import numpy as np
import random


image_paths = ['IMG_5993.JPG', 'IMG_5994.WEBP', 'IMG_5995.PNG', 'IMG_5996.JPG']


circle_color = (0, 0, 255) 
rectangle_color = (0, 255, 0)  
line_color = (255, 0, 0)  
text_color = (0, 0, 255)  


height, width = 400, 600  

for image_path in image_paths:
    image = cv2.imread(image_path)

    center = (random.randint(0, width), random.randint(0, height))
    radius = random.randint(20, 100)
    cv2.circle(image, center, radius, circle_color, -1)  # -1 for a filled circle

    start_point = (random.randint(0, width), random.randint(0, height))
    end_point = (start_point[0] + random.randint(50, 200), start_point[1] + random.randint(50, 200))
    cv2.rectangle(image, start_point, end_point, rectangle_color, -1)  # -1 for a filled rectangle

    line_start = (random.randint(0, width), random.randint(0, height))
    line_end = (random.randint(0, width), random.randint(0, height))
    cv2.line(image, line_start, line_end, line_color, 3)  # 3 is the line thickness

    text = "Hi, Cats!"
    text_position = (random.randint(0, width - 150), random.randint(0, height - 10))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    cv2.putText(image, text, text_position, font, font_scale, text_color, 2, cv2.LINE_AA)

    # Save the modified image with a unique filename
    output_path = f'output_{image_path}'
    cv2.imwrite(output_path, image)

for image_path in image_paths:
    modified_image = cv2.imread(f'output_{image_path}')
    cv2.imshow(f'Modified Image: {image_path}', modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

