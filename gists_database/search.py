from .models import Gist
import datetime

def search_gists(db_connection, **kwargs):
    if kwargs == {}:
        results = db_connection.execute('SELECT * FROM gists')
        return results.fetchall()
    elif kwargs.get('github_id'):
        results = db_connection.execute('SELECT * FROM gists WHERE github_id= :github_id', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('created_at'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at)= datetime(:created_at)', kwargs)
        return [Gist(gist) for gist in results]
    
    
    elif '__' in kwargs.keys():
        key, comparison = kwargs.keys().split('__')
        comparison = operator_dic[comparison]
        if key == 'created_at':
            results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at) ' + comparison + datetime(kwargs.keys()), kwargs)
            return [Gist(gist) for gist in results] 
    
    #Optional tests (not dynamic)
    elif kwargs.get('created_at__gt'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at)   > datetime(:created_at__gt)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('created_at__gte'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at)   >= datetime(:created_at__gte)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('created_at__lt'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at)   < datetime(:created_at__lt)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('created_at__lte'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at)   <= datetime(:created_at__lte)', kwargs)
        return [Gist(gist) for gist in results]
    
    
    elif kwargs.get('updated_at__gt'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(updated_at)   > datetime(:updated_at__gt)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('updated_at__gte'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(updated_at)   >= datetime(:updated_at__gte)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('updated_at__lt'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(updated_at)   < datetime(:updated_at__lt)', kwargs)
        return [Gist(gist) for gist in results]
    elif kwargs.get('updated_at__lte'):
        results = db_connection.execute('SELECT * FROM gists WHERE datetime(updated_at)   <= datetime(:updated_at__lte)', kwargs)
        return [Gist(gist) for gist in results]
    