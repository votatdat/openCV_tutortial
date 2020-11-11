import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# def changeRes(width, height):
#     # Live vids only
#     capture.set(3, width)
#     capture.set(4, height)


def test_pic_resize():
    img = cv.imread('../Photos/cat.jpg')
    img_resized = rescaleFrame(img)

    cv.imshow('Cat', img)
    cv.imshow('Cat2', img_resized)

    cv.waitKey(0)


def test_vid_resize():
    capture = cv.VideoCapture('Videos/dog.mp4')

    while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame, scale=0.2)

        cv.imshow('Video', frame)
        cv.imshow('Video Resize', frame_resized)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()


test_pic_resize()
