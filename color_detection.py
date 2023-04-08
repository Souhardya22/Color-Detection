
import cv2
import pandas as pd

# img_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\pic1.jpg'
# img_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\pic2.jpg'
# img_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\pic3.jpg'
# img_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\colorpic.jpg'
img_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\Abstract Painting by Adrika.jpg'
csv_path = r'C:\Users\KIIT\Documents\3rd Year\6th SEM\Data Analytics\Color detection\colors.csv'

# reading csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)
print(df.head())
print(f'The number of columns and rows are : {df.shape}')
# reading image
img = cv2.imread(img_path)
img = cv2.resize(img, (800, 600))

# declaring global variables
clicked = False
r = g = b = x_pos = y_pos = 0


# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    global cname
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']

    return cname


# function to get x,y coordinates of mouse double click
def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


# creating window
cv2.namedWindow('Group-3 DA MINOR PROJECT')
cv2.setMouseCallback('Group-3 DA MINOR PROJECT', draw_function)

while True:
    cv2.imshow('Group-3 DA MINOR PROJECT', img)
    if clicked:
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (630, 60), (b, g, r), -1)

        # Creating text string to display( Color name and RGB values )
        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (40, 40), 1, 1.3, (255, 255, 255), 1, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (40, 40), 1, 1.3, (0, 0, 0), 1, cv2.LINE_AA)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
