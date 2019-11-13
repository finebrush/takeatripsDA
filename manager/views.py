from django.shortcuts import render
from django import forms
from django.forms import modelformset_factory
from .models import Post, Images
from .forms import ImageForm, PostForm
from django.template import RequestContext

def post(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors) 
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'manager/main.html',
                  {'postForm': postForm, 'formset': formset})