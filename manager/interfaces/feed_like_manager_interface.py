from typing import Protocol

class IFeedLikeManager(Protocol):
    def like_feed_posts(self) -> None: ...