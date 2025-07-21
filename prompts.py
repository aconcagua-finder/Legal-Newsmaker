#!/usr/bin/env python3
"""
Промпты для нейронных сетей в проекте NEWSMAKER

Этот файл содержит все промпты для работы с AI моделями:
- Perplexity Sonar Deep Research (получение юридических новостей)
- OpenAI GPT-Image-1 (генерация комиксов)
"""

from datetime import datetime, timedelta


def get_yesterday_date() -> str:
    """Получает вчерашнюю дату в формате 'день месяц'"""
    yesterday = datetime.now() - timedelta(days=1)
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа", 
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    day = yesterday.day
    month = months[yesterday.month]
    return f"{day} {month}"


# =============================================================================
# ПРОМПТЫ ДЛЯ PERPLEXITY API (получение юридических новостей)
# =============================================================================

def get_perplexity_system_prompt() -> str:
    """Системный промпт для Perplexity AI"""
    return ("Ты опытный юрист-практик, специализирующийся на актуальных изменениях "
            "законодательства. Отвечай кратко, по существу, с конкретными фактами и цифрами. "
            "КРИТИЧЕСКИ ВАЖНО: ищи только самые свежие новости за последние дни, проверяй даты в источниках! "
            "Предпочитай новости со свежими датами публикации или недавним вступлением в силу.")


def get_perplexity_daily_collection_prompt() -> str:
    """Промпт для ежедневного сбора множества законодательных новостей"""
    
    return f"""Проведи глубокий анализ и собери ВСЕ значимые изменения в российском законодательстве за ВЧЕРА.

🎯 ЗАДАЧА: Найди РОВНО 7 самых важных законодательных новостей за вчерашний день и ранжируй их по приоритету.

КРИТЕРИИ ПРИОРИТЕТА:
1. КРИТИЧЕСКАЯ важность - затрагивает миллионы граждан (налоги, пособия, штрафы)
2. ОЧЕНЬ ВАЖНАЯ - значительные изменения в популярных сферах 
3. ВАЖНАЯ - изменения в специализированных областях
4. СРЕДНЯЯ - технические изменения, уточнения процедур
5. УМЕРЕННАЯ - отраслевые изменения, региональные вопросы
6. ДОПОЛНИТЕЛЬНАЯ - профессиональные изменения, узкие области
7. НИЗКАЯ - вспомогательные изменения, процедурные вопросы

ТРЕБОВАНИЯ К КАЖДОЙ НОВОСТИ:
- Конкретные цифры: суммы, проценты, сроки, даты
- Указание кого именно затрагивает изменение
- Практический эффект для граждан/бизнеса
- Точная дата вступления в силу или принятия
- Минимум 2-3 надежных источника

ФОРМАТ ОТВЕТА (строго соблюдай структуру):

ПРИОРИТЕТ 1 - КРИТИЧЕСКИ ВАЖНО:
📜 [Название закона/изменения]

💬 КОММЕНТАРИЙ КАРМАННОГО КОНСУЛЬТАНТА:

[Первый абзац - суть изменения с конкретными цифрами]

[Второй абзац - кого затронет и практические последствия]

[Третий абзац - ироничное наблюдение или совет]

ИСТОЧНИКИ:
🔗 Источник 1: [ссылка]
🔗 Источник 2: [ссылка]

---

ПРИОРИТЕТ 2 - ОЧЕНЬ ВАЖНО:
[Аналогичный формат]

---

ПРИОРИТЕТ 5 - УМЕРЕННАЯ:
[Аналогичный формат]

---

ПРИОРИТЕТ 6 - ДОПОЛНИТЕЛЬНАЯ:
[Аналогичный формат]

---

ПРИОРИТЕТ 7 - НИЗКАЯ:
[Аналогичный формат]

АЛЬТЕРНАТИВА ЕСЛИ НЕТ СВЕЖИХ НОВОСТЕЙ:
Если за вчера нет значимых изменений, найди важные законы, которые ВСТУПАЮТ В СИЛУ в ближайшие 2-4 недели.
Обязательно укажи: "Вступает в силу [конкретная дата]"

СТИЛЬ:
- Юридический с легкой иронией
- Живой язык, как будто пишет опытный практик
- 1-2 эмодзи на новость (умеренно!)
- Каждая новость 100-150 слов
- Фокус на практические последствия для людей"""


