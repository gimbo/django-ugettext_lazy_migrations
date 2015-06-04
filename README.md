# django-ugettext_lazy_migrations

This repository demonstrates a strange behaviour (bug?) in Django 1.8, where any model field with a `help_string` of `ugettext_lazy('')` causes infinite migrations to be produced my `makemigrations`.

In `myapp/model.py`, we have:

    from django.db import models
    from django.utils.translation import ugettext_lazy as _

    class X(models.Model):
        y = models.CharField(help_text=_(''), max_length=10)

Creating an initial migration based on this model works fine.  If you then call `makemigrations` again, it *should* find no changes.  However, in fact it *does* think its finds changes, and will produce a new migration (which doesn't actually produce any SQL under `sqlmigrate`, however); subsequent calls will keep doing this, infinitely.

The `cycle` script can be used to quickly test the behaviour.  It starts by deleting any migrations and tearing down the database (sqlite, but the behaviour has also been seen with postgres), and then calls `makemigration`, `migrate`, and `makemigration`.

Setup:

1. Obtain a copy of this repository and `cd` to the directory containing this `README.md`.

2. Make and activate a virtual environment (e.g. using `mkvirtualenv`).

3. `pip install -r requirements.txt`

4. Run `./cycle`

--

The problem goes away if you do any of the following:

* Use Django 1.7.8 (problem seen with all released versions of 1.8 so far)
* Remove the `help_text` parameter
* Use a non-empty `help_text`
* Don't internationalise the `help_text` parameter
* Use `ugettext` instead of `ugettext_lazy` (which you [shouldn't](https://docs.djangoproject.com/en/1.8/topics/i18n/translation/#lazy-translations))
