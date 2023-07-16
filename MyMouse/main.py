import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _,  frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    output2 = hand_detector.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    hands = output2.multi_hand_landmarks
    frame_h, frame_w, _ = frame.shape
    frame_height, frame_width, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks[474:478]:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x, y ), 3, (0, 255, 0))
            # print(x, y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x, y ), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.019:
            pyautogui.click()
            pyautogui.sleep(1)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            hlandmarks = hand.landmark
            for id, landmark in enumerate(hlandmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)

    cv2.imshow('AI Mouse', frame)
    cv2.waitKey(1)