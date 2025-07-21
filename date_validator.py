#!/usr/bin/env python3
"""
Модуль для проверки актуальности новостей по датам
"""

import re
from datetime import datetime, timedelta
from typing import Optional


def extract_date_from_content(content: str) -> Optional[datetime]:
    """
    Извлекает дату из контента новости
    
    Args:
        content: Текст новости
        
    Returns:
        datetime или None если дата не найдена
    """
    # Паттерны для поиска дат
    patterns = [
        r'(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})',
        r'с\s+(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)',
        r'(\d{1,2})\.(\d{1,2})\.(\d{4})',
        r'(\d{4})-(\d{1,2})-(\d{1,2})'
    ]
    
    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }
    
    for pattern in patterns:
        matches = re.findall(pattern, content.lower())
        for match in matches:
            try:
                if len(match) == 3:
                    if match[1] in months:
                        # Формат: "день месяц год"
                        day, month_name, year = match
                        month = months[month_name]
                        return datetime(int(year), month, int(day))
                    else:
                        # Формат: "день.месяц.год" или "год-месяц-день"
                        if '.' in content:
                            day, month, year = match
                            return datetime(int(year), int(month), int(day))
                        else:
                            year, month, day = match
                            return datetime(int(year), int(month), int(day))
            except (ValueError, KeyError):
                continue
                
    return None


def is_content_fresh(content: str, max_age_days: int = 3) -> tuple[bool, Optional[str]]:
    """
    Проверяет, свежий ли контент новости
    
    Args:
        content: Текст новости
        max_age_days: Максимальный возраст в днях
        
    Returns:
        (is_fresh, reason) - свежая ли новость и причина
    """
    extracted_date = extract_date_from_content(content)
    
    if not extracted_date:
        return False, "Не удалось извлечь дату из контента"
    
    now = datetime.now()
    age = (now - extracted_date).days
    
    if age < 0:
        return True, f"Будущая дата (вступает в силу {extracted_date.strftime('%d.%m.%Y')})"
    elif age <= max_age_days:
        return True, f"Свежая новость ({age} дн. назад, {extracted_date.strftime('%d.%m.%Y')})"
    else:
        return False, f"Устаревшая новость ({age} дн. назад, {extracted_date.strftime('%d.%m.%Y')})"


def get_date_feedback_for_next_prompt(content: str) -> str:
    """
    Генерирует обратную связь для следующего запроса к Perplexity
    
    Args:
        content: Текст предыдущей новости
        
    Returns:
        Текст с рекомендациями для улучшения поиска
    """
    is_fresh, reason = is_content_fresh(content)
    
    if not is_fresh:
        return f"""
ПРОБЛЕМА С ПРЕДЫДУЩИМ РЕЗУЛЬТАТОМ: {reason}

ТРЕБОВАНИЯ ДЛЯ НОВОГО ПОИСКА:
- Ищи ТОЛЬКО новости за последние 2-3 дня
- Проверяй дату публикации в источнике
- Если нет свежих новостей - лучше написать про изменения, которые вступают в силу в ближайшие 2 недели
- ОБЯЗАТЕЛЬНО укажи точную дату в тексте
        """
    else:
        return "Предыдущий поиск был успешным по актуальности дат."


if __name__ == "__main__":
    # Тест модуля
    test_content = """📜 Индексация тарифов ЖКУ — рост на 11,9% с июля

💬 КОММЕНТАРИЙ КАРМАННОГО КОНСУЛЬТАНТА:

С 1 июля 2025 года россиян ждет очередной «подарок» — тарифы на жилищно-коммунальные услуги официально увеличены на 11,9%."""
    
    print("🔍 ТЕСТ ВАЛИДАТОРА ДАТ")
    print("=" * 40)
    
    extracted = extract_date_from_content(test_content)
    print(f"📅 Извлеченная дата: {extracted}")
    
    is_fresh, reason = is_content_fresh(test_content)
    print(f"🔄 Свежесть: {is_fresh}")
    print(f"📝 Причина: {reason}")
    
    feedback = get_date_feedback_for_next_prompt(test_content)
    print(f"\n💬 Обратная связь:\n{feedback}")