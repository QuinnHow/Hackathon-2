from flask import Flask, render_template

app = Flask(__name__)

dataSci = 0
cyberSec = 0
gameDesign = 0
webDev = 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/page0")
def page0():
    return render_template('page0.html')

@app.route("/page0-3")
def page0x3():
    return render_template('page0-3.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page1-4")
def page1x4():
    global gameDesign
    gameDesign += 1
    return render_template('page1-4.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page2-1")
def page2x1():
    global gameDesign
    gameDesign += 1
    return render_template('page2-1.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')

@app.route("/page4")
def page4():
    return render_template('page4.html')

@app.route("/page5")
def page5():
    return render_template('page5.html')

@app.route("/page6")
def page6():
    return render_template('page6.html')

@app.route("/page7")
def page7():
    return render_template('page7.html')

@app.route("/page8")
def page8():
    return render_template('page8.html')

@app.route("/ending1")
def ending1():
    dict = {'dataSci': dataSci, 'cyberSec': cyberSec, 'gameDesign': gameDesign, 'webDev': webDev}
    choice = max(dict, key=dict.get)
    if choice == "dataSci":
        choice_title = "Data Scientist"
        choice_desc = "You have a very logical, though out way of thinking. This is an asset to the field of Data Science. Data Scientists are the ones behind every stat, every piece of information you've used. They analyse patterns in the way people interact with the world around them, and produce valuable insights to the general public."
    elif choice == "cyberSec":
        pass
    elif choice == "gameDesign":
        choice_title = "Game Developer"
        choice_desc = "You are creative a really creative person, and love to push the boundaries of what can be created with computers. Game developers are some of the most beloved programmers out there, responsible for every video game we play. Whether you're interested in the beautiful 2D art of an indie platform game, or the technical 3D animation accompanying a game of difficult decisions, there are no shortage of spaces for talented artists."
    elif choice == "webDev":
        choice_title = "Web Developer"
        choice_desc = "You are creative, but like to apply that creativity to something that will benefit anyone who uses your program. \n If you're looking for a creative outlet, that will reach even the most tech-illiterate people, look no further.  Web designers are the most obvious workers to those who have no knowledge on the industry. The pages they create, are seen by hundreds, thousands, millions of people, and are heavily relied on by every single business."

    return render_template('ending1.html', value=choice_title, value2=choice_desc)

if __name__ == '__main__':
    app.run(debug=True)