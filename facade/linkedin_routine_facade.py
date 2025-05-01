from manager.interfaces.auth_manager_interface import IAuthManager
from manager.interfaces.connect_with_people_interface import IConnectWithPeopleManager
from manager.interfaces.feed_like_manager_interface import IFeedLikeManager

class LinkedinRoutineFacade:
    def __init__(self, auth:IAuthManager, connections:IConnectWithPeopleManager, feed_like:IFeedLikeManager):
        self.auth = auth
        self.connections = connections
        self.feed_like = feed_like

    def execute(self):
        self.auth.login()
        self.connections.connect_with_targets()
        self.feed_like.like_feed_posts()