def get_perplexity_news_prompt() -> str:
    """Основной промпт для поиска одной законодательной новости (legacy)"""
    
    return f"""Найди ОДНО главное изменение в российском законодательстве за ВЧЕРА или СЕГОДНЯ.

КРИТИЧЕСКИ ВАЖНО - СТРОГИЙ ПРИОРИТЕТ ПО СВЕЖЕСТИ:
1. Новости ТОЧНО за вчера или сегодня
2. Если за последние 2 дня ничего нет - лучше НЕ ПУБЛИКОВАТЬ чем брать старое
3. НИКОГДА не бери новости старше 3 дней
4. Обязательно укажи точную дату в тексте новости

ТРЕБОВАНИЯ:
- Изучи источники и найди КОНКРЕТНЫЕ цифры: суммы, проценты, сроки
- НЕ пиши общие фразы без конкретики
- Комментарий должен быть КОМПАКТНЫМ (100-120 слов, 2-3 абзаца)
- Стиль: юридический с легкой иронией, как будто пишет живой человек
- НЕ ставь никакие маркеры ссылок типа [1], [2] в тексте
- НЕ добавляй примечания после основного текста
- ОБЯЗАТЕЛЬНО укажи хотя бы один источник в секции ИСТОЧНИКИ

СТИЛЬ КОММЕНТАРИЯ:
- Пиши от лица опытного юриста-практика с чувством юмора
- Используй 1-2 эмодзи на весь текст (умеренно!)
- Разбей на 2-3 коротких абзаца
- Первый абзац - суть изменения с конкретными цифрами
- Второй абзац - кого затронет и практический совет
- Третий абзац (опционально) - короткое ироничное наблюдение

Формат ответа (СТРОГО СОБЛЮДАЙ):

📜 Федеральный закон №123-ФЗ - штрафы увеличены вдвое

💬 КОММЕНТАРИЙ КАРМАННОГО КОНСУЛЬТАНТА:

С 1 июня вступает в силу закон об увеличении штрафов для автомобилистов. Теперь за превышение скорости на 20-40 км/ч придется выложить не 500, а целых 1000 рублей. За повторное нарушение - уже 2000 рублей.

Особенно "повезет" любителям погонять на трассах - там камеры фиксируют каждое движение. Совет простой: либо соблюдайте скоростной режим, либо готовьте кошелек потолще 💰

В общем, государство в очередной раз напоминает: лучший способ пополнить бюджет - это карман автомобилиста.

ИСТОЧНИКИ:
🔗 Источник: https://sozd.duma.gov.ru/bill/123456-8

ВАЖНО: 
- Пиши живым языком, но профессионально
- Строго 100-120 слов в комментарии
- ОБЯЗАТЕЛЬНО включи раздел ИСТОЧНИКИ с реальной ссылкой
- Дата новости должна быть максимально свежей!

АЛЬТЕРНАТИВНЫЕ ИСТОЧНИКИ ДЛЯ ПОИСКА:
- Сайт Госдумы (duma.gov.ru) - законопроекты и принятые законы
- Официальные порталы ведомств (nalog.gov.ru, pfr.gov.ru и др.)
- Портал нормативных актов (pravo.gov.ru)
- Новостные агентства с проверенной датой публикации

ЕСЛИ НЕ НАЙДЕНО СВЕЖИХ НОВОСТЕЙ ЗА ВЧЕРА-СЕГОДНЯ:
Найди важное изменение, которое ТОЛЬКО ВСТУПАЕТ В СИЛУ в ближайшие 2-4 недели.
Это должен быть закон, который был принят ранее, но начинает действовать в текущем или следующем месяце.
Обязательно укажи в тексте: "Вступает в силу [точная дата]"

КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО:
- Брать новости старше недели без указания актуальной даты вступления в силу
- Писать про изменения, которые уже давно действуют"""


# =============================================================================
# ПРОМПТЫ ДЛЯ OPENAI API (генерация комиксов)
# =============================================================================

def get_openai_comic_styles() -> list:
    """Список доступных художественных стилей для комиксов (теперь используется только реалистичный)"""
    return [
        "photorealistic digital art, dramatic lighting, 4-panel comic layout"
    ]


def get_openai_comic_prompt(context: str, chosen_style: str) -> str:
    """Создает промпт для генерации 4-панельного комикса на основе новостей"""
    
    return f"""Create a 4-panel comic strip about Russian legal news:

TOPIC: {context}

STYLE: Realistic style, photographic quality

4-PANEL LAYOUT:
Panel 1: Setup - Character discovers the legal change (reading phone/paper)
Panel 2: Reaction - Character processes the information (confused/surprised look)
Panel 3: Understanding - Character realizes the implications (lightbulb moment)
Panel 4: Resolution - Character adapts to new reality (acceptance/action)

VISUAL REQUIREMENTS:
- NO TEXT OR SPEECH BUBBLES
- Photorealistic modern Russian characters
- Clear visual storytelling without words
- Contemporary settings (office, home, street)
- Expressive faces and body language
- Easy to understand sequence

CHARACTER DESIGN:
- Everyday Russian people (office workers, parents, drivers, etc.)
- Appropriate clothing for situation
- Clear facial expressions showing emotion progression
- Relatable appearance

COMPOSITION:
- 4 equal panels arranged horizontally
- Clean layout with clear panel separation
- Good lighting and contrast in each panel
- Focus on character expressions and actions
- Professional quality illustration

The comic should tell a complete story about how regular people discover and adapt to the legal change, using only visual storytelling without any text."""


