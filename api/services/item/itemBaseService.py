from abc import ABC, abstractmethod


class ItemBaseService (ABC):

    @abstractmethod
    def create(self):
        """
        Abstract method for Creating Item
        """
        pass

    @abstractmethod
    def update(self):
        """
        Abstract method for Updating Item
        """
        pass

    @abstractmethod
    def get_object(self):
        """
        Abstract method for fetching Object
        """
        pass

    @abstractmethod
    def get_item(self):
        """
        Abstract method for getting Object
        """
        pass

    @abstractmethod
    def delete(self):
        """
        Abstract method for deleting Item
        """
        pass

    @abstractmethod
    def get_all_items(self):
        """
        Abstract method for List
        """
        pass

    @abstractmethod
    def get_items_with_pagination(self):
        """
        Abstract method for pagination
        """
        pass
