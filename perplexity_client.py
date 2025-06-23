import requests
import json
import re
from datetime import datetime, timedelta
from typing import Optional, Tuple, List
from loguru import logger

import config


class PerplexityClient:
    """Клиент для работы с Perplexity API (модель Sonar-pro)"""
    
    def __init__(self):
        self.api_key = config.PERPLEXITY_API_KEY
        self.api_url = config.PERPLEXITY_API_URL
        self.timeout = config.REQUEST_TIMEOUT
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _get_yesterday_date(self) -> str:
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
    
    def _create_prompt(self) -> str:
        """Создает промпт для запроса информации о законодательных изменениях"""
        yesterday_date = self._get_yesterday_date()
        
        prompt = f"""САМОЕ интересное изменение в российском законодательстве за {yesterday_date} - найди одно, но самое громкое!

КРИТИЧЕСКИ ВАЖНО:
- ОБЯЗАТЕЛЬНО изучи все найденные источники полностью
- Найди КОНКРЕТНЫЕ детали: суммы, проценты, сроки, штрафы, льготы
- ЗАПРЕЩЕНО писать "детали не раскрыты", "конкретика неизвестна" 
- Если в первых источниках мало деталей - найди дополнительные источники
- Комментарий должен содержать КОНКРЕТНЫЕ ФАКТЫ с иронией и юмором

Инструкции:
- Найди ОДНО самое значимое законодательное изменение именно за эту дату
- Если изменений нет - напиши ироничный комментарий об этом
- Пиши с легкой иронией, но в рамках приличий
- Разбей комментарий на короткие абзацы (по 1-2 предложения каждый)

Формат ответа:

📜 Название документа [1] - краткое описание (максимум 10 слов)
(ВАЖНО: обязательно используй [1] в тексте для ссылки на источник!)

💬 КОММЕНТАРИЙ КАРМАННОГО КОНСУЛЬТАНТА:

Суть изменения с конкретными цифрами и фактами, но с легкой иронией. Добавь 1-2 подходящих эмодзи.

Кого это касается в первую очередь 🎯

Как это повлияет на обычных людей 💰 или 😅

Можно добавить юмор о реакции граждан 🤔

Общий ироничный вывод или прогноз 🔮

ИСТОЧНИКИ:
- ОБЯЗАТЕЛЬНО используй маркеры [1], [2], [3] в тексте там, где ссылаешься на факты
- Например: "С 1 июня вступает в силу закон [1]", "штраф составит 5000 рублей [2]"
- В конце ответа ОБЯЗАТЕЛЬНО добавь секцию источников в формате:

ИСТОЧНИКИ:
🔗 Источник: https://sozd.duma.gov.ru/bill/номер-законопроекта
🔗 Источник: https://pravo.gov.ru/proxy/ips/?docbody=номер-документа
🔗 Источник: https://regulation.gov.ru/projects/номер-проекта

ВАЖНО: Всегда указывай реальные ссылки на официальные источники!

Отвечай только на русском языке с легкой иронией, но корректно."""

        return prompt
    
    def _extract_sources_from_content(self, content: str) -> Tuple[str, List[str]]:
        """
        Извлекает источники из ответа AI и возвращает текст с номерами + список ссылок
        
        Args:
            content: Полный ответ от AI
            
        Returns:
            Tuple[str, List[str]]: (текст с номерами источников, список ссылок по порядку)
        """
        sources = []
        
        # Разделяем контент на основную часть и секцию ссылок
        lines = content.split('\n')
        main_content_lines = []
        sources_section_started = False
        
        for line in lines:
            # Ищем строку "ИСТОЧНИКИ:" и начинаем секцию источников
            if line.strip().upper() == 'ИСТОЧНИКИ:' or line.strip().upper().startswith('ИСТОЧНИК'):
                sources_section_started = True
                # НЕ добавляем эту строку в основной контент
                continue
                
            # Ищем строку с источником (новый формат: "🔗 Источник: https://...")
            if line.strip().startswith('🔗'):
                # Извлекаем ссылку из строки типа "🔗 Источник: https://ссылка [1]"
                url_match = re.search(r'https?://[^\s\[\]]+', line)
                if url_match:
                    source_url = url_match.group().rstrip('.,;:')
                    sources.append(source_url)
                # НЕ добавляем строку в основной контент - убираем источники из отображения
                continue
                
            # Также ищем старый формат секции ссылок для совместимости
            if re.match(r'^Ссылки:\s*$', line.strip(), re.IGNORECASE):
                sources_section_started = True
                continue
            
            if sources_section_started:
                # В секции ссылок ищем строки вида [номер] ссылка
                source_match = re.match(r'^\[(\d+)\]\s*(https?://[^\s]+)', line.strip())
                if source_match:
                    source_num = int(source_match.group(1))
                    source_url = source_match.group(2).rstrip('.,;:')
                    
                    # Расширяем список если нужно
                    while len(sources) < source_num:
                        sources.append('')
                    sources[source_num - 1] = source_url
            else:
                # Основной контент - сохраняем
                main_content_lines.append(line)
        
        # Убираем пустые элементы из sources
        sources = [s for s in sources if s]
        
        # Формируем основной текст
        main_content = '\n'.join(main_content_lines).strip()
        
        # Если не нашли источники в отдельной секции, пробуем найти в тексте
        if not sources:
            url_pattern = r'https?://[^\s\)\]>]+'
            sources = re.findall(url_pattern, content)
            sources = list(set(sources))
            sources = [source.rstrip('.,;:') for source in sources]
            
            # Если URL не найдены, но есть ссылки на документы, добавляем стандартные источники
            if not sources and '[1]' in main_content:
                # Ищем упоминания законопроектов
                bill_match = re.search(r'N\s*(\d+-\d+)', main_content)
                if bill_match:
                    bill_number = bill_match.group(1)
                    sources.append(f'https://sozd.duma.gov.ru/bill/{bill_number}')
                else:
                    # Добавляем общий источник
                    sources.append('https://sozd.duma.gov.ru/')
                    
                logger.warning("Источники не найдены в ответе, добавлены стандартные ссылки")
        
        logger.debug(f"Извлечено {len(sources)} источников")
        if sources:
            for i, source in enumerate(sources, 1):
                logger.debug(f"Источник [{i}]: {source}")
        
        return main_content, sources
    
    def get_legal_updates(self) -> Optional[dict]:
        """
        Получает информацию о законодательных изменениях за вчерашний день
        
        Returns:
            dict: {'content': str, 'sources': List[str]} или None в случае ошибки
        """
        try:
            prompt = self._create_prompt()
            yesterday_date = self._get_yesterday_date()
            
            logger.info(f"Запрашиваю информацию о законодательных изменениях за {yesterday_date}")
            
            payload = {
                "model": "sonar-pro",
                "messages": [
                    {
                        "role": "system",
                        "content": "Ты эксперт по российскому законодательству. Отвечай точно и кратко."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                "max_tokens": 1000,
                "temperature": 0.2,
                "top_p": 0.9
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            
            data = response.json()
            raw_content = data['choices'][0]['message']['content']
            
            logger.info("Успешно получен ответ от Perplexity API")
            logger.debug(f"Ответ (первые 500 символов): {raw_content[:500]}...")
            
            # Проверяем наличие маркеров ссылок
            link_markers = re.findall(r'\[\d+\]', raw_content)
            if link_markers:
                logger.debug(f"Найдены маркеры ссылок в тексте: {link_markers}")
            else:
                logger.warning("В тексте не найдены маркеры ссылок [1], [2] и т.д.")
            
            # Извлекаем источники
            content, sources = self._extract_sources_from_content(raw_content)
            
            return {
                'content': content,
                'sources': sources
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе к Perplexity API: {e}")
            return None
            
        except KeyError as e:
            logger.error(f"Неожиданный формат ответа от API: {e}")
            return None
            
        except Exception as e:
            logger.error(f"Неизвестная ошибка при работе с API: {e}")
            return None
    
    def test_connection(self) -> bool:
        """
        Тестирует подключение к API
        
        Returns:
            bool: True если подключение работает
        """
        try:
            test_payload = {
                "model": "sonar-pro",
                "messages": [
                    {
                        "role": "user",
                        "content": "Привет! Это тестовый запрос."
                    }
                ],
                "max_tokens": 50
            }
            
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=test_payload,
                timeout=10
            )
            
            response.raise_for_status()
            logger.info("Тест подключения к Perplexity API прошел успешно")
            return True
            
        except Exception as e:
            logger.error(f"Ошибка при тестировании подключения: {e}")
            return False 