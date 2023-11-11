# from modelos import db, VideoConversion, Usuario
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import datetime
# import os


# class Video:

#     def __init__(self, app):
#         self.app = app

#     def convert_video(self, conversion_id):
#         with self.app.app_context():
#             conversion = VideoConversion.query.filter(
#                 VideoConversion.id == conversion_id).first()
#             usuario = Usuario.query.filter(
#                 Usuario.id == conversion.usuario_id).first()
#             mail_params = {}
#             # UPDATE STATUS
#             conversion.state = "IN-PROGRESS"
#             db.session.commit()

#             # SET CONVERTED VIDEO INFORMATION
#             formated_video_name = "".join(
#                 [conversion.id, ".", conversion.conversion_format])

#             # OPEN CONVERTED VIDEO
#             with open(formated_video_name, "wb") as binary_file:
#                 binary_file.write(conversion.video)

#             formated_video = open(formated_video_name, "rb")

#             # UPDATE CONVERSION ENTITY
#             conversion.state = "DONE"
#             conversion.video_converted = formated_video.read()
#             conversion.conversion_date = datetime.datetime.now()
#             mail_params['email'] = usuario.email
#             mail_params['name'] = conversion.video_name
#             mail_params['conversion_date'] = conversion.conversion_date
#             self.send_email(mail_params)
#             db.session.commit()

#             # CLOSE AND DELETE VIDEO FILE
#             formated_video.close()
#             os.remove(formated_video_name)


# # from converter import Converter
# # conv = Converter()

# # OTRA OPCION
# # try:
# #     convert = conv.convert(video_name, formated_video_name, {
# #         'format': conversion.conversion_format,
# #         'audio': {
# #             'codec': 'mp3',
# #             'samplerate': 11025,
# #             'channels': 2
# #         },
# #         'video': {
# #             'codec': 'h264',
# #             'width': 720,
# #             'height': 400,
# #             'fps': 15
# #         }})

# #     for timecode in convert:
# #         print(timecode)

# # except:
# #     print("Something could be wrong")
