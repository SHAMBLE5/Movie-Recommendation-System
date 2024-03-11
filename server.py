from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def getvalue():
    number = request.form.to_dict()
    output=number['fname']
    file2write = open("filename",'w')
    file2write.write(output)
    file2write.write('\n')
    file2write.close()
    import main
    return render_template('mylocation.html',)


@app.route("/home")

@app.route('/')
def temp():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
