import boto3
import os


K_PUBLIC_READ = 'public-read'
K_BUCKET_NAME = 'wanikanji'
K_S3 = 's3'
K_AWS_ACCESS_KEY_ID = 'AKIAJPLXRHOGTNGSPWOA'
K_AWS_SECRET_ACCESS_KEY = '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'


class S3ImageManager(object):
    def __init__(self):
        self.api = S3API(K_BUCKET_NAME)

    def upload_image(self, folder, filename):
        print ('UPLOADING')
        filepath = os.path.join(folder, filename)
        uploaded_url = self.api.upload_file(filepath)
        return uploaded_url


class S3API(object):
  
    def __init__(self, bucket_name):
        self.s3 = self.connect()

    def connect(self):
        return boto3.client(K_S3, aws_access_key_id=K_AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=K_AWS_SECRET_ACCESS_KEY)

    def upload_file(self, filepath):
        return self.s3.upload_file(filepath, K_BUCKET_NAME, filepath, ExtraArgs={'ACL': K_PUBLIC_READ})
        # print ('UPLOAD FILE')
        # key = self.bucket.new_key(filepath)
        # key.set_contents_from_filename(filepath)
        # key.set_acl(K_PUBLIC_READ)
        # url = key.generate_url(expires_in=0, query_auth=False)
        # return url
