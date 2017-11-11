from flask import Flask, render_template

app= Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html', key="AIzaSyCLlGnDH8lP4MOvUgo16vxK149VX0x1PyQ")

if __name__ == '__main__':
    app.run(debug=True)
