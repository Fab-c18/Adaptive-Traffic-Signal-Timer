import cv2
import glob
from vehicle_detector import VehicleDetector

def count(img_add):
    # Load Veichle Detector
    vd = VehicleDetector()
    # Load images from a folder
    img=cv2.imread(img_add)
    # Loop through all the images
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    if(vehicle_count<5):
        return 0
    time=15
    if(vehicle_count<=20):
        time+=int(1.3*vehicle_count)-10
    else :
        if(vehicle_count>20 and vehicle_count<35):
            time+=int(vehicle_count*1.43)-10
        else:
            time=150
    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
        cv2.putText(img, "Timer: " + str(time),(20,110),0,2,(0,255,255),3)
    cv2.imwrite(img_add,img)
    cv2.destroyAllWindows()    
    return time
    #cv2.imshow("Cars", img)
    #cv2.waitKey(0)
