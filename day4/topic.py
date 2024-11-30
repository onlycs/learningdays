from abc import ABC, abstractmethod
from home import Home

from manim import Text, Succession as Sequence, Animation, Wait

class Topic(ABC):
    @property
    @abstractmethod
    def title(self) -> Text:
        raise NotImplementedError("Title not implemented")

    @property
    @abstractmethod
    def num_slides(self) -> int:
        raise NotImplementedError("Number of slides not implemented")

    @abstractmethod
    def next_slide(self) -> Animation:
        raise NotImplementedError("Next slide not implemented")

    @abstractmethod
    def create(self):
        raise NotImplementedError("Create not implemented")

    @abstractmethod
    def destroy(self):
        raise NotImplementedError("Destroy not implemented")

class TopicScheduler:
    home: Home
    topics: list[Topic]

    topic: int = 0
    subslide: int = 0
    in_home: bool = True

    def __init__(self, topics: list[Topic], home: Home):
        self.topics = topics
        self.home = home

    def next_slide(self) -> Animation:
        if self.topic >= len(self.topics):
            raise ValueError("No more topics")

        if self.in_home:
            self.in_home = False
            return Sequence(
                self.home.transition_out(self.topics[self.topic].title) if self.topic > 0 else Wait(0.0),
                self.topics[self.topic].create(),
            )

        if self.subslide >= self.topics[self.topic].num_slides:
            self.topic += 1
            self.subslide = 0
            self.in_home = True

            return Sequence(
                self.topics[self.topic-1].destroy(),
                self.home.transition_in() if self.topic > 1 else self.home.init(),
            )

        self.subslide += 1
        return self.topics[self.topic].next_slide()
    
    def destroy(self):
        return self.home.destroy()

    @property
    def num_slides(self) -> int:
        return sum(topic.num_slides + 2 for topic in self.topics)