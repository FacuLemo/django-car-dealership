from django.shortcuts import redirect
from django.views import View

from cars.models import Comment
from cars.forms import CommentForm
from cars.repositories.comment_repository import CommentRepository

class CommentView(View):
    model = Comment
    repo = CommentRepository
    form_class = CommentForm
    
class CreateComment(CommentView):
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
        
class DeleteComment(CommentView):
    def post(self, request, id):
        repo = self.repo()
        comment = repo.get_by_id(id)
        repo.delete(comment)
        return redirect(request.META['HTTP_REFERER'])