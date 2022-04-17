from utils import get_candidates, format_candidates, get_candidate_by_id, get_candidates_by_skill

from flask import Flask

app = Flask(__name__)


# Главная страница сайта
@app.route("/")
def main():
    candidates_list = get_candidates("candidates.json")

    return format_candidates(candidates_list)


# Страница с кандидатами
@app.route("/candidates/<int:candidate_id>")
def page_candidate(candidate_id):
    candidates_list = get_candidates("candidates.json")

    candidate = get_candidate_by_id(candidates_list, candidate_id)

    result = f'<img src="{candidate["picture"]}">'

    return result + format_candidates([candidate])


# Страница вывода кандидата по скилу
@app.route("/skills/<skill>")
def skills(skill):
    candidates_list = get_candidates("candidates.json")

    return format_candidates(get_candidates_by_skill(candidates_list, skill))


app.run()
