from uuid import uuid4

from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")


def create_tables():
    SQLModel.metadata.create_all(engine)


class Language(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid4().hex), primary_key=True)
    text: str


def create_language(lang: Language) -> Language:
    with Session(engine) as s:
        s.add(lang)
        s.commit()
    return lang


def update_language(lang_id: str, new_text: str) -> Language | None:
    with Session(engine) as s:
        query = select(Language).where(Language.id == lang_id)
        result = s.exec(query).first()
        if result:
            result.text = new_text
            s.commit()
            return result
        return None


def view_languages() -> list[Language]:
    with Session(engine) as s:
        query = select(Language)
        results = s.exec(query).all()
    return list(results)


def delete_language(lang_id: str) -> bool:
    with Session(engine) as s:
        query = select(Language).where(Language.id == lang_id)
        result = s.exec(query).first()
        if result:
            s.delete(result)
            s.commit()
            return True
        return False


if __name__ == "__main__":
    create_tables()
