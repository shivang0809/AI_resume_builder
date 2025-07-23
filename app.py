from flask import Flask, render_template, request
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    job_role = request.form['job_role']
    experience = request.form['experience']
    skills = request.form['skills']
    goal = request.form['goal']
    job_desc = request.form['job_description']

    summary_prompt = f"""
    Write a professional resume summary for {name}, a {job_role} with {experience} years of experience. 
    Their skills are: {skills}. Their career goal is: {goal}.
    """
    cover_letter_prompt = f"""
    Write a personalized cover letter for a {job_role} role. Candidate: {name}, with {experience} years of experience. 
    Skills: {skills}. Career goal: {goal}. Target job description: {job_desc}.
    """

    summary = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": summary_prompt}]
    )['choices'][0]['message']['content']

    cover_letter = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": cover_letter_prompt}]
    )['choices'][0]['message']['content']

    return render_template('result.html', summary=summary, cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True)