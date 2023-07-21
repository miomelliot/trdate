# Trdate

Trdate is a library for converting date and time from natural language in the Russian language to Python.

Trdate - библиотека для преобразования даты и времени из естественной речи русского языка Python.

## Installation / Установка

Use pip to install Trdate:

Используйте pip для установки [Trdate](https://pypi.org/search/?q=trdate):

```python
pip install trdate
```

## Usage / Использование

Here's an example of how to use Trdate:

Вот пример использования Trdate:

```python
import trdate

ds = trdate.TransFormDate()
ds.get_date_list("3 июля 23 год 23 59") # 2023-07-03 23:59:00
print(ds) # ['3DD', '7MM', '23YY', '2023YY', '23HH', '59MI']

```

## Documentation / Документация

For detailed documentation, please refer to the [API Reference](https://github.com/miomelliot/trdate).

Подробная документация доступна в [API Reference](https://github.com/miomelliot/trdate).

## Contributing / Участие в проекте

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

Принимаются вклады! Если у вас возникли проблемы или у вас есть предложения по улучшению, пожалуйста, создайте issue или отправьте pull request.

## License / Лицензия

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

Этот проект лицензирован под лицензией MIT. Более подробную информацию см. в файле [LICENSE](LICENSE).

## Contact / Контакты

If you have any questions or inquiries, please contact the project maintainer:

Если у вас есть вопросы или запросы, пожалуйста, свяжитесь с автором проекта:

Name: Ostrovsky Andrey Yuryevich

Email: <miomelliot@gmail.com>
