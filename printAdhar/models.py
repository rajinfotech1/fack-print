from django.db import models



class AdharCardDetail(models.Model):

    # Gender
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICE ={
            (MALE, 'MALE'),
            (FEMALE , 'FEMALE'),
        }

    # State
    MP = "Madhya Pradesh"
    CG = "Chhattisgarh"

    STATE_CHOICE={
        (MP, "Madhya Pradesh"),
        (CG, "Chhattisgarh"),
    }

    # Relation type
    SON_OF = "S/O"
    DAUGHTER_OF = "D/O"
    WIFE_OF = "W/O"

    RELATION_CHOICE = {
        (SON_OF, "S/O"),
        (DAUGHTER_OF, "D/O"),
        (WIFE_OF, "W/O"),
    }

    uid = models.BigIntegerField(verbose_name="Adhar Aumber")
    full_name = models.CharField(max_length=100, verbose_name='Full Name (English)')
    relation = models.CharField(max_length=4, choices=RELATION_CHOICE, default=SON_OF, verbose_name="Relation")
    relation_name = models.CharField(max_length=100, verbose_name='Father/Husband (English)')
    date_of_birth = models.DateField(null=True, verbose_name='DOB')
    gender = models.CharField(choices=GENDER_CHOICE, max_length=8, default=MALE, verbose_name='Gender')
    image = models.ImageField(upload_to = "profile_image", verbose_name="Image")
    address = models.CharField(max_length=150, verbose_name='Address (English)', )
    city = models.CharField(max_length=20, verbose_name="City")
    state = models.CharField(choices=STATE_CHOICE, max_length=20, verbose_name="State", default=MP)

    full_name_hi = models.CharField(max_length=100, verbose_name='Full Name (Hindi)')
    relation_hi = models.CharField(max_length=20, verbose_name="Relation (hindi)")
    gender_hi = models.CharField(max_length=20, verbose_name='Gender (Hindi)')
    relation_name_hi = models.CharField(max_length=100, verbose_name='Father/Husband (Hindi)')
    address_hi = models.CharField(max_length=150, verbose_name='Address (Hindi)', )
    city_hi = models.CharField(max_length=20, verbose_name="City (Hindi)")
    state_hi = models.CharField(max_length=50, verbose_name="State (Hindi)")

    pin_code = models.CharField(max_length=6, default="482000", verbose_name= "PIN CODE")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


