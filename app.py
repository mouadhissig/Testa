from flask import Flask, render_template, request, jsonify

@app.route("/")
def home():
    return render_template("index.html", subjects_by_semester=subjects_by_semester)  # <-- Add this parameter


app = Flask(__name__)

# Complete subjects data
subjects_by_semester = {
    1: [
        {"name": "Anatomie-physiologie (1)", "coeff": 2.5, "credits": 5, "isAnatomie": True},
        {"name": "Déontologie-Ethique", "coeff": 1, "credits": 2},
        {"name": "Soins dans la Communauté (1)", "coeff": 1, "credits": 2},
        {"name": "Démarche de soins", "coeff": 1.5, "credits": 3},
        {"name": "Microbiologie, parasitologie et immunité", "coeff": 1, "credits": 2},
        {"name": "Introduction à la Discipline infirmière", "coeff": 1.5, "credits": 3},
        {"name": "Psychologie du développement social", "coeff": 1, "credits": 2},
        {"name": "Techniques infirmières 1", "coeff": 1.5, "credits": 3, "singleNote": True, "controlThreshold": 8},
        {"name": "Anglais médicale (1)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Droit de patient", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "2CN (1)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Technique de communication (1)", "coeff": 1, "credits": 2, "noControl": True}
    ],
    2: [
        {"name": "Philosophie des sciences", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Anatomie-physiologie (2)", "coeff": 1.5, "credits": 3, "isAnatomie": True},
        {"name": "Pharmacologie (1)", "coeff": 1, "credits": 2},
        {"name": "Soins à la mére et au nouveau né", "coeff": 1, "credits": 2},
        {"name": "Hygiène et environnement", "coeff": 1, "credits": 2},
        {"name": "Relation d'aide", "coeff": 1, "credits": 2},
        {"name": "Techniques infirmières 2", "coeff": 1, "credits": 2, "singleNote": True, "controlThreshold": 8},
        {"name": "Biologie Clinique", "coeff": 0.5, "credits": 1},
        {"name": "Sociologie de la santé", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Techniques de communication (2)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "2CN (2)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Anglais médicale (2)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Initiation aux premiers secours", "coeff": 1, "credits": 2, "singleNote": True, "controlThreshold": 8},
        {"name": "Stage hospitalier en médecine-chirurgie", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10}
    ],
    3: [
        {"name": "Stage hospitalier en pédiatrie", "coeff": 1.5, "credits": 3, "singleNote": True, "controlThreshold": 10},
        {"name": "Soins infirmiers en pédiatrie", "coeff": 1.5, "credits": 3, "isSpecialCase": True},
        {"name": "Soins infirmiers en cardiologie", "coeff": 1, "credits": 2, "isSpecialCase": True, "controlThreshold": 10},
        {"name": "Soins infirmiers en pneumologie", "coeff": 1, "credits": 2, "isSpecialCase": True},
        {"name": "Pharmacologie (2)", "coeff": 1, "credits": 2},
        {"name": "Soins infirmiers en neurologie", "coeff": 1, "credits": 2},
        {"name": "Soins infirmiers en infectieux", "coeff": 1, "credits": 2, "isSpecialCase": True},
        {"name": "Soins infirmiers et handicap", "coeff": 0.5, "credits": 1, "noControl": True},
        {"name": "Santé et sécurité au travail", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Soins infirmiers et santé de l'adolescent", "coeff": 0.5, "credits": 1, "noControl": True},
        {"name": "Stage hospitalier en médecine-chirurgie", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10},
        {"name": "Techniques infirmières (3)", "coeff": 1, "credits": 2, "singleNote": True, "controlThreshold": 8},
        {"name": "Recherche documentaire", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Anglais médical (3)", "coeff": 1, "credits": 2, "noControl": True}
    ],
    4: [
        {"name": "Raisonnement et jugement clinique", "coeff": 1, "credits": 2},
        {"name": "Stage hospitalier en médecine-chirurgie", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10},
        {"name": "Système de santé", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Économie de la santé", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Soins infirmiers en endocrinologie et diététique nutrition", "coeff": 1.5, "credits": 3, "isSpecialCase": True},
        {"name": "Soins infirmiers en pathologie digestive", "coeff": 1, "credits": 2, "isSpecialCase": True},
        {"name": "Soins infirmiers en situations critiques", "coeff": 1.5, "credits": 3, "isSpecialCase": True, "controlThreshold": 10},
        {"name": "Soins infirmiers en uro-néphrologie et hémodialyse", "coeff": 1.5, "credits": 3},
        {"name": "Soins infirmiers en Orthopédie", "coeff": 1, "credits": 2, "isSpecialCase": True},
        {"name": "Soins infirmiers en gynéco-obstétrique", "coeff": 1.5, "credits": 3},
        {"name": "Anglais médical (4)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Méthodologie de la recherche (1)", "coeff": 1, "credits": 2, "noControl": True}
    ],
    5: [
        {"name": "Soins infirmiers aux personnes âgées", "coeff": 2.5, "credits": 5},
        {"name": "Soins infirmiers en santé mentale", "coeff": 2.5, "credits": 5},
        {"name": "Soins infirmiers dans la communauté (2)", "coeff": 2, "credits": 4},
        {"name": "Carcinologie", "coeff": 1, "credits": 2},
        {"name": "Hématologie", "coeff": 1, "credits": 2},
        {"name": "Dermatologie/ORL/Ophtalmo", "coeff": 0.5, "credits": 1, "isAnatomie": True},
        {"name": "Stage hospitalier au bloc opératoire", "coeff": 1, "credits": 2, "singleNote": True, "controlThreshold": 10},
        {"name": "Stage hospitalier en soins critiques", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10},
        {"name": "Méthodologie de la recherche (2)", "coeff": 1, "credits": 2, "noControl": True},
        {"name": "Statistiques", "coeff": 0.5, "credits": 1, "noControl": True},
        {"name": "Qualité et sécurité des soins", "coeff": 1, "credits": 2, "noControl": True}
    ],
    6: [
        {"name": "Stage hospitalier de soins auprès des personnes âgées", "coeff": 1, "credits": 2, "singleNote": True, "controlThreshold": 10},
        {"name": "Soins chez les hémodialysés", "coeff": 1.5, "credits": 3, "singleNote": True, "controlThreshold": 10},
        {"name": "Projet de fin d'études", "coeff": 7, "credits": 14, "singleNote": True, "controlThreshold": 10},
        {"name": "Stage hospitalier d'intégration", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10},
        {"name": "Stage hospitalier de soins communautaires", "coeff": 2, "credits": 4, "singleNote": True, "controlThreshold": 10},
        {"name": "Stage hospitalier de soins en santé mentale", "coeff": 1.5, "credits": 3, "singleNote": True, "controlThreshold": 10}
    ]
}

def calculate_average(semester, input_data):
    subjects = subjects_by_semester.get(semester, [])
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
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    semester = data.get("semester")
    input_data = data.get("input_data")
    result = calculate_average(semester, input_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
