import pyjokes
import random
import PIL
from PIL import Image

q_answer = ["No", "Yes", "Probably Not", "Probably Yes", "Maybe", "Definitely", "Impossible", "Hell Nah", "Hell Yeah"]

def joke():
    joke = pyjokes.get_joke()
    return(joke)
def question():
    answer = random.choice(q_answer)
    return(answer)
def idiotcmd():
    size = 196,196
    ava = Image.open('avatar.png')
    cover = Image.open('cheese.jpg')
    ava_resized = ava.resize(size, Image.ANTIALIAS)
    cover.paste(ava_resized, (523, 55))
    cover.save('cheeseResult.png')
    success = "True"
    return("True")