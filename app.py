from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    topic = request.form.get("topic")
    subject = request.form.get("subject")
    difficulty = request.form.get("difficulty")
    output_type = request.form.get("type").lower()

    # ---------------- QUIZ ----------------
    if output_type == "quiz":

        result = f"""
<h1>{topic.title()} Quiz</h1>

<p><b>Subject:</b> {subject} | <b>Difficulty:</b> {difficulty}</p>

<div class="quiz">

<div class="question">
<h3>1. What best describes {topic}?</h3>
<ul>
<li>A) A process related to energy conversion</li>
<li>B) A chemical compound</li>
<li>C) A historical theory</li>
<li>D) None of the above</li>
</ul>
</div>

<div class="question">
<h3>2. Why is {topic} important in {subject}?</h3>
<ul>
<li>A) It explains fundamental scientific processes</li>
<li>B) It helps understand natural phenomena</li>
<li>C) It supports development of scientific theories</li>
<li>D) All of the above</li>
</ul>
</div>

<div class="question">
<h3>3. Which factor most directly affects {topic}?</h3>
<ul>
<li>A) Environmental conditions</li>
<li>B) Energy availability</li>
<li>C) Biological structures</li>
<li>D) All of the above</li>
</ul>
</div>

<div class="question">
<h3>4. Which field studies {topic} in detail?</h3>
<ul>
<li>A) Biology</li>
<li>B) Physics</li>
<li>C) Chemistry</li>
<li>D) Environmental Science</li>
</ul>
</div>

<div class="question">
<h3>5. Which statement about {topic} is correct?</h3>
<ul>
<li>A) It plays a major role in ecosystems</li>
<li>B) It is essential for life processes</li>
<li>C) It contributes to energy transfer</li>
<li>D) All of the above</li>
</ul>
</div>

<div class="answers">
<h3>Answer Key</h3>
<p>1 → A</p>
<p>2 → D</p>
<p>3 → D</p>
<p>4 → A</p>
<p>5 → D</p>
</div>

</div>
"""

    # ---------------- STUDY NOTES ----------------
    elif output_type == "study notes":

        result = f"""
<h1>{topic.title()} – Detailed Study Notes</h1>

<p>
<b>{topic.title()}</b> is an important concept in <b>{subject}</b>.
These notes are designed for <b>{difficulty}</b> learners to understand the topic in depth.
</p>

<h2>1. Introduction</h2>

<p>
{topic.title()} refers to a process or concept that plays a significant role in understanding
various natural or scientific phenomena. It helps explain how systems function and interact
with each other in the field of {subject}.
</p>

<h2>2. Key Concepts</h2>

<ul>
<li>Definition and meaning of {topic}</li>
<li>Fundamental principles related to {topic}</li>
<li>Scientific mechanisms behind the process</li>
<li>Importance in real-world applications</li>
</ul>

<h2>3. How It Works</h2>

<p>
The mechanism behind {topic} involves several stages. These stages include energy interaction,
chemical or physical transformations, and production of useful outputs that support larger systems.
</p>

<ul>
<li>Stage 1: Initial interaction with environmental factors</li>
<li>Stage 2: Internal transformation processes</li>
<li>Stage 3: Final output or result</li>
</ul>

<h2>4. Importance of {topic}</h2>

<ul>
<li>Helps explain important natural processes</li>
<li>Provides insights into how living or physical systems operate</li>
<li>Supports scientific research and innovation</li>
<li>Contributes to sustainability and ecosystem balance</li>
</ul>

<h2>5. Real-World Applications</h2>

<ul>
<li>Used in scientific research</li>
<li>Important for environmental studies</li>
<li>Helps develop technological and biological solutions</li>
<li>Supports understanding of ecological systems</li>
</ul>

<div class="info-box">
Understanding <b>{topic}</b> helps students build strong foundations in <b>{subject}</b>.
</div>
"""

    # ---------------- SUMMARY ----------------
    else:

        result = f"""
<h1>{topic.title()} – Summary</h1>

<p>
{topic.title()} is a fundamental concept in <b>{subject}</b>.
It plays a crucial role in explaining how systems interact and function.
</p>

<h2>Main Points</h2>

<ul>
<li>Defines how important processes operate</li>
<li>Explains relationships between different components</li>
<li>Helps understand scientific principles</li>
<li>Provides real-world applications</li>
</ul>

<p>
For <b>{difficulty}</b> learners, understanding {topic} is essential for building
a strong academic foundation and exploring advanced topics in {subject}.
</p>
"""

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)