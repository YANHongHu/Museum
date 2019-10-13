from django.db import models

# Create your models here.


# 服装表
class Costume(models.Model):
    cs_id = models.AutoField(verbose_name="服装id，自增", primary_key=True)
    cs_name = models.CharField(verbose_name="服饰名称", max_length=32)
    # 1为女，0为男
    gender = models.CharField(verbose_name="性别", max_length=1, default="1")
    describe = models.CharField(verbose_name="描述", max_length=512, null=True)
    material = models.CharField(verbose_name="材质", max_length=16, null=True)
    texture = models.CharField(verbose_name="纹理", max_length=32, null=True)
    dynasty = models.CharField(verbose_name="朝代", max_length=16, null=True)
    cs_sort = models.CharField(verbose_name="服装类别", max_length=32)


# # 多媒体资源表
# class Media(models.Model):
#     media_id = models.AutoField(verbose_name="多媒体资源id，自增", primary_key=True)
#     media_name = models.CharField(verbose_name="资源名称", max_length=32)
#     describe = models.CharField(verbose_name="资源描述", max_length=256)


# 音频资源表
class MP3(models.Model):
    mp3_id = models.AutoField(verbose_name="音频资源id，自增", primary_key=True)
    mp3_name = models.CharField(verbose_name="音频资源名称", max_length=32)
    describe = models.CharField(verbose_name="资源描述", max_length=256)
    costume_id = models.ForeignKey(verbose_name="所属服装", to='Costume', to_fields='cs_id', on_delete=models.CASCADE)


# 视频资源表
class MP4(models.Model):
    mp4_id = models.AutoField(verbose_name="视频资源id，自增", primary_key=True)
    mp4_name = models.CharField(verbose_name="音频资源名称", max_length=32)
    describe = models.CharField(verbose_name="资源描述", max_length=256)
    costume_id = models.ForeignKey(verbose_name="所属服装", to='Costume', to_fields='cs_id', on_delete=models.CASCADE)


# VR资源表
class VR(models.Model):
    vr_id = models.AutoField(verbose_name="VR资源id，自增", primary_key=True)
    vr_name = models.CharField(verbose_name="音频资源名称", max_length=32)
    describe = models.CharField(verbose_name="资源描述", max_length=256)
    costume_id = models.ForeignKey(verbose_name="所属服装", to='Costume', to_fields='cs_id', on_delete=models.CASCADE)