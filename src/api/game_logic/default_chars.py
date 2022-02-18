
def get_default_chars(naut):
    default_chars = {
        'cute': get_cute(naut),
        'social': get_social(naut),
        'nimble': get_nimble(naut),
        'speed': get_speed(naut),
        'wealthy': get_wealth(naut)
    }
    return default_chars

def get_wealth(naut):
    if(naut.background == 'tokyo' or naut.background == 'new_york'):
        return 3
    if(naut.background == 'space' or naut.background == 'defi_land'):
        return 2
    return 0
def get_cute(naut):
    return 0
def get_social(naut):
    return 0
def get_nimble(naut):
    return 0
def get_speed(naut):
    return 0

