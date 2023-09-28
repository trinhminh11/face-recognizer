import cv2
import os

class FaceDetector:
	process_current_frame = True
	
	faceDetect = cv2.CascadeClassifier(
		cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
	)
	
	def detect_face(self, frame):
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		face = self.faceDetect.detectMultiScale(
			gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
		)

		for x, y, w, h in face:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

	def run(self):

		cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

		if not cam.isOpened():
			print("Video Source not found...")
			exit()

		# counter = 0

		while True:
			# counter += 1 
			ret, frame = cam.read()

			if not ret:
				print("failed to grab frame")
				break
			
			if self.process_current_frame:
				
				self.detect_face(frame)
			
			# self.process_current_frame = not self.process_current_frame

			cv2.imshow("test", frame)

			# stored last frame into folder image
			cv2.imwrite("image/current.jpg", frame)

			key = cv2.waitKey(1)

			# if key = escape or "q" then stop
			if key%256 == 27 or key == ord("q"):
				print("Escape app")
				break
		
		
		os.remove("image/current.jpg")
		
		cam.release()
		cv2.destroyAllWindows()


def main():

	faceDetect = FaceDetector()

	faceDetect.run()

if __name__ == "__main__":
	main()