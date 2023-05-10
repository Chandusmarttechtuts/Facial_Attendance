import cv2
import os
from datetime import datetime
import csv
import face_recognition
def checking():
    known_encodings = []
    known_names = []
    for filename in os.listdir('faces'):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            name = os.path.splitext(filename)[0]
            face = face_recognition.load_image_file(os.path.join('faces', filename))
            encoding = face_recognition.face_encodings(face)
            if len(encoding) > 0:
                known_encodings.append(encoding[0])
                known_names.append(name)
    #initialize webcam
    cap = cv2.VideoCapture(0)
    cur_date = datetime.now().strftime("%Y-%m-%d")
    f = open(cur_date + '.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(["name of student", 'attendence'])
    cnames = []
    while True:
        ret, frame = cap.read()
        locations = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, locations)
        for encoding, location in zip(encodings, locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]
                cv2.putText(frame, f'Match found: {name}', (location[3], location[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 255, 0), 2)
                if name not in cnames:
                    f = open(cur_date + '.csv', 'a', newline='')
                    writer = csv.writer(f)
                    writer.writerow([name, 'present'])
                cnames.append(name)
            else:
                cv2.putText(frame, 'Match not found', (location[3], location[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 0, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()