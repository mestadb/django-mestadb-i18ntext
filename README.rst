===============
django-i18ntext
===============

Multilingual texts for Django apps.

I18ntext is a simple Django app to add multilingual texts to your Django-based web pages.
Texts are save into the database, so you can easily have different texts on different web sites.

Note that for texts, which are static and are the same on all sites, you should use
Django's i18n functionality.

Detailed documentation will appear in the "docs" directory later.

Quick start
-----------

1. Add "i18ntext" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'i18ntext',
      )

2. Optionally include the i18ntext URLconf in your project urls.py like this::

      url(r'^i18ntext/', include('i18ntext.urls')),

3. Run `python manage.py syncdb` to create the i18ntext models.

4. Add an i18ntext tag to your apps template::

      {% i18n_text "test_text" "This is default text for key 'test_text'." %}

4. Start the development server and visit the page which contains the tag above.

5. Visit http://127.0.0.1:8000/admin/i18ntext/ to manage your texts.
(you'll need the Admin app enabled).

