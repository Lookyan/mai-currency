## Requirements
`>= python3.5`

## Local env
Create virtual env:
```bash
virtualenv venv -p python3
. ./venv
```

Install deps:
```bash
pip install -r requirements.txt
```

Run app:
```bash
python3 currency.py
```

Try it out:
```bash
curl http://127.0.0.1:5000/usd2rub?value=200
{
  "result": 14025.5204
}
```
