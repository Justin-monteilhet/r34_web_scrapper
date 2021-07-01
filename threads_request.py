from post import Post, InvalidId

import threading
import time

posts = []
THREADS = set()

def get_post_thread(posts_id):
    global posts
    for _id in posts_id:
        if Post.is_id_valid(_id):
            posts.append(Post(str(_id)))
            
        else:
            posts.append(None)

def threaded_request(posts_id):   
    """Make rule 34 Post requests faster with threads

    Args:
    
        posts_id (iterable): IDs of the posts

    Returns:
    
        Post[]: requested Posts
    """        
    IDS = list(posts_id)
    coeff = 3
    num_full_threads = len(IDS) // coeff
    uncomplete_thread = len(IDS) % coeff
    print(time.time(), 'Creating Threads')
    for i in range(0, num_full_threads):
        posts_id = IDS[i*coeff:(i+1)*coeff]
        t = threading.Thread(target=get_post_thread, args=(posts_id,))
        THREADS.add(t)
            
    if uncomplete_thread:    
        posts_id = IDS[-uncomplete_thread:]
        t = threading.Thread(target=get_post_thread, args=(posts_id,))
        THREADS.add(t)
        
    print(time.time(), 'Threads starts')
    
    for thread in THREADS:
        thread.start()

    for thread in THREADS:
        thread.join()
    
    print(time.time(), 'Done getting all posts')
    return posts
