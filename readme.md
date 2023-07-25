### Telegram bot

#### Install requirements
```
pip install -r requirements.txt
```


#### Run tg bot
```
python manage.py bot
```

#### Populate excel reports into database
```
1. Add excel file in telegram_bot/reports/oylik.xlsx folder
2. Run following command for populating
    python manage.py populate_report oylik.xlsx
```