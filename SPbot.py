import requests 
import time
 #Chat ID -605918100
quotes = {
    'What a piece of work is man, How noble in reason, how infinite in faculty, In form and moving how express and admirable, In action how like an Angel, In apprehension how like a god, The beauty of the world, The paragon of animals. And yet to me, what is this quintessence of dust? Man delights not me; no, nor Woman neither; ',
    'web of our life is of a mingled yarn, good and ill together. ',
    'And so, from hour to hour, we ripe and ripe.And then, from hour to hour, we rot and rot;And thereby hangs a tale.',
    'To be, or not to be,—that is the question:— Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune'
}

for quote in quotes:
    #stroke = input("Hi, How are you today?")
    url = 'https://api.telegram.org/bot2105491081:AAHaQEKu_2XdCfrDG7kdgCyCgpOliWUVbi4/sendMessage?chat_id=-605918100&text="{}"'.format(quote)
    requests.get(url)
    time.sleep(3)
    
    