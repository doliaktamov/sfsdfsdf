from main.models import Worker, Document

e = Worker.objects.first()
p = Document(worker=e)
p.inn = 'dsadsadsa'

p.save()

