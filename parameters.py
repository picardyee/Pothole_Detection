# train

--img 640
--batch 32
--epochs 500
--data C:\Users\User\PycharmProjects\Detection\Pothole\data.yaml
--cfg C:\Users\User\PycharmProjects\Detection\yolov5\models\yolov5s.yaml
--weights ''
--name pothole_result

# validation

--img 640
--iou 0.65
--half
--data C:\Users\User\PycharmProjects\Detection\Pothole\data.yaml
--weights C:\Users\User\PycharmProjects\Detection\yolov5\runs\train\pothole_results\weights\best.pt

# inference

--img 640
--conf 0.4
--half
--source C:\Users\User\PycharmProjects\Detection\Pothole\test\images
--weights C:\Users\User\PycharmProjects\Detection\yolov5\runs\train\pothole_results\weights\best.pt

