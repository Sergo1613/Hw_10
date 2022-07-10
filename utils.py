import json


def load_candidates():  # Загрузит данные из файла
    """
        Загружает из файла список кандидатов
        Возвращает list[dict]
        """
    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_all():  # Покажет всех кандидатов
    """
       :return: форматированный список всех кандидатов str
       """
    candidates = load_candidates()
    result = '<pre>'
    for cand in candidates:
        result += f"Имя кандидата : {cand['name']}\nПозиция: {cand['position']}\nНавыки: {cand['skills']}\n\n"
    result += '<pre>'
    return result


def get_by_pk(pk: int) -> str:  # которая вернет кандидата по pk
    """
    :param pk: id candidate
    :return: форматированную колонку кандидата по id
    """
    candidates = load_candidates()
    result: str = '<pre>'
    for cand in candidates:
        if cand['pk'] == pk:
            url = cand['picture']
            result += f"<img src='{url}'>\nИмя кандидата: {cand['name']}\nПозиция: {cand['position']}\nНавыки: {cand['skills']}\n\n"
    result += '</pre>'
    return result


def get_by_skill(skill_name: str) -> str:  # которая вернет кандидатов по навыку
    """
    :param skill_name: строка со скилом
    :return: форматированную строку всех подходящих кандидатов
    """
    candidates = load_candidates()
    result = '<pre>'
    for cand in candidates:
        skill_name = skill_name.lower()
        skill_str = cand["skills"]
        skill_str = skill_str.lower()
        if skill_name in skill_str:
            url = cand['picture']
            result += f"<img src='{url}'>\nИмя кандидата: {cand['name']}\nПозиция: {cand['position']}\nНавыки: {cand['skills']}\n\n"
    result += '</pre>'
    return result
