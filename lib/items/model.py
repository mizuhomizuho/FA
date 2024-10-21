from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class ModelBase(DeclarativeBase):
    pass

class ItemsTable(ModelBase):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    sort: Mapped[int]
    desc: Mapped[str | None]
