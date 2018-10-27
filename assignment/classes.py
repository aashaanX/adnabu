import urllib.request as re
import datetime

import os

from django.core.mail.message import EmailMessage


class UrlExtractor:

    def download_url(self, url, request_id):
        try:
            url = url.strip("/")
            name = url.split("/")[-1]
            opener = re.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            re.install_opener(opener)
            re.urlretrieve(url, "adnabu_dow/{}.html".
                           format(str(request_id)+"/"+name))
            # response = urllib.requesturlopen(url)
            # web_content = response.read()

            # with open("adnabu_dow/{}".format(str(request_id)+"/"+name), 'w') as file:
            #     file.write(web_content)
            return True
        except Exception as e:
            print(e)
            return False
    def download_urls(self, urls, request_id):
        os.mkdir("adnabu_dow/{}".format(str(request_id)))
        result_status = []
        for url in urls:
            status = self.download_url(url, request_id)
            if status:
                result_status.append(url)
            print("download completed for", url)
        print("Zip operation")
        self.zip_files("adnabu_dow/adnabu_{}".format(str(request_id)), "adnabu_dow/{}".format(str(request_id)))
        return result_status

    def send_mail_adnabu(self, email_id, file=None, body=""):
        # from django.courllib.requestmail import EmailMessage
        print("Sending email")
        print(email_id, file)
        email = EmailMessage("title", body, to=[email_id])
        email.attach_file(file)
        email.send()


    def zip_files(self, zip_name, directory):
        from zipfile import ZipFile
        print(zip_name, directory)
        file_paths = []

        for root, directories, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_paths.append(file_path)

        with ZipFile(zip_name+".zip", 'w') as zip:
            for file in file_paths:
                print("writing file", file)
                zip.write(file)
        print("Zip Completed")



