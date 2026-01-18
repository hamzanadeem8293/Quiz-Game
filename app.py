from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'quiz_secret_key'

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "HTML", "JavaScript", "All"],
        "answer": "All"
    },
    {
        "question": "What does ICT stand for?",
        "options": ["Information Communication Technology",
                    "International Communication Tool",
                    "Information Control Technique",
                    "None"],
        "answer": "Information Communication Technology"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "12"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is mutable in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    },
    {
        "question": "Which HTML tag is used to create a hyperlink?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "answer": "<a>"
    },
    {
        "question": "Which protocol is used to send emails?",
        "options": ["HTTP", "FTP", "SMTP", "TCP"],
        "answer": "SMTP"
    },
    {
        "question": "What does CSS stand for?",
        "options": [
            "Computer Style Sheets",
            "Cascading Style Sheets",
            "Creative Style System",
            "Colorful Style Sheets"
        ],
        "answer": "Cascading Style Sheets"
    },
    {
        "question": "Which company developed Python?",
        "options": ["Google", "Microsoft", "Facebook", "Python Software Foundation"],
        "answer": "Python Software Foundation"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "/*", "#", "<!--"],
        "answer": "#"
    },
    {
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["while", "for", "do-while", "loop"],
        "answer": "for"
    },
    {
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Advanced Program Integration",
            "Application Process Interface",
            "Applied Programming Internet"
        ],
        "answer": "Application Programming Interface"
    },
    {
        "question": "Which database is a NoSQL database?",
        "options": ["MySQL", "PostgreSQL", "MongoDB", "Oracle"],
        "answer": "MongoDB"
    },
    {
        "question": "What does ICT stand for?",
        "options": [
            "Information Communication Technology",
            "Internet Control Technique",
            "Information Computer Tool",
            "International Communication Type"
        ],
        "answer": "Information Communication Technology"
    },
    {
        "question": "Which HTTP method is used to submit form data?",
        "options": ["GET", "POST", "PUT", "DELETE"],
        "answer": "POST"
    },
    {
        "question": "Which Python library is used for web development?",
        "options": ["NumPy", "Flask", "Pandas", "Matplotlib"],
        "answer": "Flask"
    },
    {
        "question": "Which operator is used for equality check in Python?",
        "options": ["=", "==", "!=", "<>"],
        "answer": "=="
    },
    {
        "question": "Which device is used to connect different networks?",
        "options": ["Switch", "Hub", "Router", "Repeater"],
        "answer": "Router"
    },
    {
        "question": "Which software model follows sequential steps?",
        "options": ["Agile", "Spiral", "Waterfall", "RAD"],
        "answer": "Waterfall"
    },
    {
        "question": "What is the default port for HTTP?",
        "options": ["21", "25", "80", "443"],
        "answer": "80"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },
    {
        "question": "Which Python framework is micro-framework?",
        "options": ["Django", "Flask", "FastAPI", "Pyramid"],
        "answer": "Flask"
    },
    {
        "question": "Which cloud service model provides infrastructure?",
        "options": ["SaaS", "PaaS", "IaaS", "FaaS"],
        "answer": "IaaS"
    },
    {
        "question": "Which algorithm is used for classification?",
        "options": ["Linear Regression", "K-Means", "Decision Tree", "Apriori"],
        "answer": "Decision Tree"
    },
    {
        "question": "Which tag is used to display images in HTML?",
        "options": ["<img>", "<image>", "<pic>", "<src>"],
        "answer": "<img>"
    },
    {
        "question": "What does URL stand for?",
        "options": [
            "Uniform Resource Locator",
            "Universal Resource Link",
            "Uniform Reference Link",
            "Universal Reference Locator"
        ],
        "answer": "Uniform Resource Locator"
    },
    {
        "question": "Which sorting algorithm has O(n log n) complexity?",
        "options": ["Bubble Sort", "Selection Sort", "Merge Sort", "Insertion Sort"],
        "answer": "Merge Sort"
    },
    {
        "question": "Which language is used for styling web pages?",
        "options": ["HTML", "JavaScript", "CSS", "Python"],
        "answer": "CSS"
    },
    {
        "question": "Which command is used to install Flask?",
        "options": ["install flask", "pip install flask", "python flask", "setup flask"],
        "answer": "pip install flask"
    },
    {
        "question": "Which OSI layer handles routing?",
        "options": ["Physical", "Data Link", "Network", "Transport"],
        "answer": "Network"
    },
    {
        "question": "Which protocol is used for secure communication?",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "Which data structure does FIFO follow?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },
    {
        "question": "Which function is used to get input in Python?",
        "options": ["get()", "input()", "scan()", "read()"],
        "answer": "input()"
    },
    {
        "question": "Which Python keyword is used for exception handling?",
        "options": ["catch", "try", "handle", "error"],
        "answer": "try"
    },
    {
        "question": "Which SQL command is used to retrieve data?",
        "options": ["INSERT", "DELETE", "SELECT", "UPDATE"],
        "answer": "SELECT"
    },
    {
        "question": "Which HTML tag is used to create a table?",
        "options": ["<table>", "<tab>", "<tr>", "<td>"],
        "answer": "<table>"
    },
    {
        "question": "Which programming paradigm does Python support?",
        "options": ["Procedural", "Object-Oriented", "Functional", "All"],
        "answer": "All"
    },
    {
        "question": "Which device forwards data based on MAC address?",
        "options": ["Router", "Switch", "Hub", "Gateway"],
        "answer": "Switch"
    },
    {
        "question": "Which version control system is widely used?",
        "options": ["SVN", "Git", "Mercurial", "CVS"],
        "answer": "Git"
    },
    {
        "question": "Which Python function returns length?",
        "options": ["count()", "size()", "len()", "length()"],
        "answer": "len()"
    },
    {
        "question": "Which HTTP status code means success?",
        "options": ["404", "500", "200", "301"],
        "answer": "200"
    },
    {
        "question": "Which HTML tag is used for the largest heading?",
        "options": ["<h6>", "<h4>", "<h2>", "<h1>"],
        "answer": "<h1>"
    },
    {
        "question": "Which AI field deals with learning from data?",
        "options": ["Robotics", "Machine Learning", "Expert Systems", "NLP"],
        "answer": "Machine Learning"
    },
    {
        "question": "Which Python library is used for numerical computation?",
        "options": ["Flask", "NumPy", "Django", "Seaborn"],
        "answer": "NumPy"
    },
    {
        "question": "Which network topology uses a central hub?",
        "options": ["Bus", "Ring", "Star", "Mesh"],
        "answer": "Star"
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['qno'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['POST', 'GET'])
def quiz():
    qno = session.get('qno', 0)

    if request.method == 'POST':
        selected = request.form.get('option')
        correct = questions[qno-1]['answer']
        if selected == correct:
            session['score'] += 1

    if qno < len(questions):
        question = questions[qno]
        session['qno'] = qno + 1
        return render_template('quiz.html', q=question, qno=qno+1)
    else:
        return redirect('/result')

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
if 'username' not in session:
    session['username'] = request.args.get('username')
