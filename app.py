from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

app = Flask(__name__)

# Load the Netflix dataset
df = pd.read_csv('data/netflix_titles.csv')

@app.route('/')
def index():
    # Basic dataset info
    total_titles = len(df)
    movie_count = len(df[df['type'] == 'Movie'])
    tvshow_count = len(df[df['type'] == 'TV Show'])
    
    # Create a pie chart for content types
    content_types = df['type'].value_counts()
    fig_types = px.pie(
        names=content_types.index, 
        values=content_types.values,
        title='Distribution of Content Types',
        color_discrete_sequence=['#E50914', '#564d4d']
    )
    chart_types = json.dumps(fig_types.to_dict())
    
    # Top 10 countries
    country_data = df['country'].dropna()
    # Split countries if multiple are listed
    countries = []
    for c in country_data:
        if ',' in str(c):
            countries.extend([x.strip() for x in c.split(',')])
        else:
            countries.append(c)
    
    country_counts = pd.Series(countries).value_counts().head(10)
    fig_countries = px.bar(
        x=country_counts.index,
        y=country_counts.values,
        title='Top 10 Countries by Content',
        labels={'x': 'Country', 'y': 'Number of Titles'},
        color_discrete_sequence=['#E50914']
    )
    chart_countries = json.dumps(fig_countries.to_dict())
    
    # Content added by year
    df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
    yearly_additions = df['year_added'].value_counts().sort_index()
    fig_additions = px.line(
        x=yearly_additions.index,
        y=yearly_additions.values,
        title='Content Added by Year',
        labels={'x': 'Year', 'y': 'Number of Titles'},
        line_shape='spline',
        markers=True,
        color_discrete_sequence=['#E50914']
    )
    chart_additions = json.dumps(fig_additions.to_dict())
    
    # Top 10 genres
    genres = []
    for g in df['listed_in']:
        if ',' in str(g):
            genres.extend([x.strip() for x in g.split(',')])
        else:
            genres.append(g)
            
    genre_counts = pd.Series(genres).value_counts().head(10)
    fig_genres = px.bar(
        x=genre_counts.index,
        y=genre_counts.values,
        title='Top 10 Genres',
        labels={'x': 'Genre', 'y': 'Number of Titles'},
        color_discrete_sequence=['#E50914']
    )
    chart_genres = json.dumps(fig_genres.to_dict())
    
    return render_template(
        'index.html',
        total_titles=total_titles,
        movie_count=movie_count,
        tvshow_count=tvshow_count,
        chart_types=chart_types,
        chart_countries=chart_countries,
        chart_additions=chart_additions,
        chart_genres=chart_genres
    )

if __name__ == '__main__':
    app.run(debug=True) 