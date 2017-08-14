#!/usr/bin/env python
import sys
import string
import json
tweets = []
for line in sys.stdin:
  tweets.append(json.loads(line))
badwords=['alcoholic', 'amateur', 'analphabet', 'anarchist', 'ape', 'arse', 'arselicker', 'ass', 'ass master', 'ass-kisser', 'ass-nugget', 'ass-wipe', 'asshole', 'baby', 'backwoodsman', 'balls', 'bandit', 'barbar', 'bastard', 'bastard', 'beavis', 'beginner', 'biest', 'bitch', 'blubber gut', 'bogeyman', 'booby', 'boozer', 'bozo', 'brain-fart', 'brainless', 'brainy', 'brontosaurus', 'brownie', 'bugger', 'bugger', 'bulloks', 'bum', 'bum-fucker', 'butt', 'buttfucker', 'butthead', 'callboy', 'callgirl', 'camel', 'cannibal', 'cave man', 'chaavanist', 'chaot', 'chauvi', 'cheater', 'chicken', 'children fucker', 'clit', 'clown', 'cock', 'cock master', 'cock up', 'cockboy', 'cockfucker', 'cockroach', 'coky', 'con merchant', 'con-man', 'country bumpkin', 'cow', 'creep', 'creep', 'cretin', 'criminal', 'cunt', 'cunt sucker', 'daywalker', 'deathlord', 'derr brain', 'desperado', 'devil', 'dickhead', 'dinosaur', 'disguesting packet', 'diz brain', 'do-do', 'dog', 'dog , dirty', 'dogshit', 'donkey', 'drakula', 'dreamer', 'drinker', 'drunkard', 'dufus', 'dulles', 'dumbo', 'dummy', 'dumpy', 'egoist', 'eunuch', 'exhibitionist', 'fake', 'fanny', 'farmer', 'fart', 'fart , shitty', 'fatso', 'fellow', 'fibber', 'fish', 'fixer', 'flake', 'flash harry', 'freak', 'frog', 'fuck', 'fuck face', 'fuck head', 'fuck noggin', 'fucker', 'gangster', 'ghost', 'goose', 'gorilla', 'grouch', 'grumpy', 'head, fat', 'hell dog', 'hillbilly', 'hippie', 'homo', 'homosexual', 'hooligan', 'horse fucker', 'idiot', 'ignoramus', 'jack-ass', 'jerk', 'joker', 'junkey', 'killer', 'lard face', 'latchkey child', 'learner', 'liar', 'looser', 'lucky', 'lumpy', 'luzifer', 'macho', 'macker', 'man, old', 'minx', 'missing link', 'monkey', 'monster', 'motherfucker', 'mucky pub', 'mutant', 'neanderthal', 'nerfhearder', 'nobody', 'nurd', 'nuts, numb', 'oddball', 'oger', 'oil dick', 'old fart', 'orang-uthan', 'original', 'outlaw', 'pack', 'pain in the ass', 'pavian', 'pencil dick', 'pervert', 'pig', 'piggy-wiggy', 'pirate', 'pornofreak', 'prick', 'prolet', 'queer', 'querulant', 'rat', 'rat-fink', 'reject', 'retard', 'riff-raff', 'ripper', 'roboter', 'rowdy', 'rufian', 'sack', 'sadist', 'saprophyt', 'satan', 'scarab', 'schfincter', 'shark', 'shit eater', 'shithead', 'simulant', 'skunk', 'skuz bag', 'slave', 'sleeze', 'sleeze bag', 'slimer', 'slimy bastard', 'small pricked', 'snail', 'snake', 'snob', 'snot', 'son of a bitch', 'square', 'stinker', 'stripper', 'stunk', 'swindler', 'swine', 'teletubby', 'thief', 'toilett cleaner', 'tussi', 'typ', 'unlike', 'vampir', 'vandale', 'varmit', 'wallflower', 'wanker', 'wanker, bloody', 'weeze bag', 'whore', 'wierdo', 'wino', 'witch', 'womanizer', 'woody allen', 'worm', 'xena', 'xenophebe', 'xenophobe', 'xxx watcher', 'yak', 'yeti', 'zit face']
for tweet in tweets:
  tweet_text=tweet['text'].lower()
  time_at=tweet['created_at']
  tweet_hour=time_at.split(' ')[3].split(':')[0]
  word_count = 0  
  bad_count = 0
  for word in tweet_text.split(' '):
    word_count +=1
    if word in badwords:
      bad_count += 1
  print '%s\t%s'% (tweet_hour,str(word_count)+'_'+str(bad_count))
