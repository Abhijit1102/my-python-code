from flask import Flask, render_template
app = Flask(__name__)

post=[
    {
        "author": "Abhijit Rajlkumar",
        "title":"Blog Post 1",
        "content":"First post conent",
        "dated_posted": "April 14, 2019"
    },

    {
        "author": "Chunu",
        "title":"Blog Post 2",
        "content":"2nd post conent",
        "dated_posted": "April 202, 2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = post)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ =="___main__":
    app.run(debug=True)    
