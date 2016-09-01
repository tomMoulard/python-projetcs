yolos = "yolo"
import sl4a
import time
droid = sl4a.Android()

def yolo(n):
    if n == 0: return None;
    print ( "yoloso", droid.startLocating () + droid.batteryGetStatus () )
    yolos = "yolo " + str(n) +' nb iter\n'+ str( time.strftime("%I %M %p on %A, %B %e, %Y, %H:%M:%S"))
    droid.makeToast(yolos)   
    #time.sleep(1)
    yolo(n-1)
    
    
a = int( input ( 'Choose a nb to loop here : ' ) )
yolo (a)