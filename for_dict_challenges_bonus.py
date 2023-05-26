"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


#Вывести айди пользователя, который написал больше всех сообщений
def most_texting_user(messages):
    c = Counter(message['sent_by'] for message in messages)
    max_texting_user_key = max(c, key=c.get)
    return max_texting_user_key

#Вывести айди пользователя, на сообщения которого больше всего отвечали
def most_replied_user(messages):
    c = Counter(message['reply_for'] for message in messages)
    user_replied = {}
    c = dict(c)
    for item in c:
        for message in messages:
            if item == message['id']:
                if user_replied.get(message['sent_by'], 0) == 0:
                    user_replied[message['sent_by']] = 0
                user_replied[message['sent_by']] = user_replied[message['sent_by']] + c[item]
    max_replied_user_key = max(user_replied, key=user_replied.get)
    return max_replied_user_key

#Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей
def most_viewed_messages_user(messages):
    user_views = {}
    for message in messages:
        if user_views.get(message['sent_by'], 0) == 0:
            user_views[message['sent_by']] = []
        user_views[message['sent_by']] = user_views[message['sent_by']] + message['seen_by']
    max_viewed_count = 0
    for user in user_views:
        user_views[user]= set(user_views[user])
        if len(user_views[user]) > max_viewed_count:
            max_viewed_count = len(user_views[user])
            max_viewed_user_key = user
    return max_viewed_user_key

#Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
def max_messages_times_of_day(messages):
    times_of_day ={
        'morning': 0,
        'day': 0,
        'evening': 0
    }  
    for message in messages:
        if message['sent_at'].time() <= datetime.time(12, 0, 0, 0):
            times_of_day['morning'] += 1
        elif datetime.time(12, 0, 0, 0) < message['sent_at'].time() <= datetime.time(18, 0, 0, 0):
            times_of_day['day'] += 1
        else:
            times_of_day['evening'] += 1
    max_time_of_day = max(times_of_day, key=times_of_day.get)
    return max_time_of_day
"""
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
"""
#Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов)    
def max_thread(messages):
    threads = {}
    for message in messages:
        if message['reply_for'] == None:
            if threads.get(message['id'], 0) == 0:
                threads[message['id']] = []
            #threads[message['id']] += [message['id']]
    #print(threads)
    for thread in threads:
        for message in messages:
            current_id = ''
            if message['reply_for'] == thread:
                current_id = message['id']
                threads[thread] += [current_id]
    #print(threads)
#сделал пока только словарь: ключи - первые сообщения, а значения - список реплаев на самое первое сообщение.
# видится, что если продолжать в том же духе, то пойдет по экспоненте. надо подумать, как решить.              


         

if __name__ == "__main__":
    #print(generate_chat_history())
    text = generate_chat_history()
    print(f'ID пользователя, написавшего большего всего сообщений: {most_texting_user(text)}')
    print(f'ID пользователя, на сообщения которого больше всего отвечали: {most_replied_user(text)}')
    print(f'ID пользователя, сообщения которых видело больше всего уникальных пользователей: {most_viewed_messages_user(text)}')
    print(f'В чате больше всего сообщений: {max_messages_times_of_day(text)}')
    #max_thread(text)
    
    
