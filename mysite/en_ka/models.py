from django.db import models

class Word(models.Model):
    word_text = models.CharField(max_length=100)
    def __str__(self):
        return self.word_text

class Category(models.Model):
    category_text = models.CharField(max_length=20)
    def __str__(self):
        return self.category_text

class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    definition_text = models.CharField(max_length=400)
    def __str__(self):
        return self.definition_text
