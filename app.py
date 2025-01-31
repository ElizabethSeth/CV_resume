from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

resume_data = {
    "about_me": "Hello! My name is Elizabeth Seth. I am a Data Engineer, Data Analyst, and Data Scientist.",
    "education": "Education:\n- Bachelor's Degree in Law\n- Programming School 42\n- Master's Degree in Data Engineering from Microsoft Simplon.",
    "projects": "Projects:\n1. Portfolio Website\n2. Machine Learning Projects , Excel Automation, Data Engineering Projects ",
    "skills": "Skills:\n- Python, Kafka, Airflow, ClickHouse, PostgresSQL, MySQL Azure GCP Kubernetis\n- Stress resilience\n- Resourcefulness\n- Enthusiastic engagement in projects.",
    "internships": "Internships:\n- XYZ Corp, Software Intern.\nPernodRicard,DataScientist Aprentice 18 months.",
    "interests": "Interests:\n- Cybersecurity, AI, Open-Source Artificial Intelligence, Machine Learning, Data Engineering, Data Science, Data Analysis, Data Visualization, Data Warehousing, Data Mining, Data Modeling, Data Cleaning, Data Transformation, Data Integration, Data Quality, Data Governance, Data Security, Data Privacy, Data Ethics, Data Strategy, Data Architecture, Data Infrastructure, Data Pipelines, Data Lakes, Data Warehouses, Data Marts, Data Catalogs, Data Lineage, Data Profiling, Data Standardization, Data Enrichment, Data Harmonization, Data Classification, Data Categorization, Data Tagging, Data Annotation, Data Labeling, Data Augmentation, Data Aggregation, Data Sampling, Data Splitting, Data Partitioning, Data Sharding, Data Replication, Data Migration, Data Synchronization, Data Ingestion, Data Streaming, Data Processing, Data Transformation, Data Enrichment, Data Wrangling, Data Munging, Data Normalization, Data Standardization, Data Cleansing, Data Deduplication, Data Imputation, Data Interpolation, Data Smoothing, Data Aggregation, Data Summarization, Data Reduction, Data Compression, Data Decompression, Data Encryption, Data Masking, Data Obfuscation, Data Anonymization, Data Pseudonymization, Data De-identification, Data Tokenization, Data Minimization, Data Retention, Data Archiving, Data Purging, Data Deletion, Data Recovery, Data Backup, Data Restoration, Data Versioning, Data Lineage, Data Provenance, Data Quality, Data Profiling, Data Validation, Data Verification, Data Testing, Data Auditing, Data Monitoring, Data Governance, Data Stewardship, Data Custodianship, Data Ownership, Data Privacy, Data Ethics, Data Security, Data Protection, Data Compliance, Data Regulation, Data Legislation, Data Standards, Data Policies, Data Procedures, Data Guidelines, Data Best Practices, Data Management, Data Administration, Data Operations, Data Engineering, Data Science, Data Analysis, Data Visualization, Data Storytelling, Data Reporting, Data Dashboards, Data Insights, Data Intelligence, Data Wisdom, Data Knowledge, Data Information, Data Understanding, Data Awareness, Data Literacy, Data Fluency, Data Competency, Data Proficiency, Data Skills, Data Expertise, Data Experience, Data Wisdom, Data Intelligence, Data Knowledge, Data Awareness, Data Literacy, Data Fluency, Data Competency, Data Proficiency, Data Skills, Data Expertise, Data Experience, Data",
    "Languages" : "Languages:\n- English, French, Russian, Ukrainian, Spanish"
}


def display_help():
    help_data = {
        "about_me": "Displays information about me.",
        "education": "Shows my education details.",
        "projects": "Lists my projects.",
        "skills": "Lists my technical and soft skills.",
        "internships": "Shows my internship experience.",
        "interests": "Shows my personal interests.",
        "Languages" : "Shows my languages skills.",
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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    data = request.json
    user_command = data.get("command", "").strip()

    if user_command == "help":
        response = display_help()
    elif user_command == "clear":
        response = "" 
    else:
        response = resume_data.get(user_command, "Unknown command. Type 'help' to see available commands.")

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
