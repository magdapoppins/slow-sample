import json

from PIL import Image
from werkzeug.debug import DebuggedApplication
from werkzeug.wrappers import Request, Response

from tf_mnist.predict import Predictor

predictor = None


def read_image_from_wsgi_request(environ):
    request = Request(environ)
    if not request.files:
        return None
    file_key = list(request.files.keys())[0]
    file = request.files.get(file_key)
    img = Image.open(file.stream)
    img.load()
    return img


def predict(environ, start_response):
    raise Exception
    #return True


predict = DebuggedApplication(predict)

if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 3000, predict)
