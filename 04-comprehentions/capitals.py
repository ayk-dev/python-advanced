countries = input().split(', ')
capitals = input().split(', ')

info = {country: capital for country, capital in list(zip(countries, capitals))}
print('\n'.join([f'{k} -> {v}' for k, v in info.items()]))
