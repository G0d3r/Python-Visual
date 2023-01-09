import requests

from plotly.graph_objs import Bar
from plotly import offline

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(URL, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Umieszczenie odpowiedzi API w zmiennej.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Utworzenie wizualizacji
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(150, 150, 150)',
        'line': {'width': 2, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Oznaczone największą liczbą gwiazdek projekty Pythona w serwisie GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repozytorium',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
        },
    'yaxis': {
        'title': 'Gwiazdki',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
