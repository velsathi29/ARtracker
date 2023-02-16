from django.db import models
from django.utils import timezone
from django.conf import settings
from djmoney.models.fields import  MoneyField
from django.contrib.auth.models import User
import datetime

#from djmoney.models.fields import MoneyField


CALLING_CHOICES=[('Calling','Calling'),('Non Calling','Non Calling')]

CLAIM_STATUS_CHOICES=[('Follow Up Claims','Follow Up Claims'),('ERA PAYER DENIED','ERA PAYER DENIED'),('Insurance Accepted','Insurance Accepted'),('Submitted','Submitted'),('CORRESPONDENCE','CORRESPONDENCE'),('MANUAL PMT DENIAL','MANUAL PMT DENIAL'),('FROM WFH','FROM WFH'),('Ready to Submit (Electronic)','Ready to Submit (Electronic)'),('Clearinghouse Accepted','Clearinghouse Accepted'),('AMED-Insurance Contacted','AMED-Insurance Contacted'),('MEDICAL RECORDS SENT','MEDICAL RECORDS SENT'),('Med Rec/Appeals in process','Med Rec/Appeals in process'),('Payment recouped','Payment recouped'),('Overpayment Claims','Overpayment Claims'),('PAYMENT PENDING','PAYMENT PENDING'),('PRE CERT REQUEST SENT','PRE CERT REQUEST SENT'),('APPEAL SENT','APPEAL SENT')]

DENIAL_CODE_CHOICES=[('-','-'),('197','197'),('22','22'),('V55','V55'),('272','272'),('151','151'),('27','27'),('31','31'),('OA 23','OA 23'),('288','288'),('222','222'),('109','109'),('127','127'),('M29','M29')]

DISPOSITION_TYPE_CHOICES=[('Patient','Patient'),('Medical Records/Appeal in Process','Medical Records/Appeal in Process'),
       ('Submitted','Submitted'),('Payment Pending','Payment Pending'),
       ('Ready to Submit','Ready to Submit'), ('AMED Review - Coding Handoff','AMED Review - Coding Handoff'),('From WFH','From WFH'),
       ('Cur-Review-MedRec/Authorization','Cur-Review-MedRec/Authorization'),
       ('ERA Payer Denied','ERA Payer Denied'),
       ('Medical Record Sent','Medical Record Sent'), 
       ('CUR Review Appeal','CUR Review Appeal'), ('-','-'),
       ('AMED Review-Insurance contaced','AMED Review-Insurance contaced'), ('To WFH','To WFH'), ('Manual payment denial','Manual payment denial')]

STATUS_CHOICES=[('Clarification','Clarification'),('In-process','In-process'),('Pending','Pending'),('Completed','Completed')]

FINAL_STATUS_CHOICES=[('Open','Open'),('Closed','Closed')]

STEP_CHOICES=[('Need Coding review','Need Coding review'),
              ('Billed to patient','Billed to patient'),
              ('COB information need to be updated','COB information need to be updated'),
              ('Patient not active for DOS','Patient not active for DOS'),
              ('Need to submit appeal','Need to submit appeal'),
              ('Left voicemail','Left voicemail'),('Appeal in process','Appeal in process'),
              ('Adjustment posted','Adjustment posted'),
              ('Future recoupment or offset','Future recoupment or offset'),('Sent for reprocessing','Sent for reprocessing'),
              ('Need assistance to proceed further','Need assistance to proceed further'),
              ('Payment Pending','Payment Pending'),('Refiled Claim','Refiled Claim'),('Coding Review','Coding Review'),
              ('Billed to patient','Billed to patient'),
              ('Need Currence Review','Need Currence Review'),('Adjusted off','Adjusted off'),
              ('allow time','allow time'),
              ('Appeal upheld','Appeal upheld'),('Awaiting Call Back','Awaiting Call Back'),
              ('Claim paid','Claim paid'),
              ('COB information need to be updated','COB information need to be updated'),
              ('Emailed Refund Request to Svtlana','Emailed Refund Request to Svtlana'),('222','222'),
              ('Emailed SEIU requesting claim status','Emailed SEIU requesting claim status'),
              ('Emailed Svitlana following up on previous email','Emailed Svitlana following up on previous email'),('Emailed to Post Payment','Emailed to Post Payment'),
              ('Sent MR via availity','Sent MR via availity'),('Sent for reprocessing','Sent for reprocessing'),
              ('Requested copy of EOB via Fax','Requested copy of EOB via Fax'),
              ('Reprocessing','Reprocessing'),('Need to submit the records','Need to submit the records'),
              ('Need to submit reconsideration','Need to submit reconsideration'),
              ('Need to Send Sec Claim & Primary EOB','Need to Send Sec Claim & Primary EOB'),
              ('Need to send MR','Need to send MR'),('InprocesS','Inprocess'),
              ('MR sent recently','MR sent recently'),('Need advice','Need advice'),
              ('Need Approval for Writeoff','Need Approval for Writeoff'),('Need assistance to proced further',
              'Need assistance to proced further'),('Need Resend Claim via Fax','Need Resend Claim via Fax'),('Need to allow more time','Need to allow more time'),
              ('Need to appeal','Need to appeal'),('Need to Fax WOL','Need to Fax WOL'),
              ('Need to Follow Up','Need to Follow Up'),('Need to Refund Overpaid Balance','Need to Refund Overpaid Balance'),]



CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('INR','INR'),
    )

class Detail(models.Model):

                               #input fields

    received=models.DateField(null=True,blank=True)

    account_or_Claim_Number=models.CharField(max_length=20,null=True,blank=True)

    service_Date=models.DateField(null=True,blank=True)

    payer=models.CharField(max_length=500,null=True,blank=True)

    claim_Status=models.CharField(max_length=1000,choices=CLAIM_STATUS_CHOICES,null=True,blank=True)

    charge_USD=MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True,blank=True)

    balance_USD=MoneyField(max_digits=14, decimal_places=2, default_currency='USD',null=True,blank=True)

    client=models.CharField(max_length=500,null=True,blank=True)

    assigned_To=models.CharField(max_length=100,null=True,blank=True)

    upload_Date=models.DateField(null=True,blank=True)

    allocation_Date=models.DateField(auto_now_add=True) 

    aging_Lag=models.DurationField(null=True, blank=True)


    
                          #Update fields

    call_Type=models.CharField(max_length=25, choices=CALLING_CHOICES,null=True,blank=True)

    account_Status=models.CharField(max_length=100, choices=STATUS_CHOICES,null=True,blank=True)

    disposition=models.CharField(max_length=200,choices=DISPOSITION_TYPE_CHOICES,null=True,blank=True)

    denial_Code=models.CharField(max_length=10,choices=DENIAL_CODE_CHOICES,null=True,blank=True)

    step=models.CharField(max_length=200,null=True,blank=True)

    next_Best_Action_For_Success_Rate=models.CharField(max_length=1000,null=True,blank=True)

    worked_By=models.CharField(max_length=200,editable=False,null=True,blank=True)

    worked_On=models.DateField(editable=False)

    follow_up_Date=models.DateField(null=True,blank=True)

    follow_up_Comments=models.CharField(max_length=500,null=True,blank=True)

    status_history=models.TextField(blank=True,null=True)

    final_Status=models.CharField(max_length=500,null=True,blank=True)

    __previous_value=None

    #class Meta:  
        # db_table = "task_details"

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
           
            self.__previous_value = str(self.disposition)+"-"+str(self.follow_up_Comments)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # if not self.id:
        #     self.created = datetime.date.today()    #The first time a new detail is saved, it won’t have an id because there’s no row for it in the database yet. So the if not self.id check tells us that the to-do list is being saved for the first time, and we drop in a single line which fills the current date into the created field. We also want the updated field to be updated on every save, so we add a line which sets that to the current date and time. Then the super call saves the list.
        # if User.is_superuser:

        #     self.worked_On=self.worked_On
        
        # else:
        if(self.allocation_Date!='NoneType'):                                # proceed only if assigned_To is filled

            if isinstance(self.allocation_Date, str):                        #convert to date type if assigned_To is string
                self.allocation_Date=datetime.datetime.strptime(self.allocation_Date, "%Y-%m-%d").date()
        
        self.aging_Lag=datetime.datetime.now().date() - self.allocation_Date
               #  timezone.now() - self.allocation_Date  #difference b/w allocation date and today

        self.worked_On = datetime.datetime.now().date()  # datetime.now() datetime.date.today()   #  updates worked on & worked by everytime when save is clicked.
        self.worked_By = self.assigned_To  
        
        if (str(self.disposition)+"-"+str(self.follow_up_Comments)) != self.__previous_value:  #checks this time submitted disposition & follow up comments is different from previously saved values or not 
             
            self.status_history=str(self.status_history)+"\n"+str(self.disposition)+" - "+str(self.follow_up_Comments)+" - "+"("+str(self.worked_On.today())+")" # adds disposition, follow up comments & today's date with already existing string in status history

        super(Detail, self).save(force_insert, force_update, *args, **kwargs)
        self.__previous_value = str(self.disposition)+"-"+str(self.follow_up_Comments) #changing variable with this time received didposition & follow up comments

 


    def __str__(self):
        return str(self.account_or_Claim_Number)

    objects = models.Manager()











 

 




    

    


    
