from werkzeug.debug import DebuggedApplication
from werkzeug.wrappers import Request, Response

predictor = None

def predict(environ, start_response):
    return Response('no file uploaded', 400)(environ, start_response)


predict = DebuggedApplication(predict)

if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 3000, predict)
