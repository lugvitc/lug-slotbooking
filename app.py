from flask import Flask, render_template, session,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<username>:<password>@<host>/<dbname>'
app.config['SECRET_KEY'] = '123456790'
db = SQLAlchemy(app)



class Users(db.Model):
    regno = db.Column(db.String(9), unique=True, primary_key=True)
    passwd =  db.Column(db.String(64), nullable=False)

class Admins(db.Model):
    name = db.Column(db.String(64), nullable=False)
    regno = db.Column(db.String(9), unique=True, primary_key=True)
    passwd = db.Column(db.String(64))

class SlotBookedApplicants(db.Model):
    name = db.Column(db.String(128), unique=False, nullable=False)
    regno = db.Column(db.String(9), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=False)
    phoneNo = db.Column(db.String(32), unique=True, nullable=False)
    department1 = db.Column(db.String(32))
    department2 = db.Column(db.String(32))
    slot1_status = db.Column(db.Integer())
    slot2_status = db.Column(db.Integer())
    slot1 = db.Column(db.String(320))
    slot2 = db.Column(db.String(320))

class Slots(db.Model):
    slot_id = db.Column(db.Integer(), unique=True, primary_key = True)
    slot_num = db.Column(db.Integer())
    department = db.Column(db.String(32))
    slot = db.Column(db.String(128))
    seats = db.Column(db.Integer())
    seats_left = db.Column(db.Integer())


class Booked_Slots(db.Model):
    id = db.Column(db.Integer(), unique=True, nullable=False,primary_key = True)
    regno = db.Column(db.String(9))
    department = db.Column(db.String(32))
    slot = db.Column(db.String(64))

class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    ops1 = db.Column(db.Text, nullable=True, unique=False)
    ops2 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Technical_Rec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_linux_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Technical_Cybersec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cybersec_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    

class Technical_Frontend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_frontend_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_Backend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_backend_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_Devops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_devops_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Technical_CP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    tech1 = db.Column(db.Text, nullable=True, unique=False)
    tech2 = db.Column(db.Text, nullable=True, unique=False)
    tech3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_1 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_2 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_3 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_4 = db.Column(db.Text, nullable=True, unique=False)
    tech_cp_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

class Management(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    mang1 = db.Column(db.Text, nullable=True, unique=False)
    mang2 = db.Column(db.Text, nullable=True, unique=False)
    mang3 = db.Column(db.Text, nullable=True, unique=False)
    mang4 = db.Column(db.Text, nullable=True, unique=False)
    mang5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)

    
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    content1 = db.Column(db.Text, nullable=True, unique=False)
    content2 = db.Column(db.Text, nullable=True, unique=False)
    content3 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)
    
class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=False)
    email = db.Column(db.String(128), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=False)
    prefDept = db.Column(db.String(128), nullable=False, unique=False)
    prefDept2 = db.Column(db.String(128), nullable=True, unique=False)
    regno = db.Column(db.String(9), nullable=False, unique=False)
    whatLinux = db.Column(db.Text, nullable=True, unique=False)
    whyLinux = db.Column(db.Text, nullable=False, unique=False)
    expLinux = db.Column(db.Text, nullable=False, unique=False)
    media1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_1 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_2 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_3 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_4 = db.Column(db.Text, nullable=True, unique=False)
    media_photo_5 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_1 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_2 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_3 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_4 = db.Column(db.Text, nullable=True, unique=False)
    media_graphic_5 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_1 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_2 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_3 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_4 = db.Column(db.Text, nullable=True, unique=False)
    media_social_media_5 = db.Column(db.Text, nullable=True, unique=False)
    media_video_1 = db.Column(db.Text, nullable=True, unique=False)
    media_video_2 = db.Column(db.Text, nullable=True, unique=False)
    media_video_3 = db.Column(db.Text, nullable=True, unique=False)
    media_video_4 = db.Column(db.Text, nullable=True, unique=False)
    media_video_5 = db.Column(db.Text, nullable=True, unique=False)
    shortlisted = db.Column(db.Boolean, nullable=True)
    slotbooked = db.Column(db.Boolean, nullable=True)
    slot = db.Column(db.String(128), nullable=True, unique=False)
    interviewed = db.Column(db.Boolean, nullable = True)
    issues = db.Column(db.Text, nullable = True)
    remarks = db.Column(db.Text, nullable = True)
    score = db.Column(db.Integer, nullable = True)



