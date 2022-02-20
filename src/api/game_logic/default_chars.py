
def get_default_stats(naut):
    default_stats = {
        'cute': get_cute(naut),
        'social': get_social(naut),
        'nimble': get_nimble(naut),
        'speed': get_speed(naut),
        'wealthy': get_wealth(naut)
    }
    return default_stats

def get_wealth(naut):
    if(naut['bg'] == 'tokyo' or naut['bg'] == 'new_york'):
        return 3
    if(naut['bg'] == 'space' or naut['bg'] == 'defi_land' or naut['bg'] == 'mondrian'):
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

