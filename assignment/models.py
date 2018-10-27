from django.db import models

# Create your models here.
from assignment.classes import UrlExtractor


class URequest(models.Model):
    email_id = models.EmailField()
    email_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + str(self.email_id)

    def add_urls(self, urls):
        for url in urls:
            uurl = UUrl()
            uurl.url = url
            uurl.urequest = self
            uurl.save()

    def extract_contents(self):
        urls = UUrl.objects.filter(urequest=self).values_list('url')
        urls = [url[0] for url in urls]
        uextractor = UrlExtractor()
        status = uextractor.download_urls(urls, self.id)
        UUrl.objects.filter(urequest=self, url__in=status).update(status=True)
        extracted_urls = UUrl.objects.filter(urequest=self).values_list('url', 'status')
        body = [(x[0], "Sucess" if x[1] else "Unsucessful") for x in extracted_urls]
        uextractor.send_mail_adnabu(self.email_id, "adnabu_dow/adnabu_{}.zip".format(self.id), str(body))
        self.email_status = True
        self.save()



class UUrl(models.Model):
    url = models.CharField(max_length=1024)
    urequest = models.ForeignKey(URequest)
    status = models.BooleanField(default=False)
    note = models.TextField()

    def __str__(self):
        return str(self.urequest.id) + "|" + str(self.url) + "|" + str(self.status)
