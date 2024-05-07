# apideck-due-date-error-demo

This project demonstrates that the creation of a `Bill` fails if `due_date` is `None` 

## How to reproduce the error
- make sure you have [Poetry](https://python-poetry.org/) installed
- run `poetry shell`
- then `poetry install`
- finally `poetry run python run.py`

You should see an error message saying `apideck.exceptions.ApiTypeError: Invalid type for variable 'due_date'. Required value type is date and passed type was NoneType at ['due_date']`