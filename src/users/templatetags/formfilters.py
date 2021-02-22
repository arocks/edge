from django import template

# Adds CSS classes to a form field
# Thanks to https://stackoverflow.com/a/18962481/3107299

register = template.Library()


@register.filter(name="addcss")
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get("class", "")
    classes = css_classes.split(" ")
    if css_classes:
        if arg not in classes:
            css_classes = " ".join(classes + [arg])
    else:
        css_classes = arg
    return value.as_widget(attrs={"class": css_classes})
