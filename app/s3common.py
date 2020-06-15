import boto3, os
#from app.abcdef import BUCKET_NAME, BUCKET_KEY

BUCKET_NAME = os.environ.get('PYTHONDEV_BUCKET_NAME') or 'tkusiak-priv-tf-pro'
BUCKET_KEY = os.environ.get('PYTHONDEV_BUCKET_KEY', '')

bucket = boto3.resource('s3').Bucket(BUCKET_NAME)
s3_client = boto3.client('s3')


class StorageError(Exception):
    pass


def get_presigned_url(object_name):
    #object_key = f'{BUCKET_KEY}/{object_name}'
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


# def upload_file(content, object_name):
#     object_key = f'{BUCKET_KEY}/{object_name}'
#     try:
#         bucket.put_object(Key=object_key, Body=content)
#     except ClientError:
#         raise StorageError
#     return object_key