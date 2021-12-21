accounts_following_you = open('accounts_following_you.txt', 'r').read().split('\n')
accounts_you_follow = open('accounts_you_follow.txt', 'r').read().split('\n')

you_follow_but_dont_follow_you = list(set(accounts_you_follow) - set(accounts_following_you))
follow_you_but_you_dont_follow = list(set(accounts_following_you) - set(accounts_you_follow))

print(f'Sigo mas não me segue: {you_follow_but_dont_follow_you}')
print(f'Segue mas não sigo: {follow_you_but_you_dont_follow}')
