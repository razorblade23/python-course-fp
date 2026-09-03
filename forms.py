from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class AddLanguageForm(FlaskForm):
    name = StringField("Unesite ime programskog jezika")
    create_lang = SubmitField("Dodaj")


class ModifyLanguageForm(FlaskForm):
    selection = SelectField("Izaberite jezik za ažuriranje", choices=[])
    new_name = StringField("Upišite izmjenu")
    update_lang = SubmitField("Ažuriraj")


class DeleteLanguageForm(FlaskForm):
    selection = SelectField("Izaberite jezik za brisanje", choices=[])
    delete_lang = SubmitField("Obriši")