"""
@app.route('/admin')
def admin():
    try:
        x=session['user']
    except:
        session['user'] = 'nil'
    
    if session['user'] == 'admin':
        Tech = SlotBookedApplicants.query.filter(SlotBookedApplicants.department=="TECHNICAL")
        Management = SlotBookedApplicants.query.filter(SlotBookedApplicants.department=="MANAGEMENT")
        Operations = SlotBookedApplicants.query.filter(SlotBookedApplicants.department=="OPERATIONS")
        Media = SlotBookedApplicants.query.filter(SlotBookedApplicants.department=="MEDIA")
        Content = SlotBookedApplicants.query.filter(SlotBookedApplicants.department=="CONTENT")
        tch=[]
        m=[]
        op=[]
        mdia=[]
        cont=[]
        if Tech:
            for i in Tech:
                temp = {}
                temp['name'] = i.name
                temp['regno'] = i.regno
                temp['department'] = i.department
                temp['slot'] = i.slot
                tch.append(temp)
        if Management:
            for i in Management:
                temp = {}
                temp['name'] = i.name
                temp['regno'] = i.regno
                temp['department'] = i.department
                temp['slot'] = i.slot
                m.append(temp)
        if Operations:
            for i in Operations:
                temp = {}
                temp['name'] = i.name
                temp['regno'] = i.regno
                temp['department'] = i.department
                temp['slot'] = i.slot
                op.append(temp)
        if Media:
            for i in Media:
                temp = {}
                temp['name'] = i.name
                temp['regno'] = i.regno
                temp['department'] = i.department
                temp['slot'] = i.slot
                mdia.append(temp)
        if Content:
            for i in Content:
                temp = {}
                temp['name'] = i.name
                temp['regno'] = i.regno
                temp['department'] = i.department
                temp['slot'] = i.slot
                cont.append(temp)
        return render_template('admin.html',technical=tch,management=m,operations=op,media=mdia,content=cont)

    else:
        return redirect(url_for('home'))
"""
@app.route('/',methods=['GET','POST'])
def home(): 
    if request.method == "POST":
        ApplicantData = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == session["regno"]).first()
        details = request.form
        s = details["selectedslot"]
        if ApplicantData.slot1_status != 1 and ApplicantData.department1:
             dict = {}
             #g = int(ApplicantData.regno[-4:])
             #dict['id'] = g*random.randint(1,100000)
             dict['regno'] = ApplicantData.regno
             dict['department'] = ApplicantData.department1
             dict['slot'] = s
             db.session.add(Booked_Slots(**dict))
             db.session.commit()
             if ApplicantData.department1 == ApplicantData.department2:
                 ApplicantData.slot2_status = 1
             ApplicantData.slot1_status = 1
             ApplicantData.slot1 = s
             db.session.commit()
             if ApplicantData.department1 == "Technical Department - Linux":
                 DeptData = Technical_Rec.query.filter(Technical_Rec.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Technical Department - Frontend":
                 DeptData = Technical_Frontend.query.filter(Technical_Frontend.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Technical Department - Backend":
                 DeptData = Technical_Backend.query.filter(Technical_Backend.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Technical Department - Cybersec":
                 DeptData = Technical_Cybersec.query.filter(Technical_Cybersec.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Technical Department - CP":
                 DeptData = Technical_CP.query.filter(Technical_CP.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Technical Department - DevOps":
                 DeptData = Technical_Devops.query.filter(Technical_Devops.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Management Department":
                 DeptData = Management.query.filter(Management.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Operations Department":
                 DeptData = Operations.query.filter(Operations.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Media Department":
                 DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Media Department - Graphics Design":
                 DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Media Department - Social Media Engagement":
                 DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Media Department - Video":
                 DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Media Department - Photography":
                 DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             elif ApplicantData.department1 == "Content Department":
                 DeptData = Content.query.filter(Content.regno == session["regno"]).first()
                 DeptData.slot = s
                 DeptData.slotbooked = True
             db.session.commit()

             st = Slots.query.filter(Slots.department == SlotBookedApplicants.department1).filter(Slots.slot == s).first()
             st.seats_left -= 1
             db.session.commit()
             return redirect('/')
        if ApplicantData.slot2_status != 1:
             if ApplicantData.department2:
                dict = {}
                #g = int(ApplicantData.regno[-4:])
                #dict['id'] = g*random.randint(1,100000)
                dict['regno'] = ApplicantData.regno
                dict['department'] = ApplicantData.department2
                dict['slot'] = s
                db.session.add(Booked_Slots(**dict))
                db.session.commit()
                ApplicantData.slot2_status = 1
                ApplicantData.slot2 = s
                db.session.commit()
                if ApplicantData.department2 == "Technical Department - Linux":
                    DeptData = Technical_Rec.query.filter(Technical_Rec.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Technical Department - Frontend":
                    DeptData = Technical_Frontend.query.filter(Technical_Frontend.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Technical Department - Backend":
                    DeptData = Technical_Backend.query.filter(Technical_Backend.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Technical Department - Cybersec":
                    DeptData = Technical_Cybersec.query.filter(Technical_Cybersec.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Technical Department - CP":
                    DeptData = Technical_CP.query.filter(Technical_CP.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Technical Department - DevOps":
                    DeptData = Technical_Devops.query.filter(Technical_Devops.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Management Department":
                    DeptData = Management.query.filter(Management.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Operations Department":
                    DeptData = Operations.query.filter(Operations.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Media Department":
                    DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Media Department - Graphics Design":
                    DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Media Department - Social Media Engagement":
                    DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Media Department - Video":
                    DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Media Department - Photography":
                    DeptData = Media.query.filter(Media.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                elif ApplicantData.department2 == "Content Department":
                    DeptData = Content.query.filter(Content.regno == session["regno"]).first()
                    DeptData.slot = s
                    DeptData.slotbooked = True
                db.session.commit()
                st = Slots.query.filter(Slots.department == SlotBookedApplicants.department2).filter(Slots.slot == s).first()
                st.seats_left -= 1
                db.session.commit()
                dt = Booked_Slots.query.filter(Booked_Slots.regno == session['regno'])
                tmp = []
                for i in dt:
                    t = {}
                    t['department'] = i.department
                    t['slot'] = i.slot
                    tmp.append(t)
                return render_template('success.html', slt = tmp)
             
    if request.method == "GET":
        if 'regno' in session:
            tmp = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno==session["regno"]).first()            
            if tmp.slot1_status == 1 and tmp.slot2_status == 1:
                dt = Booked_Slots.query.filter(Booked_Slots.regno == session['regno'])
                tmp = []
                for i in dt:
                    t = {}
                    t['department'] = i.department
                    t['slot'] = i.slot
                    tmp.append(t)
                return render_template('success.html', slt = tmp)
            if tmp.slot1_status != 1 and tmp.department1:
                slots_list = Slots.query.filter(Slots.department==session['department1']).filter(Slots.seats_left > 0)
                sl_data = []
                for i in slots_list:
                    temp = {}
                    temp['slotid'] = i.slot_id
                    temp['slot'] = i.slot
                    temp['seats'] = i.seats
                    temp['seats_left'] = i.seats_left
                    sl_data.append(temp)
                return render_template('home.html', slotdata = sl_data, dept = tmp.department1)
            else:
                if tmp.slot2_status != 1 and tmp.department2:
                    slots_list = Slots.query.filter(Slots.department==session['department2']).filter(Slots.seats_left > 0)
                    sl_data = []
                    for i in slots_list:
                        temp = {}
                        temp['slotid'] = i.slot_id
                        temp['slot'] = i.slot
                        temp['seats'] = i.seats
                        temp['seats_left'] = i.seats_left
                        sl_data.append(temp)
                    return render_template('home.html', slotdata = sl_data, dept = tmp.department2)
                else:
                    dt = Booked_Slots.query.filter(Booked_Slots.regno == session['regno'])
                    tmp = []
                    for i in dt:
                        t = {}
                        t['department'] = i.department
                        t['slot'] = i.slot
                        tmp.append(t)
                    return render_template('success.html', slt = tmp)

        else:
            return redirect(url_for('login'))
        

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        details = request.form
        regno = details["regno"]
        password = details["password"]
        ab = Admins.query.filter(Admins.regno == regno).first()
        if ab:
            if ab.passwd == password:
                session['user'] = 'admin'
                session['regno'] = regno
                session['department'] = 'admin'
                return redirect(url_for('admin'))
        else:
            lb = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == regno).first()
            print(regno)
            print(lb.phoneNo)
            
            if lb:
                if lb.phoneNo == password:
                    applicantdetail = SlotBookedApplicants.query.filter(SlotBookedApplicants.regno == regno).first()
                    session['user'] = 'applicant'
                    session['regno'] = regno
                    session['department1'] = applicantdetail.department1
                    session['department2'] = applicantdetail.department2
                else:
                    return redirect(url_for('login'))
            if 'regno' in session:
                return redirect(url_for('home'))
    return render_template('login.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        app.run(debug=True)


