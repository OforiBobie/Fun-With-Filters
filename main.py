import cv2
image=cv2.imread('image.png')
print("R-Red tint")
print("G-Green tint")
print("B-Blue tint")
print("i-increase Red")
print("d-decrease green")
print("q-quit")
cv2.imshow("Original image",image)
while True:
    key=cv2.waitKey(0) &0xFF
    filtered_image=image.copy()
    #red tint
    if key==ord("r"):
        filtered_image[:,:,0]=0
        filtered_image[:,:,1]=0
    #blue tint
    elif key==ord("b"):
        filtered_image[:,:,1]=0
        filtered_image[:,:,2]=0
    #green tint
    if key==ord("g"):
        filtered_image[:,:,0]=0
        filtered_image[:,:,2]=0
    #increase red intensity
    elif key==ord("i"):
        filtered_image[:,:,2]=cv2.add(filtered_image[:,:,2],10)
    #decrease blue intensity
    elif key==ord("d"):
        filtered_image[:,:,0]=cv2.subtract(filtered_image[:,:,0],10)
    elif key==ord("o"):
        filtered_image.copy()
    elif key==ord("q"):
        break
    cv2.imshow("filtered_image",filtered_image)
cv2.destroyAllWindows()