

def get_default_stats(naut):
    print(dir(naut))
    wealthy = 50
    cute = 50
    speed = 50
    social = 50
    nimble = 50
    if naut['eyes'] == 'happy':
        social += 10
    if naut['eyes'] == 'sleepy':
        nimble -= 10
    if naut['eyes'] == 'droopy':
        wealthy -= 10
    if naut['eyes'] == 'mischevous':
        social -= 10
        nimble += 10
    if naut['eyes'] == 'glittery':
        cute += 10
        social += 10
    if naut['eyes'] == 'aviator_sunglasses':
        social += 20
    if naut['eyes'] == 'side-eye':
        social -= 20
    if naut['eyes'] == 'socn_snorkel':
        speed += 20
        nimble += 10
    if naut['eyes'] == 'sol_sunglasses': 
        wealthy += 20
        cute += 20
    if naut['mouth'] == 'grin':
        wealthy += 10
    if naut['mouth'] == 'frown':
        social -= 10
    if naut['mouth'] == 'smirk':
        wealthy += 10
        nimble += 10
    if naut['mouth'] == 'cat':
        cute += 10
        nimble += 10
    if naut['mouth'] == 'vampire':
        social -= 20
    if naut['mouth'] == 'tongue':
        cute += 20
    if naut['mouth'] == 'golden_teeth':
        social -= 10
        wealthy += 20
    if naut['mouth'] == 'aurory_mask':
        cute += 20
        social += 20
    if naut['hats'] == 'bandana':
        cute += 10
    if naut['hats'] == 'pirate_hat':
        wealthy += 10
    if naut['hats'] == 'audius_headphones':
        cute += 10
    if naut['hats'] == 'marinade_chef_hat':
        social += 10
    if naut['hats'] == 'ninja_hood':
        nimble += 10
    if naut['hats'] == 'astronaut_helmet':
        speed += 10
    return {
        'cute': cute,
        'social': social,
        'nimble': nimble,
        'speed': speed,
        'wealthy': wealthy
    }


