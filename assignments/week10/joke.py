import cowsay
import pyjokes
import emoji
joke = pyjokes.get_joke()
laugh = emoji.emojize(":face_with_tears_of_joy:")
cowsay.cow(joke)
cowsay.kitty(laugh)
