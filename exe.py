from main import caturing_images
from check import checking
count =0
print("       ---Menu---       \nenter c for capturing new faces\nenter q for quit\nenter any other keys for attendence taking")
while True:
    key =  input()
    if key=="c":
        count=caturing_images(count)
    elif key == "q":
            print("closing")
            break

    else:
        checking()



