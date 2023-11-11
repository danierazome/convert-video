from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from google.cloud import storage


import os
import uuid
import logging


class VistaGenerar(Resource):
    def post(self):

        storage_client = storage.Client()
        bucket = storage_client.bucket("video_conversion_bucket_uniades")
        blob = bucket.blob(request.json['blob_name'])

        with open("video.avi", "wb") as binary_file:
            binary_file.write(blob.download_as_bytes())

        return {"token": "ok"}
