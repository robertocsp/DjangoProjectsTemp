from django import template

t = template.Template('Meu nome e {{ name }}.')
c = template.Context({'name':'Roberto'})
print t.render(c)
