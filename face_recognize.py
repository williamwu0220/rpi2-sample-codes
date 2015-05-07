#!/usr/bin/python

def face_recognize(filename):
    from SimpleCV import Image, Display, DrawingLayer
    
    image = Image(filename)
    faces = image.findHaarFeatures('face.xml')
    if faces:
        for face in faces:
            face_layer = DrawingLayer((image.width, image.height))
            face_box = face_layer.centeredRectangle(face.coordinates(), (face.width(), face.height()))
            image.addDrawingLayer(face_layer)
            image.applyLayers()
        image.save(filename)
        print('偵測到 {} 張人臉'.format(len(faces)))
    else:
        print('沒有偵測到人臉')

def take_picture(filename):
    import time
    import picamera

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(filename)
        camera.stop_preview()
    

def main():
    from datetime import datetime

    filename = '{}.jpg'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    take_picture(filename)
    face_recognize(filename)

if __name__ == '__main__':
    main()
