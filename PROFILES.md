# 👥 Система профилей NEWSMAKER

## 📋 Оглавление
- [Обзор](#обзор)
- [Быстрый старт](#быстрый-старт)
- [Управление через веб-интерфейс](#управление-через-веб-интерфейс)
- [Структура профиля](#структура-профиля)
- [API для разработчиков](#api-для-разработчиков)
- [Примеры использования](#примеры-использования)

## 🎯 Обзор

Система профилей позволяет сохранять и быстро переключаться между различными конфигурациями NEWSMAKER. Это особенно полезно для:

- **Тестирования** - отдельный профиль с тестовыми настройками
- **Разных каналов** - профили для разных Telegram каналов
- **Экспериментов** - тестирование новых моделей и параметров
- **Резервных копий** - сохранение рабочих конфигураций

## 🚀 Быстрый старт

### 1. Запустите веб-интерфейс
```bash
python web_config_app.py
```
Откройте http://localhost:5000 в браузере

### 2. Профили по умолчанию
- **Pocket Consultant** - дефолтный профиль (нельзя удалить)
- Автоматически создается при первом запуске
- Содержит оптимальные настройки для юридических новостей

### 3. Создание нового профиля
1. Нажмите кнопку "➕ Новый" в панели профилей
2. Введите название профиля
3. Профиль создается как копия текущего

## 🌐 Управление через веб-интерфейс

### Панель профилей
Расположена в верхней части интерфейса:

```
[👤 Профиль: [Pocket Consultant ▼]] [⬇ Загрузить] [💾 Сохранить] [➕ Новый] [📋 Дублировать] [🗑 Удалить]
```

### Основные операции

#### Загрузка профиля
- Выберите профиль из списка
- Нажмите "⬇ Загрузить"
- Все настройки обновятся автоматически

#### Сохранение изменений
- Внесите изменения в настройки
- Нажмите "💾 Сохранить"
- Изменения сохранятся в текущий профиль

#### Создание профиля
- Нажмите "➕ Новый"
- Введите уникальное название
- Новый профиль создается с текущими настройками

#### Дублирование профиля
- Выберите профиль для копирования
- Нажмите "📋 Дублировать"
- Введите название для копии

#### Удаление профиля
- Выберите профиль (кроме Pocket Consultant)
- Нажмите "🗑 Удалить"
- Подтвердите удаление

## 📁 Структура профиля

Профили хранятся в папке `profiles/` в формате JSON:

```json
{
  "config": {
    "api_models": {
      "perplexity": {
        "model": "sonar-deep-research",
        "max_tokens": 8192,
        "temperature": 0.7,
        "top_p": 0.9,
        "presence_penalty": 0.0,
        "frequency_penalty": 0.0,
        "search_domain_filter": [],
        "return_citations": true
      },
      "openai": {
        "model": "dall-e-3",
        "image_quality": "standard",
        "image_style": "vivid",
        "image_size": "1024x1024",
        "response_format": "url",
        "n_images": 1
      }
    },
    "schedule": {
      "collection_time": "08:30",
      "publication_times": ["09:05", "11:03", "13:07", "15:09", "17:05", "19:02", "21:07"],
      "timezone": "Europe/Moscow"
    },
    "content": {
      "max_news_per_day": 7,
      "min_content_length": 50,
      "max_content_length": 1500,
      "generate_images": true,
      "publish_without_images": false
    }
  },
  "prompts": {
    "perplexity_system": "...",
    "perplexity_collection": "...",
    "openai_comic": "..."
  },
  "created_at": "2025-08-06T14:00:00+03:00",
  "updated_at": "2025-08-06T14:00:00+03:00"
}
```

## 🔧 API для разработчиков

### Python API

```python
from web_config_app import ConfigManager

# Инициализация
cm = ConfigManager()

# Список всех профилей
profiles = cm.profiles.keys()
print(f"Доступные профили: {list(profiles)}")

# Загрузка профиля
cm.load_profile("Мой тестовый")

# Изменение настроек
cm.config["content"]["max_news_per_day"] = 5
cm.config["api_models"]["openai"]["image_quality"] = "hd"

# Сохранение в текущий профиль
cm.save_profile(cm.current_profile)

# Создание нового профиля
cm.save_profile("Новый профиль")

# Дублирование профиля
cm.duplicate_profile("Pocket Consultant", "Моя копия")

# Удаление профиля
cm.delete_profile("Старый профиль")
```

### REST API

#### Получить список профилей
```http
GET /api/profiles
```

#### Загрузить профиль
```http
POST /api/profiles/load
{
  "profile_name": "Мой профиль"
}
```

#### Сохранить профиль
```http
POST /api/profiles/save
{
  "profile_name": "Мой профиль"
}
```

#### Создать профиль
```http
POST /api/profiles/create
{
  "profile_name": "Новый профиль"
}
```

#### Дублировать профиль
```http
POST /api/profiles/duplicate
{
  "source_name": "Pocket Consultant",
  "new_name": "Копия"
}
```

#### Удалить профиль
```http
POST /api/profiles/delete
{
  "profile_name": "Старый профиль"
}
```

## 💡 Примеры использования

### Профиль для тестирования

```python
# Создаем тестовый профиль с минимальными затратами
cm = ConfigManager()
cm.config["content"]["max_news_per_day"] = 2
cm.config["content"]["generate_images"] = False
cm.config["api_models"]["openai"]["image_quality"] = "low"
cm.config["api_models"]["perplexity"]["max_tokens"] = 1000
cm.save_profile("Тестовый")
```

### Профиль для другого канала

```python
# Профиль с другим расписанием и стилем
cm = ConfigManager()
cm.config["schedule"]["publication_times"] = ["10:00", "14:00", "18:00"]
cm.prompts["perplexity_collection"] = "Собери новости в более формальном стиле..."
cm.save_profile("Официальный канал")
```

### Профиль с высоким качеством

```python
# Максимальное качество изображений
cm = ConfigManager()
cm.config["api_models"]["openai"]["model"] = "gpt-image-1"
cm.config["api_models"]["openai"]["image_quality"] = "high"
cm.config["api_models"]["openai"]["image_size"] = "4096x4096"
cm.save_profile("Premium")
```

### Профиль без изображений

```python
# Только текстовые публикации
cm = ConfigManager()
cm.config["content"]["generate_images"] = False
cm.config["content"]["publish_without_images"] = True
cm.save_profile("Текстовый")
```

## 🔄 Миграция профилей

### Экспорт профиля
```python
import json

cm = ConfigManager()
cm.load_profile("Мой профиль")

# Экспорт в файл
with open("my_profile_backup.json", "w") as f:
    json.dump({
        "config": cm.config,
        "prompts": cm.prompts
    }, f, indent=2)
```

### Импорт профиля
```python
import json

cm = ConfigManager()

# Импорт из файла
with open("my_profile_backup.json", "r") as f:
    data = json.load(f)
    cm.config = data["config"]
    cm.prompts = data["prompts"]
    cm.save_profile("Импортированный")
```

## 📊 Сравнение профилей

| Параметр | Pocket Consultant | Тестовый | Premium |
|----------|------------------|----------|---------|
| Новостей в день | 7 | 2 | 7 |
| Генерация изображений | ✅ | ❌ | ✅ |
| Модель изображений | DALL-E 3 | - | GPT-Image-1 |
| Качество | standard | - | high |
| Размер | 1024x1024 | - | 4096x4096 |
| Max tokens | 8192 | 1000 | 8192 |

## ⚠️ Важные замечания

1. **Дефолтный профиль** - "Pocket Consultant" нельзя удалить
2. **API ключи** - хранятся отдельно в `.env` файле, не в профилях
3. **Автосохранение** - изменения сохраняются только при явном сохранении
4. **Совместимость** - профили совместимы между версиями
5. **Резервные копии** - рекомендуется экспортировать важные профили

## 🆘 Решение проблем

### Профиль не загружается
- Проверьте, что файл профиля не поврежден
- Убедитесь, что JSON валидный
- Проверьте права доступа к папке `profiles/`

### Изменения не сохраняются
- Нажмите "Сохранить все" в веб-интерфейсе
- Проверьте логи на наличие ошибок
- Убедитесь, что папка `profiles/` доступна для записи

### Потерянный профиль
- Проверьте папку `profiles/` на наличие файла
- Используйте историю изменений в веб-интерфейсе
- Восстановите из резервной копии

---

📝 **Совет**: Регулярно экспортируйте важные профили для резервного копирования!