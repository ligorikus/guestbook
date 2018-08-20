from models.User import User

admin = User(email="semal551@gmail.com", role=User.ROLE_ADMIN)
admin.save()
