from pprint import pprint

from itertools import islice

from pubsub import *

post_message('raymondh', '#python tip: use named tuples')
post_message('barry', 'join a band today')
post_message('selik', 'gradient descent save me money on travel')
post_message('raymondh', '#python tip: develop interactively')
post_message('barry', 'learn emacs')
post_message('davin', 'teaching #python today')
post_message('selik', 'have you ever wanted to unpack mappings?')
post_message('raymondh', '#python tip: have fun programming')
post_message('davin', '#camping tip:  always take water')
post_message('barry', 'enums rock')
post_message('raymondh', '#python tip: never mutate while iterating')
post_message('davin', 'coriander and cilantro come from the same plant')

follow('davin', followed_user='raymondh')
follow('davin', followed_user='barry')

if __name__ == '__main__':
    # pprint(posts)
    # print()
    # pprint(user_posts['raymondh'])

    # pprint(following)
    # pprint(followers)

    pprint(search('#python', limit=3))