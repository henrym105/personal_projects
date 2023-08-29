import cv2
from preprocessing import preprocess_frame
from visualization import display_frame
from ball_tracking import track_ball, initial_ball_coordinates

def main():
    # video_path = '/Users/Henry/Desktop/personal_projects/cv_testing_space/Golf Shot Tracer/Videos/Collin Morikawas PURE Iron Swing.mp4'
    video_path = r'Videos/Tiger Woods cropped.mp4'
    cap = cv2.VideoCapture(video_path)

    # ret, frame = cap.read()
    # initial_position = initial_ball_coordinates(frame)
    # print(initial_position)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret: 
            break

        resized_frame = preprocess_frame(frame)
        tracked_frame = track_ball(resized_frame)
        display_frame(tracked_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