def get_openai_test_prompt() -> str:
    """Простой промпт для тестирования OpenAI API"""
    return "Simple test image: a small blue circle on white background"


# =============================================================================
# УТИЛИТЫ ДЛЯ РАБОТЫ С ПРОМПТАМИ
# =============================================================================

def extract_news_key_points(news_content: str) -> list:
    """
    Извлекает ключевые моменты из новостей для более точного комикса
    
    Args:
        news_content: Текст новостей о законодательных изменениях
        
    Returns:
        list: Список ключевых фактов
    """
    key_points = []
    lines = news_content.split('\n')
    
    for line in lines:
        if '📜' in line:
            # Извлекаем название документа
            key_points.append(f"Legal document: {line.replace('📜', '').strip()}")
        elif any(keyword in line.lower() for keyword in 
                ['штраф', 'налог', 'закон', 'запрет', 'льгота', 'пособие']):
            # Важные юридические термины
            key_points.append(line.strip())
    
    return key_points[:3]  # Возвращаем первые 3 ключевых момента


def get_comic_context_from_news(news_content: str) -> str:
    """
    Создает контекст для комикса на основе новостей
    
    Args:
        news_content: Полный текст новостей
        
    Returns:
        str: Краткий контекст для генерации изображения
    """
    key_points = extract_news_key_points(news_content)
    return ' '.join(key_points)


def parse_collected_news(raw_content: str) -> list:
    """
    Парсит собранные новости из ответа Deep Research
    
    Args:
        raw_content: Сырой ответ от Deep Research
        
    Returns:
        list: Список словарей с новостями
    """
    news_list = []
    
    # Разделяем по приоритетам
    sections = raw_content.split('ПРИОРИТЕТ ')
    
    for i, section in enumerate(sections[1:], 1):  # Пропускаем первую пустую секцию
        try:
            # Извлекаем приоритет из заголовка секции
            priority_line = section.split('\n')[0]
            if 'КРИТИЧЕСКИ ВАЖНО' in priority_line:
                priority = 1
            elif 'ОЧЕНЬ ВАЖНО' in priority_line:
                priority = 2
            elif 'ВАЖНО' in priority_line and 'ОЧЕНЬ' not in priority_line:
                priority = 3
            elif 'СРЕДНЯЯ' in priority_line:
                priority = 4
            elif 'УМЕРЕННАЯ' in priority_line:
                priority = 5
            elif 'ДОПОЛНИТЕЛЬНАЯ' in priority_line:
                priority = 6
            elif 'НИЗКАЯ' in priority_line:
                priority = 7
            else:
                priority = i  # fallback по порядку
            
            # Разделяем контент и источники
            if 'ИСТОЧНИКИ:' in section:
                content_part, sources_part = section.split('ИСТОЧНИКИ:', 1)
            else:
                content_part = section
                sources_part = ""
            
            # Извлекаем заголовок (строка с 📜)
            title = ""
            content_lines = content_part.split('\n')
            for line in content_lines:
                if '📜' in line:
                    title = line.replace('📜', '').strip()
                    break
            
            # Извлекаем основной контент (все кроме заголовка приоритета)
            content = '\n'.join(content_lines[1:]).strip()
            
            # Извлекаем источники
            sources = []
            if sources_part:
                for line in sources_part.split('\n'):
                    if '🔗' in line and 'http' in line:
                        # Ищем URL в строке
                        import re
                        url_match = re.search(r'https?://[^\s\)]+', line)
                        if url_match:
                            # Убираем лишние символы в конце URL
                            clean_url = url_match.group().rstrip('.,;:)')
                            sources.append(clean_url)
            
            if title and content:  # Добавляем только если есть заголовок и контент
                news_item = {
                    'priority': priority,
                    'title': title,
                    'content': content,
                    'sources': sources
                }
                news_list.append(news_item)
                
        except Exception as e:
            # Логируем ошибку парсинга но продолжаем
            print(f"Ошибка парсинга секции {i}: {e}")
            continue
    
    # Сортируем по приоритету
    news_list.sort(key=lambda x: x['priority'])
    
    return news_list


# =============================================================================
# КОНФИГУРАЦИЯ ПРОМПТОВ
# =============================================================================

class PromptConfig:
    """Настройки для промптов"""
    
    # Perplexity настройки
    PERPLEXITY_MAX_TOKENS = 900  # Для одиночных новостей
    PERPLEXITY_COLLECTION_MAX_TOKENS = 8192  # Максимум для Deep Research при сборе
    PERPLEXITY_TEMPERATURE = 0.2
    PERPLEXITY_TOP_P = 0.9
    
    # OpenAI настройки
    OPENAI_IMAGE_SIZE = "1536x1024"
    OPENAI_IMAGE_QUALITY = "medium"  # low, medium, high, auto
    OPENAI_IMAGE_COUNT = 1
    
    # Общие настройки
    COMMENT_WORD_LIMIT = 120
    SIMILARITY_THRESHOLD = 0.7