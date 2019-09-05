import requests

def import_gists_to_database(db, username, commit=True):
    url = 'https://api.github.com/users/{username}/gists'
    response = requests.get(url.format(username=username))
    response.raise_for_status()
    
    for gist in response.json():
        gist_db_script = """
            INSERT INTO gists ('github_id', 'html_url', 'git_pull_url', 
            'git_push_url', 'commits_url', 'forks_url', 'public', 
            'created_at', 'updated_at', 'comments', 'comments_url')
            VALUES (:github_id, :html_url, :git_pull_url, 
            :git_push_url, :commits_url, :forks_url, :public, 
            :created_at, :updated_at, :comments, :comments_url
            )""" 
        params = {
            'github_id': gist['id'], 
            'html_url': gist['html_url'], 
            'git_pull_url': gist['git_pull_url'], 
            'git_push_url': gist['git_push_url'], 
            'commits_url': gist['commits_url'], 
            'forks_url': gist['forks_url'], 
            'public': gist['public'], 
            'created_at': gist['created_at'], 
            'updated_at': gist['updated_at'], 
            'comments': gist['comments'], 
            'comments_url': gist['comments_url']
            }
        db.execute(gist_db_script, params)
        
    return db
    

"""
You are going to use the GitHub gists API to retrieve the gists of a given user, insert those gists into a database (schema may be found in the schema.sql file), and if commit is True, commit those changes to the database.
"""