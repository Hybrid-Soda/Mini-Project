from django.db import models


class DepositProducts(models.Model):
    LIMITS = [
        (1, '제한없음'),
        (2, '서민전용'),
        (3, '일부제한'),
    ]
    fin_prdt_cd = models.TextField(primary_key=True, default='-')
    kor_co_nm = models.TextField(default='-')
    fin_prdt_nm = models.TextField(default='-')
    etc_note = models.TextField(default='-')
    join_deny = models.IntegerField(choices=LIMITS, default=1)
    join_member = models.TextField(default='-')
    join_way = models.TextField(default='-')
    spcl_cnd = models.TextField(default='-')


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()