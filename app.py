from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

subjects_by_semester = {
    1: [
        {"name": "Anatomie-physiologie (1)", "coeff": 2.5, "credits": 5, "isAnatomie": True},
        # ... [ALL OTHER SUBJECTS FROM ORIGINAL JS CODE] ...
    ],
    2: [
        # ... [SEMESTER 2 SUBJECTS] ...
    ],
    3: [
        # ... [SEMESTER 3 SUBJECTS] ...
    ],
    4: [
        # ... [SEMESTER 4 SUBJECTS] ...
    ],
    5: [
        # ... [SEMESTER 5 SUBJECTS] ...
    ],
    6: [
        # ... [SEMESTER 6 SUBJECTS] ...
    ]
}

def calculate_average(semester, input_data):
    subjects = subjects_by_semester.get(int(semester), [])
    total = 0.0
    total_coeff = 0.0
    total_credits = 0
    earned_credits = 0
    warnings = []
    
    no_control_subjects = {
        "Anglais médicale (2)", "Philosophie des sciences", "2CN (2)",
        "Sociologie de la santé", "Technique de communication (2)",
        "Système de santé", "Economie de la santé", "Méthodologie de la recherche (1)",
        "Anglais médical (4)", "Anglais médicale (1)", "Droit de patient", "2CN (1)",
        "Psychologie du développement social", "Technique de communication (1)",
        "Santé et sécurité au travail", "Soins infirmiers et handicap",
        "Soins infirmiers et santé de l'adolescent", "Recherche documentaire",
        "Anglais médicale (3)", "Qualité et sécurité des soins",
        "Méthodologie de la recherche (2)", "Statistiques"
    }

    for idx, subject in enumerate(subjects):
        subj_input = input_data.get(str(idx), {})
        raw_avg = 0.0
        
        if subject.get("isAnatomie"):
            averages = []
            for i in range(3):
                ds = float(subj_input.get(f"anat_ds_{i}", 0))
                exam = float(subj_input.get(f"anat_exam_{i}", 0))
                avg = (ds * 0.3) + (exam * 0.7)
                averages.append(avg)
            raw_avg = sum(averages) / len(averages) if averages else 0
        elif subject.get("singleNote"):
            raw_avg = float(subj_input.get("note", 0))
        else:
            ds = float(subj_input.get("ds", 0))
            exam = float(subj_input.get("exam", 0))
            raw_avg = (ds * 0.3) + (exam * 0.7)

        total_credits += subject["credits"]
        if raw_avg >= 10:
            earned_credits += subject["credits"]

        threshold = subject.get("controlThreshold", 6)
        if (not subject.get("noControl") and 
            subject["name"] not in no_control_subjects and 
            raw_avg < threshold):
            warnings.append(f"Contrôle requis dans {subject['name']} (Note: {raw_avg:.2f})")

        total += raw_avg * subject["coeff"]
        total_coeff += subject["coeff"]

    final_avg = total / total_coeff if total_coeff != 0 else 0
    return {
        "average": final_avg,
        "total_credits": total_credits,
        "earned_credits": earned_credits,
        "warnings": warnings
    }

@app.route("/")
def home():
    return render_template("index.html", subjects_by_semester=subjects_by_semester)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    semester = data.get("semester")
    input_data = data.get("input_data")
    result = calculate_average(semester, input_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)