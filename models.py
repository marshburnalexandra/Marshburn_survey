from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    trainer_name: str
    favorite_pokemon: str
    preferred_type: str
    favorite_region: str
    favorite_starter: str
    partner_pokemon: str
    battle_style: str
    preferred_pokeball: str
    favorite_game: str
    legendary_pokemon: str

