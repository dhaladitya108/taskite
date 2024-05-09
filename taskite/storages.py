from django.core.files.storage import FileSystemStorage


class TaskiteFileStorage(FileSystemStorage):
    def _save(self, name, content):

        print('Name', name)
        print('Content', content)

        return super()._save(name, content)
    
    def delete(self, name):
        print('Deleted --', name)
        super().delete(name)