from django.db import models

class BMBCChecksheet(models.Model):
    adjustingTube = models.CharField(max_length=100)
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    axleGuide = models.CharField(max_length=100)
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)

class BogieDetails(models.Model):
    bogieNo = models.CharField(max_length=50)
    dateOfIOH = models.DateField()
    deficitComponents = models.CharField(max_length=255)
    incomingDivAndDate = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)

class BogieChecksheetForm(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    status = models.CharField(max_length=50, default="Saved")

    bmbcChecksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)
    bogieChecksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bogieDetails = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    status = models.CharField(max_length=50, default="Saved")

    fields = models.JSONField()  # stores the complete "fields" dict
