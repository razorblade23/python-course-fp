from flask import Flask, flash, redirect, render_template, request

from database import (
    Language,
    create_language,
    create_tables,
    delete_language,
    update_language,
    view_languages,
)
from forms import AddLanguageForm, DeleteLanguageForm, ModifyLanguageForm

flask = Flask(__name__)
flask.config["SECRET_KEY"] = "my_secret_key"

programming_language_logos = {
    "python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "javascript": "https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg",
    "typescript": "https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg",
    "rust": "https://raw.githubusercontent.com/devicons/devicon/master/icons/rust/rust-original.svg",
    "go": "https://raw.githubusercontent.com/devicons/devicon/master/icons/go/go-original.svg",
    "php": "https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg",
    "c": "https://raw.githubusercontent.com/devicons/devicon/master/icons/c/c-original.svg",
    "c++": "https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg",
    "c#": "https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg",
    "java": "https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg",
    "kotlin": "https://raw.githubusercontent.com/devicons/devicon/master/icons/kotlin/kotlin-original.svg",
    "swift": "https://raw.githubusercontent.com/devicons/devicon/master/icons/swift/swift-original.svg",
    "ruby": "https://raw.githubusercontent.com/devicons/devicon/master/icons/ruby/ruby-original.svg",
    "dart": "https://raw.githubusercontent.com/devicons/devicon/master/icons/dart/dart-original.svg",
    "scala": "https://raw.githubusercontent.com/devicons/devicon/master/icons/scala/scala-original.svg",
    "elixir": "https://raw.githubusercontent.com/devicons/devicon/master/icons/elixir/elixir-original.svg",
    "haskell": "https://raw.githubusercontent.com/devicons/devicon/master/icons/haskell/haskell-original.svg",
    "lua": "https://raw.githubusercontent.com/devicons/devicon/master/icons/lua/lua-original.svg",
    "r": "https://raw.githubusercontent.com/devicons/devicon/master/icons/r/r-original.svg",
    "zig": "https://raw.githubusercontent.com/devicons/devicon/master/icons/zig/zig-original.svg",
}


@flask.route("/", methods=["GET", "POST"])
def home():
    languages = view_languages()

    add_lang_form = AddLanguageForm()
    update_lang_form = ModifyLanguageForm()
    delete_lang_form = DeleteLanguageForm()

    # Populate choices data with game data
    lang_choices = [(lang.id, lang.text) for lang in languages]
    update_lang_form.selection.choices = lang_choices
    delete_lang_form.selection.choices = lang_choices
    languages_with_logos = [
        {
            "id": choice[0],
            "text": choice[1],
            "logo": programming_language_logos.get(choice[1].lower()),
        }
        for choice in lang_choices
    ]

    # Grab the form "submit button" name (which is a key in a dict in python)
    # Check which condition applies and execute functions
    form_data = request.form
    if form_data.get("create_lang") and add_lang_form.validate_on_submit():
        lang_text = add_lang_form.name.data
        if lang_text:
            game = Language(text=lang_text.capitalize())
            create_language(game)
            flash("Jezik uspješno spremljen")
            return redirect("/")

    if form_data.get("update_lang") and update_lang_form.validate_on_submit():
        lang_id = update_lang_form.selection.data
        new_text = update_lang_form.new_name.data

        if lang_id and new_text:
            update_language(lang_id, new_text)
            flash("Jezik uspješno ažuriran")
            return redirect("/")

    if form_data.get("delete_lang") and delete_lang_form.validate_on_submit():
        lang_id = delete_lang_form.selection.data
        delete_language(lang_id)
        flash("Jezik uspješno obrisan")
        return redirect("/")

    return render_template(
        "index.html",
        add_lang_form=add_lang_form,
        update_lang_form=update_lang_form,
        delete_lang_form=delete_lang_form,
        langs=languages_with_logos,
    )


if __name__ == "__main__":
    create_tables()
    flask.run(debug=True)
