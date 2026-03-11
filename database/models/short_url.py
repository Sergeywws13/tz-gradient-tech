from sqlalchemy.orm import Mapped, mapped_column
from database.models.base import Base


class ShortURL(Base):
    __tablename__ = "short_urls"

    short_url: Mapped[str] = mapped_column(primary_key=True)
    long_url: Mapped[str] = mapped_column()
    visits: Mapped[int] = mapped_column(default=0)
    