
def show_settings(request):
    settings = ""
    for line in open("student/settings.py"):
        settings += "<p>%s</p>" % (str(line))

    return {'show_settings': settings}