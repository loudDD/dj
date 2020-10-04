# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from tinymce.models import HTMLField


class blog(models.Model):
    b_content = HTMLField()


class Book(models.Model):
    b_name = models.CharField(max_length=16, blank=True, null=True)
    cc = models.SmallIntegerField

    class Meta:
        managed = False
        db_table = 'Book'


class TwoAnimal(models.Model):
    a_name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Two_animal'


class TwoCat(models.Model):
    animal_ptr = models.OneToOneField(TwoAnimal, models.DO_NOTHING, primary_key=True)
    d_eat = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Two_cat'


class TwoDog(models.Model):
    animal_ptr = models.OneToOneField(TwoAnimal, models.DO_NOTHING, primary_key=True)
    d_leg = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Two_dog'


class TwoIdcard(models.Model):
    id_num = models.CharField(unique=True, max_length=18)

    class Meta:
        managed = False
        db_table = 'Two_idcard'


class TwoIdcardIdPerson(models.Model):
    idcard = models.ForeignKey(TwoIdcard, models.DO_NOTHING)
    person = models.ForeignKey('TwoPerson', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Two_idcard_id_person'
        unique_together = (('idcard', 'person'),)


class TwoPerson(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Two_person'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookBookinfo(models.Model):
    name = models.CharField(max_length=10)
    pub_date = models.DateField()
    commentcount = models.IntegerField()
    readcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'book_bookinfo'


class BookChoice(models.Model):
    choice_test = models.CharField(max_length=20)
    votes = models.IntegerField()
    question = models.ForeignKey('BookQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_choice'


class BookCustomerinfo(models.Model):
    c_name = models.CharField(max_length=10)
    c_sex = models.SmallIntegerField()
    c_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'book_customerinfo'


class BookPeopleinfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.IntegerField()
    book = models.ForeignKey(BookBookinfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_peopleinfo'


class BookQuestion(models.Model):
    quesion_test = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'book_question'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RegisterDeltest(models.Model):
    d_name = models.CharField(max_length=10)
    d_cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'register_deltest'


class RegisterRegisterinfo(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'register_registerinfo'


class SessiontestSessiontest(models.Model):
    s_name = models.CharField(unique=True, max_length=10)
    s_password = models.CharField(max_length=20)
    s_token = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'sessionTest_sessiontest'


class StudentsClassList(models.Model):
    c_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'students_class_list'


class StudentsStudents(models.Model):
    s_name = models.CharField(max_length=30)
    s_class = models.ForeignKey(StudentsClassList, models.DO_NOTHING)
    s_gender = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'students_students'


class VoteChoice(models.Model):
    choice_text = models.CharField(max_length=30)
    votes = models.IntegerField()
    question = models.ForeignKey('VoteQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vote_choice'


class VoteQuestion(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vote_question'


class testupload(models.Model):
    t_name = models.CharField(max_length=10)
    t_img = models.ImageField(upload_to='photo')