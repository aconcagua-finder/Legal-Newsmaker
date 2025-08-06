#!/usr/bin/env python3
"""
Показывает полный промпт, который отправляется в OpenAI
"""

def show_full_openai_prompt():
    """Демонстрирует полный промпт для OpenAI с реальным контекстом"""
    
    from prompts import (
        get_openai_comic_prompt,
        get_openai_comic_styles,
        get_comic_context_from_news
    )
    import random
    
    # Пример реальной новости
    sample_news = """📜 Федеральный закон №123-ФЗ - штрафы увеличены вдвое

💬 КОММЕНТАРИЙ КАРМАННОГО КОНСУЛЬТАНТА:

С 1 июня вступает в силу закон об увеличении штрафов для автомобилистов. Теперь за превышение скорости на 20-40 км/ч придется выложить не 500, а целых 1000 рублей. За повторное нарушение - уже 2000 рублей.

Особенно "повезет" любителям погонять на трассах - там камеры фиксируют каждое движение. Совет простой: либо соблюдайте скоростной режим, либо готовьте кошелек потолще 💰

В общем, государство в очередной раз напоминает: лучший способ пополнить бюджет - это карман автомобилиста."""
    
    print("🎨 ПОЛНЫЙ ПРОМПТ ДЛЯ OPENAI")
    print("=" * 60)
    
    # Извлекаем контекст
    context = get_comic_context_from_news(sample_news)
    print(f"📝 Исходная новость:\n{sample_news}\n")
    print(f"🎯 Извлеченный контекст:\n{context}\n")
    
    # Генерируем промпт
    styles = get_openai_comic_styles()
    chosen_style = random.choice(styles)
    full_prompt = get_openai_comic_prompt(context, chosen_style)
    
    print(f"🎨 Выбранный стиль: {chosen_style}\n")
    print("📋 ПОЛНЫЙ ПРОМПТ ДЛЯ OPENAI:")
    print("-" * 60)
    print(full_prompt)
    print("-" * 60)
    
    # Анализируем промпт
    print(f"\n📊 АНАЛИЗ ПРОМПТА:")
    print(f"   📏 Длина: {len(full_prompt)} символов")
    print(f"   📖 Строк: {full_prompt.count(chr(10)) + 1}")
    
    # Проверяем ключевые секции
    sections = ["TOPIC:", "STYLE:", "SCENE REQUIREMENTS:", "CHARACTER REACTIONS:", "SPEECH BUBBLE IDEAS:", "VISUAL APPROACH:"]
    print(f"   ✅ Секции промпта:")
    for section in sections:
        present = "✅" if section in full_prompt else "❌"
        print(f"      {present} {section}")
    
    # Проверяем наличие специфичного контекста
    specific_terms = ["штраф", "автомобилист", "скорость", "1000 рублей"]
    print(f"   🎯 Специфичные термины новости в промпте:")
    for term in specific_terms:
        present = "✅" if term in full_prompt.lower() else "❌"
        print(f"      {present} '{term}'")


if __name__ == "__main__":
    show_full_openai_prompt()