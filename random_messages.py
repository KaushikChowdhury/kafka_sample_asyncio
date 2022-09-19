from email import message
import random
import string

user_id = list(range(1, 101))
recipient_id = list(range(1, 101))

def generate_message():

    random_user_id = random.choice(user_id)

    recipient_ids_copy = recipient_id.copy()

    recipient_ids_copy.remove(random_user_id)

    random_recipient_id = random.choice(recipient_ids_copy)

    message = '-'.join(random.choice(string.ascii_letters) for i in range(10))

    myDict=  {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message
    }


    return myDict

if __name__=="__main__":
    print(generate_message())