import wikiquote, random
from mastodon import Mastodon

f = open('settings.py', 'r')
exec(f.read(), globals())
f.close()

i = 0
author_list = wikiquote.random_titles(max_titles=20, lang=wiki_lang)

while 1:
    try:
        quotes = wikiquote.quotes(author_list[i], lang=wiki_lang)
        text = '"%s"\n\n%s' % (quotes[0], author_list[i])
        if len(text) < 500:
            break
    except Exception:
        print('disambigous page')
    i += 1
    if i == len(author_list):
        print('No quote avalable.')
        exit(1)

print(text)

masto = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    access_token = 'pytooter_usercred.secret',
    api_base_url = mastodon_url
)

masto.log_in(
    mastodon_email,
    mastodon_password,
    to_file = 'pytooter_usercred.secret'
)
masto.status_post(text)
