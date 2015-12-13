from bottle import route, run, static_file, template, url

@route("/")
def index():
    return template("templates/index.html", url=url)

@route('/static/<path:path>')
def static(path):
    return static_file(path, root="static")

run(host='localhost', port=8080, debug=True)