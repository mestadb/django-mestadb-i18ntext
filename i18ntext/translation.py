# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions

from models import Text

class TextTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Text, TextTranslationOptions)
