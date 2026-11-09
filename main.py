from pyscript import document

def candidate_checker(e):
    club_members = ['jane doe', 'john doe', 'sparkle sunshine', 'alisson burgers', 
    'crystal waters', 'tree trade',' earl grey', 'winter melon', 'mr. anderson', 'todd anderson', 'charlie kelmeckis']

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    message = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are a member of The Communication Arts Club!')

    document.getElementById('output').innerHTML = message[member_checker]