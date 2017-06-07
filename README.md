Для установки JSON треба ввести команду

sudo pip install simplejson


Для додавання системи в автозагрузку відкриваємо

sudo crontab -e

і в файлі пишемо

@reboot python /home/pi/smart-avto/c4.py &
