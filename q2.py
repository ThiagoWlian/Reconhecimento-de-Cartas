import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    image = frame
    new_image = image.copy()
 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)

    inverted_binary = ~binary

    contornos, _ = cv2.findContours(inverted_binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cartasVemelhas = 0
    cartasPretas = 0

    i = 0
    for c in contornos:
        x, y, w, h = cv2.boundingRect(c)
        crop_img = image[y+20:y+100,x+15:x+60]
        if cv2.countNonZero(cv2.inRange(crop_img, (0, 0, 0), (0, 0,255))) == 0:
            cv2.rectangle(image,(x,y), (x+w,y+h), (0,128,0), 5)
            cartasVemelhas += 1
            font = cv2.FONT_HERSHEY_SIMPLEX
        else:
            cartasPretas += 1
        i += 1

    cv2.putText(image, "Cartas Vermelhas: " + str(cartasVemelhas), (1100,100), font,1,(200,50,0),2,cv2.LINE_AA)
    cv2.putText(image, "Cartas Pretas: " + str(cartasPretas), (1100,200), font,1,(200,50,0),2,cv2.LINE_AA)

    i = 0
    for c in contornos:
        x, y, w, h = cv2.boundingRect(c)
        crop_img = image[y+20:y+100,x+15:x+60]
        font = cv2.FONT_HERSHEY_SIMPLEX
        if cv2.countNonZero(cv2.inRange(crop_img, (0, 0, 0), (0, 0,255))) == 0:
            cv2.rectangle(image,(x,y), (x+w,y+h), (0,0,255), 5)
        else:
            cv2.rectangle(image,(x,y), (x+w,y+h), (0,0,0), 5)
        i += 1
    
    cv2.imshow("Feed2", frame)


    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()