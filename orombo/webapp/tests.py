# vim: ai sts=4 ts=4 et sw=4
"""
Doctests for the Orombo project
"""

__test__ = {
"PostForm_test": '''
>>> from forms import PostForm
>>> # Testing a valid URL
>>> data = {'title': 'Google Homepage', 'url': 'http://www.google.com/'}
>>> f = PostForm(data)
>>> f.is_valid()
True
>>>
>>> # Testing an invalid URL
>>> data = {'title': 'None Existent', 'url': 'http://www.google.com/doesnotexist'}
>>> f = PostForm(data)
>>> f.is_valid()
False
>>>
>>> # Testing a missing title
>>> data = {'url': 'http://www.google.com'}
>>> f = PostForm(data)
>>> f.is_valid()
False
''',

"CommentForm_test": '''
''',

"PostModel_test": '''
Testing the proper creation of slugs
>>> from models import Post
>>> from django.contrib.auth.models import User
>>> u = User.objects.create_user('john', 'johndoe@orombo.com', 'orombopassword')
>>> u.save()
>>> p = Post(title="Hello World",url="http://www.google.com/",author=u)
>>> p.save()
>>> p
<Post: Hello World>
>>> p.slug
u'hello-world'
''',

"VoteModel_test": '''
''',

"CommentModel_test": '''
''',
}

