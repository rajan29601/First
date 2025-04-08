


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <html>
        <head><title>DevOps Flask</title></head>
        <body>
            <h1>Hello from DevOps!</h1>
            <img src="https://images.pexels.com/photos/998653/pexels-photo-998653.jpeg?cs=srgb&dl=adventure-arid-bushes-998653.jpg&fm=jpg" 
                 alt="My Image" width="600">
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


