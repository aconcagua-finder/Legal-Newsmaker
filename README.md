# NEWSMAKER 🤖📰

Автоматический сервис для получения и публикации российских юридических новостей в Telegram.

## 🌟 Возможности

- 🔍 **Автоматический поиск** самых важных изменений в российском законодательстве
- 🤖 **AI-анализ** с использованием Perplexity Sonar-pro для глубокого понимания изменений
- 🎨 **Генерация комиксов** с помощью OpenAI GPT-Image-1 для визуализации новостей
- 💬 **Ироничные комментарии** от "Карманного Консультанта" с эмодзи
- 📱 **Автоматическая публикация** в Telegram канал каждые 3 часа
- 🔗 **Кликабельные источники** для проверки информации

## 📋 Требования

- Python 3.8+
- API ключи:
  - Perplexity API
  - OpenAI API
  - Telegram Bot Token
- Telegram канал для публикации

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/newsmaker.git
cd newsmaker
```

### 2. Установка зависимостей

```bash
# Создание виртуального окружения (рекомендуется)
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate

# Установка пакетов
pip install -r requirements.txt
```

### 3. Настройка конфигурации

```bash
# Копирование примера конфигурации
cp config_example.py config.py

# Редактирование config.py - вставьте свои API ключи
nano config.py  # или используйте любой текстовый редактор
```

### 4. Настройка Telegram

Создайте файл `.env` со следующим содержимым:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=@your_channel_or_chat_id
```

### 5. Тестирование

```bash
# Проверка всех компонентов
python main.py --test

# Пробная публикация
python main.py --run
```

### 6. Запуск автоматической публикации

```bash
# Запуск планировщика (публикация каждые 3 часа)
python main.py --start
```

## 🛠 Настройки

В файле `config.py`:

- `HOURLY_INTERVAL = 3` - интервал публикации в часах
- `LOG_LEVEL = "INFO"` - уровень логирования
- `REQUEST_TIMEOUT = 60` - таймаут для API запросов

## 📝 Использование

### Команды

- `python main.py --info` - информация о системе
- `python main.py --test` - тестирование компонентов
- `python main.py --run` - однократный запуск
- `python main.py --start` - запуск планировщика

### Логи

Логи сохраняются в папке `logs/`:
- `newsmaker.log` - основной лог
- `errors.log` - только ошибки
- `daily_YYYYMM.log` - архив по месяцам

## 🏗 Архитектура

- **main.py** - точка входа, управление режимами работы
- **scheduler.py** - планировщик задач
- **perplexity_client.py** - работа с Perplexity API для получения новостей
- **openai_client.py** - генерация комиксов через GPT-Image-1
- **telegram_client.py** - публикация в Telegram
- **logger_setup.py** - настройка системы логирования

## 🔒 Безопасность

- Никогда не коммитьте файл `config.py` с реальными ключами
- Используйте `.env` для Telegram токенов
- Регулярно обновляйте API ключи

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing`)
5. Откройте Pull Request

## 📄 Лицензия

MIT License - см. файл [LICENSE](LICENSE)

## 👤 Автор

Ваше имя - [@yourusername](https://github.com/yourusername)

---

⭐ Если проект полезен, поставьте звезду на GitHub!

## 📦 Быстрая установка

### 1. Клонирование и установка зависимостей
```bash
# Переходим в папку проекта
cd Newsmaker

# Устанавливаем зависимости
pip install -r requirements.txt
```

### 2. Настройка Telegram бота
1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Получите токен бота (например: `110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw`)
3. Добавьте бота в ваш канал как администратора
4. Получите ID канала (например: `@your_channel` или `-100123456789`)

### 3. Настройка конфигурации
```bash
# Создание .env файла (автоматически при первом запуске)
python main.py --info

# Отредактируйте .env файл
nano .env
```

Заполните `.env`:
```env
PERPLEXITY_API_KEY=your_perplexity_key_here
OPENAI_API_KEY=your_openai_key_here
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=your_channel_id_here
```

### 4. Тестирование системы
```bash
# Полный тест всех компонентов
python test_system.py

# Или встроенный тест
python main.py --test
```

### 5. Запуск
```bash
# Тестовый запуск (один раз)
python main.py --run

# Постоянная работа (планировщик)
python main.py --start
```

## 🎮 Команды

| Команда | Описание |
|---------|----------|
| `python main.py --info` | Показать информацию о системе и статус |
| `python main.py --test` | Проверить все компоненты системы |
| `python main.py --run` | Выполнить задачу один раз (для тестирования) |
| `python main.py --start` | Запустить планировщик (основной режим) |
| `python test_system.py` | Полное тестирование системы |

## ⚙️ Настройки

### Основные настройки в `config.py`:
- `DAILY_RUN_TIME = "09:00"` - время ежедневного запуска
- `REQUEST_TIMEOUT = 60` - таймаут запросов к API
- `LOG_LEVEL = "INFO"` - уровень логирования

### Переменные окружения в `.env`:
- `PERPLEXITY_API_KEY` - API ключ Perplexity
- `OPENAI_API_KEY` - API ключ OpenAI
- `TELEGRAM_BOT_TOKEN` - токен Telegram бота
- `TELEGRAM_CHANNEL_ID` - ID канала для публикации

## 📁 Структура проекта

```
Newsmaker/
├── main.py                 # Главный файл приложения
├── scheduler.py            # Планировщик задач
├── perplexity_client.py    # Клиент для Perplexity API
├── telegram_client.py      # Клиент для Telegram
├── logger_setup.py         # Настройка логирования
├── config.py              # Конфигурация
├── test_system.py         # Тестирование системы
├── requirements.txt       # Зависимости Python
├── .env                   # Переменные окружения (создается автоматически)
├── env_example.txt        # Пример .env файла
├── README.md             # Эта документация
└── logs/                 # Папка с логами (создается автоматически)
    ├── newsmaker.log     # Основной лог
    ├── errors.log        # Только ошибки
    └── daily_YYYYMM.log  # Ежемесячные отчёты
```

## 🔧 Диагностика проблем

### Проблема: "TELEGRAM_BOT_TOKEN не установлен"
**Решение:** Создайте файл `.env` и добавьте токен бота

### Проблема: "Perplexity API недоступен"
**Решение:** Проверьте интернет-соединение и валидность API ключа

### Проблема: "Telegram API недоступен"
**Решение:** 
- Проверьте правильность токена бота
- Убедитесь что бот добавлен в канал как администратор
- Проверьте правильность ID канала

### Просмотр логов:
```bash
# Последние события
tail -f logs/newsmaker.log

# Только ошибки
tail -f logs/errors.log

# Все логи
ls -la logs/
```

## 🚀 Автозапуск

### Linux/macOS (cron):
```bash
# Редактируем crontab
crontab -e

# Добавляем строку для запуска каждый день в 08:55
55 8 * * * cd /path/to/Newsmaker && /usr/bin/python3 main.py --start
```

### Windows (Task Scheduler):
1. Откройте "Планировщик заданий"
2. Создайте базовую задачу
3. Установите ежедневный запуск
4. Команда: `python.exe main.py --start`

## 📊 Мониторинг

Система автоматически создаёт детальные логи:
- 📄 **newsmaker.log** - все события системы
- 🔴 **errors.log** - только ошибки и проблемы  
- 📅 **daily_YYYYMM.log** - ежедневные отчёты по месяцам

## 🆘 Поддержка

При возникновении проблем:
1. Запустите `python test_system.py` для диагностики
2. Проверьте логи в папке `logs/`
3. Убедитесь что все настройки в `.env` корректны 