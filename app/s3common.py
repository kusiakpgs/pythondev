import boto3
import os

BUCKET_NAME = os.environ.get('PYTHONDEV_BUCKET_NAME') or 'tkusiak-tf-pro'

bucket = boto3.resource('s3').Bucket(BUCKET_NAME)
s3_client = boto3.client('s3')


class StorageError(Exception):
    pass


def get_presigned_url(object_name):
    presigned_url = s3_client.generate_presigned_url('get_object',
                                                     Params={'Bucket': BUCKET_NAME,
                                                             'Key': object_name},
                                                     ExpiresIn=3600)
    return presigned_url


def generate_presigned_upload_url():
    return s3_client.generate_presigned_post(
        BUCKET_NAME,
        '${filename}',
    )


def list_s3_files():
    return bucket.objects.all()
