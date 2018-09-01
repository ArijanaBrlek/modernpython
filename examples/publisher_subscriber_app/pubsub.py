import time
from collections import deque, defaultdict
from heapq import merge
from itertools import islice
from sys import intern
from typing import Deque, DefaultDict, NamedTuple, Set, List, Optional

User = str
Timestamp = float
Post = NamedTuple('Post', [('timestamp', Timestamp), ('user', User), ('text', str)])

posts: Deque[Post] = deque()  # posts from newest to oldest
user_posts: DefaultDict[User, Deque[Post]] = defaultdict(deque)
following: DefaultDict[User, Set[User]] = defaultdict(set)
followers: DefaultDict[User, Set[User]] = defaultdict(set)


def post_message(user: User, text: str, timestamp: Timestamp = None) -> None:
    user = intern(user)
    timestamp = timestamp or time.time()
    post = Post(timestamp, user, text)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    user, followed_user = intern(user), intern(followed_user)
    following[user].add(followed_user)
    followers[followed_user].add(user)


def posts_by_user(user: User, limit: Optional[int] = None) -> List[Post]:
    return list(islice(user_posts[user], limit))


def posts_for_user(user: User, limit: Optional[int] = None) -> List[Post]:
    relevant = merge(*[user_posts[followed_user] for followed_user in following[user]], reverse=True)
    return list(islice(relevant, limit))


def search(phrase: str, limit: Optional[int] = None) -> List[Post]:
    # TODO Add pre-indexing to speed-up searches
    # TODO Add time sensitive caching or LRU caching
    return list(islice((post for post in posts if phrase in post.text), limit))
