# ELK-system
my ELK laboratory


Изначально есть лог файлы. Python скриптом парсим этот лог и вытаскиваем только нужные строки. Есть какие-то beans или beens, которые тоже парсят логи. Их пока не используем. Дальше эти строки попадают в Logstash и превращаются в json. Оттуда json попадает в elasticSearch и уже визуализируется с помощью kibana.
