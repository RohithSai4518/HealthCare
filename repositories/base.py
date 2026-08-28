"""
HealthSphere Base Repository Interfaces
Defines abstract persistence contracts for entity storage, query filtering, and transactions.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, List, Optional, TypeVar
from domain.models import BaseEntity

T = TypeVar("T", bound=BaseEntity)


class IRepository(ABC, Generic[T]):
    """Generic CRUD persistence interface."""

    @abstractmethod
    def save(self, entity: T) -> T:
        """Persist or update an entity."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: str) -> Optional[T]:
        """Retrieve entity by its unique ID."""
        pass

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Retrieve all active entities with pagination."""
        pass

    @abstractmethod
    def find(self, predicate: Callable[[T], bool], skip: int = 0, limit: int = 100) -> List[T]:
        """Query entities matching custom predicate condition."""
        pass

    @abstractmethod
    def delete(self, entity_id: str, hard_delete: bool = False) -> bool:
        """Soft or hard delete an entity."""
        pass

    @abstractmethod
    def count(self, predicate: Optional[Callable[[T], bool]] = None) -> int:
        """Count total matching entities."""
        pass
