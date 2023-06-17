import cv2
import numpy as np

def track_ball(frame):
    height, width, _ = frame.shape
    half_height = height // 2

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB

    low = 200
    lower_color = np.array([low, low, low])  # Adjust these values based on your desired color range (in RGB format)
    upper_color = np.array([255, 255, 255])  # Adjust these values based on your desired color range (in RGB format)

    mask = cv2.inRange(rgb_frame, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        circularity = 4 * np.pi * (area / (perimeter * perimeter))

        if circularity > 0.75:  # Adjust this value based on the circularity threshold
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius) + 10  # Increase the radius to make the circle larger

            if center[1] > half_height:  # Only consider circles in the bottom half
                cv2.circle(frame, center, radius, (0, 255, 255), 2)  # Draw a red circle
                certainty = int(circularity * 100)  # Calculate the degree of certainty
                text = f"Ball ({certainty}%)"
                cv2.putText(frame, text, (center[0] - 50, center[1] - radius - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return frame
