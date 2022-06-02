from django.db import models
import uuid
import random

# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.category_name
    
class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    question = models.CharField(max_length=255)
    marks = models.IntegerField(default=5)
    
    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs) 
        data = []
        for answer_obj in answer_objs:
            data.append({
                "answer" : answer_obj.answer,
                "is_correct" : answer_obj.is_correct,
            })
        return data
    
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.answer