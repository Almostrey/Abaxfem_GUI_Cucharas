import cv2                              # Para graficar sobre la termograf√≠a
def visgraf(name,Image):
    cv2.imshow(name, Image)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

