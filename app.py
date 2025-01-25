from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Данные для команд
resume_data = {
    "about_me": "Hello! My name is [Your Name]. I am a Software Developer.",
    "education": "Education:\n- University of Example, 2024.",
    "projects": "Projects:\n1. Portfolio Website\n2. Machine Learning Project.",
    "skills": "Skills:\n- Python, JavaScript, Flask, Problem Solving.",
    "internships": "Internships:\n- XYZ Corp, Software Intern.",
    "interests": "Interests:\n- Cybersecurity, AI, Open-Source.",
}

# Функция для генерации HTML-таблицы с командами
def display_help():
    help_data = {
        "about_me": "Displays information about me.",
        "education": "Shows my education details.",
        "projects": "Lists my projects.",
        "skills": "Lists my technical and soft skills.",
        "internships": "Shows my internship experience.",
        "interests": "Shows my personal interests.",
        "clear": "Clears the terminal screen.",
        "help": "Displays this help message.",
        "exit": "Exits the terminal."
    }

    html_output = """
    <div style=\"color: cyan; font-weight: bold;\">Type the following commands to explore my resume:</div>
    <table style=\"width: 100%; color: #0f0; font-family: Courier, monospace; border-spacing: 10px;\">
        <tr>
            <th style=\"color: yellow; text-align: left;\">Command</th>
            <th style=\"color: magenta; text-align: left;\">Description</th>
        </tr>
    """

    for command, description in help_data.items():
        html_output += f"""
        <tr>
            <td style=\"color: lightgreen;\">{command}</td>
            <td style=\"color: lightblue;\">{description}</td>
        </tr>
        """

    html_output += "</table>"
    return html_output

# Маршрут для главной страницы
@app.route("/")
def index():
    return render_template("index.html")

# Маршрут для обработки команд
@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_command = data.get("command", "").strip()

    if user_command == "help":
        response = display_help()
    elif user_command == "clear":
        response = ""  # Очистка экрана на клиенте
    else:
        response = resume_data.get(user_command, "Unknown command. Type 'help' to see available commands.")

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
