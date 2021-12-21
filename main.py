def difference_between_two_lists(list_1, list_2):
    return list(set(list_1) - set(list_2))

def main():
    accounts_following_you = open('accounts_following_you.txt', 'r').read().split('\n')
    accounts_you_follow = open('accounts_you_follow.txt', 'r').read().split('\n')

    you_follow_but_dont_follow_you = difference_between_two_lists(accounts_you_follow, accounts_following_you)
    follow_you_but_you_dont_follow = difference_between_two_lists(accounts_following_you, accounts_you_follow)

    print(f'Sigo mas não me segue: {you_follow_but_dont_follow_you}')
    print(f'Segue mas não sigo: {follow_you_but_you_dont_follow}')

if __name__ == '__main__':
    main()