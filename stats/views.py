from django.shortcuts import render
import glob
from .models import Player,PowerPlay,PlayerTeam,MiddleOvers,DeathOvers,Matchups,City,Position,AgainstTeam
# Create your views here.
from django.http import HttpResponse
import yaml
import os
from os import listdir
from django.db.models import Q 
from os.path import isfile, join
import numpy as N
from django.templatetags.static import static
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
def home(request):
    return render(request, '../templates/html/home.html')
def filter(request):
    return render(request, '../templates/html/filter1.html')
def filterruns(request):
    player=Player.objects.all().order_by('-runs')

    return render(request, '../templates/html/filterruns.html',context={'player':player})
def m(request):
    player=Player.objects.all()

    return render(request, '../templates/html/matchups.html',context={'player':player})
def Fantasy(request):
    return render(request, '../templates/html/Fantasy.html')

def matchup1(request):
    
    try:
        entry_title = request.POST["drop1"]
    except KeyError:
        entry_title = "x"
    try:
        entry_title1 = request.POST["drop2"]
    except KeyError:
        entry_title1 = "x"
    print(entry_title)
    print(entry_title1)
    
    if entry_title and entry_title1:
        posts=Matchups.objects.filter(name=entry_title,bowler=entry_title1)
        if posts:
            posts = Matchups.objects.get(name=entry_title,bowler=entry_title1)
        else:
            return HttpResponse("THEY HAVE NOT FACED EACH OTHER")
       

	
    return render(request, '../templates/html/m1.html',context={'post':posts})
def matchup2(request):
    
    try:
        entry_title = request.POST["d1"]
    except KeyError:
        entry_title = "x"
    try:
        entry_title1 = request.POST["d2"]
    except KeyError:
        entry_title1 = "x"
    print(entry_title)
    print(entry_title1)
    
    if entry_title and entry_title1:
        posts=Matchups.objects.filter(name=entry_title,bowler=entry_title1)
        if posts:
            posts = Matchups.objects.get(name=entry_title,bowler=entry_title1)
        else:
            return HttpResponse("THEY HAVE NOT FACED EACH OTHER")
       

	
    return render(request, '../templates/html/m1.html',context={'post':posts})
def PlayerStats(request):
    return render(request, '../templates/html/PlayerStats.html')


def About(request):
    return render(request, '../templates/html/About.html')


def Contact(request):
    return render(request, '../templates/html/Contact.html')


def Disclaimer(request):
    return render(request, '../templates/html/Disclaimer.html')

def teamlist(request,id):
    player=PlayerTeam.objects.filter(name=id)
    
    return render(request, '../templates/html/teamlist.html',context={'player':player})


def citylist(request,id):
    player=City.objects.filter(name=id)
    
    return render(request, '../templates/html/citylist.html',context={'player':player})
    
def againstlist(request,id):
    player=AgainstTeam.objects.filter(name=id)
    
    return render(request, '../templates/html/againstlist.html',context={'player':player})

def positionlist(request,id):
    player=Position.objects.filter(name=id)
    
    return render(request, '../templates/html/positionlist.html',context={'player':player})
def playerProfile(request,id):
    
    player=Player.objects.get(name=id)
    context = {
				'player':player ,
                
			}
    return render(request, '../templates/html/playerProfile.html',context)

def playerProfile1(request,id):
    
    player=PlayerTeam.objects.get(id=id)
    return render(request, '../templates/html/playerProfile1.html',context={'player':player})
def playerProfile2(request,id):
    
    player=City.objects.get(id=id)
    return render(request, '../templates/html/playerProfile2.html',context={'player':player})
def playerProfile3(request,id):
    
    player=AgainstTeam.objects.get(id=id)
    return render(request, '../templates/html/playerProfile3.html',context={'player':player})
def playerProfile4(request,id):
    
    player=Position.objects.get(id=id)
    return render(request, '../templates/html/playerProfile4.html',context={'player':player})
def playerProfile5(request,id):
   
    player=Player.objects.get(name=id)
    return render(request, '../templates/html/playerProfile5.html',context={'player':player})
def playerProfile6(request,id):
   
    player=Player.objects.get(name=id)
    return render(request, '../templates/html/playerProfile6.html',context={'player':player})
def playerProfile7(request,id):
    
    player=Player.objects.get(name=id)
    return render(request, '../templates/html/playerProfile7.html',context={'player':player})

def login(request):
    return render(request, '../templates/html/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, '../templates/html/register.html', {'form': form})

def createprofile(request):
    all=glob.glob("./stats/*.yaml")
    for f in all:
        with open(f,'r') as file:
            every=Player.objects.all()
            for z in every:
                z.currentrunszero()
            every1=PlayerTeam.objects.all()
            for z in every1:
                z.currentrunszero()
            every2=City.objects.all()
            for z in every2:
                z.currentrunszero()
            every3=Position.objects.all()
            for z in every3:
                z.currentrunszero()
            list_cricket=yaml.full_load(file)
            ls=[]
            
            batlist=[]
            pp=[]
            mid=[]
            death=[]
            team1=list_cricket["innings"][0]["1st innings"]["team"]
            team2=list_cricket["innings"][1]["2nd innings"]["team"]
            city=list_cricket["info"]["city"]
            
            
            
            
                
            for x in list_cricket["innings"][0]["1st innings"]["deliveries"]:
                k=[key for key,value in x.items()]
                ls.append(k[0])
                if k[0]<7:
                    pp.append(k[0])
                if k[0]>=7 and k[0]<16:
                    mid.append(k[0])
                if k[0]>16:
                    death.append(k[0])
        k=0
        posi=1
        dicti={}
        for i in ls:
            wide=0
            legbyes=0
            e=0
            
            
            bye=0
            p=(list_cricket["innings"][0]["1st innings"]["deliveries"][k][i])
            b=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["batsman"]
            if b not in batlist:
                batlist.append(b)
                posb=Position.objects.filter(name=b,position=posi)
                if not posb:
                    
                    posb=Position(name=b,position=posi)
                    posb.save()
                posb=Position.objects.get(name=b,position=posi)
                dicti[b]=posb
                posi=posi+1
            bo=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["bowler"]
            runs=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["runs"]["batsman"]
            total=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["runs"]["total"]

            if "extras" in p.keys():
                e=1

                var=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["extras"]
                if "wides" in var.keys():
                    wide=1
                if "legbyes" in var.keys():
                    legbyes=1
                if "byes" in var.keys():
                    bye=1
            pla=Player.objects.filter(name=b)
            if not pla:
                profile=Player(name=b)
                
                profile.save()
            
            pla=Player.objects.get(name=b)
            if i<7:
                profile=PowerPlay.objects.filter(name=pla)
                if not profile:
                    pro=PowerPlay(name=pla)
                    pro.save()
                play=PowerPlay.objects.get(name=pla)
                play.ppupdateruns(runs)
            if i>=7 and i<16:
                profile=MiddleOvers.objects.filter(name=pla)
                if not profile:
                    pro=MiddleOvers(name=pla)
                    pro.save()
                player=MiddleOvers.objects.get(name=pla)
                player.midupdateruns(runs)
            if i>=16:
                profile=DeathOvers.objects.filter(name=pla)
                if not profile:
                    pro=DeathOvers(name=pla)
                    pro.save()
                players=DeathOvers.objects.get(name=pla)
                players.deathupdateruns(runs)
                
            plat=PlayerTeam.objects.filter(name=pla,Team=team1)
            ag=AgainstTeam.objects.filter(name=pla,Team=team2)
            cit=City.objects.filter(name=pla, City=city)
            if not cit:
                cite=City(name=pla,City=city)
                cite.save()
            if not plat:
                profileteam=PlayerTeam(name=pla,Team=team1)
                profileteam.save()
            if not ag:
                prot=AgainstTeam(name=pla,Team=team2)
                prot.save()
            prot=PlayerTeam.objects.get(name=pla,Team=team1)
            citi=City.objects.get(name=pla, City=city)
            agi=AgainstTeam.objects.get(name=pla,Team=team2)
            posb=dicti[b]
            prot.updateruns(runs)
            agi.updateruns(runs)
            posb.updateruns(runs)
            prot.setcurrentruns(runs)
            agi.setcurrentruns(runs)
            citi.updateruns(runs)
            citi.setcurrentruns(runs)
            posb.setcurrentruns(runs)
            pla.updateruns(runs)
            pla.setcurrentruns(runs)
            if wide==0:
                pla.updateballsfaced()
                prot.updateballsfaced()
                citi.updateballsfaced()
                posb.updateballsfaced()
                agi.updateballsfaced()
                if i<7:
                    play.ppupdateballsfaced()
                if i>=7 and i<16:
                    player.midupdateballsfaced()
                if i>=16:
                    players.deathupdateballsfaced()
            if runs==6:
                pla.updatesixes()
                prot.updatesixes()
                agi.updatesixes()
            if runs==4:
                pla.updatefours()
                prot.updatefours()
                agi.updatefours()

            pla=Player.objects.filter(name=bo)
            if not pla:
                profile=Player(name=bo)
                profile.save()
            pla=Player.objects.get(name=bo)
            plat=PlayerTeam.objects.filter(name=pla,Team=team2)
            citu=City.objects.filter(name=pla,City=city)
            aga=AgainstTeam.objects.filter(name=pla, Team=team1)
            if not plat:
                profileteam=PlayerTeam(name=pla,Team=team2)
                profileteam.save()
            if not citu:
                procit=City(name=pla, City=city)
                procit.save()
            if not aga:
                pi=AgainstTeam(name=pla,Team=team1)
                pi.save()
            prot=PlayerTeam.objects.get(name=pla,Team=team2)
            agn=AgainstTeam.objects.get(name=pla,Team=team1)
            citu=City.objects.get(name=pla, City=city)
            if i<7:
                profile=PowerPlay.objects.filter(name=pla)
                if not profile:
                    pro=PowerPlay(name=pla)
                    pro.save()
                play=PowerPlay.objects.get(name=pla)
                if e==0 or legbyes==1 or bye==1:
                    play.ppupdateballsbowled()

                if legbyes==0:
                    play.ppupdaterunsgiven(total)
            if i>=7 and i<16:
                profile=MiddleOvers.objects.filter(name=pla)
                if not profile:
                    pro=MiddleOvers(name=pla)
                    pro.save()
                player=MiddleOvers.objects.get(name=pla)
                if e==0 or legbyes==1 or bye==1:
                    player.midupdateballsbowled()
                if legbyes==0:
                    player.midupdaterunsgiven(total)
            if i>=16:
                profile=DeathOvers.objects.filter(name=pla)
                if not profile:
                    pro=DeathOvers(name=pla)
                    pro.save()
                players=DeathOvers.objects.get(name=pla)
                if e==0 or legbyes==1 or bye==1:
                    players.deathupdateballsbowled()
                if legbyes==0:
                    players.deathupdaterunsgiven(total)
            
            if e==0 or legbyes==1 or bye==1:
                pla.updateballsbowled()
                prot.updateballsbowled()
                citu.updateballsbowled()
                agn.updateballsbowled()
            if legbyes==0:
                pla.updaterunsgiven(total)
                prot.updaterunsgiven(total)
                citu.updaterunsgiven(total)
                agn.updaterunsgiven(total)

            if "wicket" in p.keys():
                    wi=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["player_out"]
                    #print(wi,end=":")
                    outupdate=Player.objects.get(name=wi)
                    outupdate.out()
                    outupdate1=PlayerTeam.objects.get(name=wi,Team=team1)
                    ou=AgainstTeam.objects.get(name=wi, Team=team2)
                    procit=City.objects.get(name=wi, City=city)
                    
                    outupdate1.out()
                    ou.out()
                    procit.out()
                    outupdate3=Position.objects.get(name=wi,position=dicti[wi].position)
                    outupdate3.out()
                    if i<7:
                        playoutupdate=Player.objects.get(name=wi)
                        ppoutupdate=PowerPlay.objects.get(name=playoutupdate)
                        ppoutupdate.ppout()
                    if i>=7 and i<16:
                        playoutupdate=Player.objects.get(name=wi)
                        midoutupdate=MiddleOvers.objects.get(name=playoutupdate)
                        midoutupdate.midout()
                    if i>=16:
                        playoutupdate=Player.objects.get(name=wi)
                        deathoutupdate=DeathOvers.objects.get(name=playoutupdate)
                        deathoutupdate.deathout()
                    
                        
                    ki=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["kind"]
           
                    x=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]
           
                    if "fielders" in x.keys():
                        c=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["fielders"][0]
                        fiel=Player.objects.filter(name=c)
                        if not fiel:
                            profile=Player(name=c)
                            profile.save()

                        fiel=Player.objects.get(name=c)
                        fiel.updatecatches()
                        pla.updatewickets()
                        prot.updatewickets()
                        citu.updatewickets()
                        if i<7:
                            play.ppupdatewickets()
                        if i>=7 and i<16:
                            player.midupdatewickets()
                        if i>=16:
                            players.deathupdatewickets()
                       
                    else:
                        if ki!="run out":
                            pla.updatewickets()
                            prot.updatewickets()
                            citu.updatewickets()
                            agn.updatewickets()
                            if i<7:
                                play.ppupdatewickets()
                            if i>=7 and i<16:
                                player.midupdatewickets()
                            if i>=16:
                                players.deathupdatewickets()

            k=k+1
        res=N.array(batlist)

        unique_res=N.unique(res)

        for some in unique_res:
            print(some)
            pin=Player.objects.get(name=some)
            pint=PlayerTeam.objects.get(name=some,Team=team1)
            pin.updateinnings() 
            pinto=AgainstTeam.objects.get(name=some,Team=team2)
            pinto.updateinnings() 
            posb=Position.objects.get(name=some,position=dicti[some].position)
            posb.updateinnings()
            pint.updateinnings()
            pc=City.objects.get(name=some,City=city)
            pc.updateinnings()
        every=Player.objects.all()
        for i in every:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.fourw()
            i.setfiftiesandhundreds()
        every1=PlayerTeam.objects.all()
        for i in every1:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        every6=AgainstTeam.objects.all()
        for i in every6:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
            
        every4=Position.objects.all()
        for i in every4:
            i.setaverage()
            i.setsr()
            
        ppevery=PowerPlay.objects.all()
        for j in ppevery:
            j.setppeco()
            j.setppsr()
            j.setppaverage()
        midevery=MiddleOvers.objects.all()
        for j in midevery:
            j.setmideco()
            j.setmidsr()
            j.setmidaverage()
        deathevery=DeathOvers.objects.all()
        for j in deathevery:
            j.setdeatheco()
            j.setdeathsr()
            j.setdeathaverage()
        
        every=Player.objects.all()
        for z in every:
            z.currentrunszero()
        every1=PlayerTeam.objects.all()
        for z in every1:
            z.currentrunszero()
        
        ls=[]
        batlist=[]
        pp=[]
        team1=list_cricket["innings"][0]["1st innings"]["team"]
        team2=list_cricket["innings"][1]["2nd innings"]["team"]
        
        
        
        posi=1
            
        for x in list_cricket["innings"][1]["2nd innings"]["deliveries"]:
            k=[key for key,value in x.items()]
            ls.append(k[0])
            if k[0]<7:
                pp.append(k[0])
        k=0
        dicti1={}
        for i in ls:
            wide=0
            legbyes=0
            
            
            e=0
            bye=0
            p=(list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i])
            b=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["batsman"]
            if b not in batlist:
                batlist.append(b)
                posb=Position.objects.filter(name=b,position=posi)
                if not posb:
                    
                    posb=Position(name=b,position=posi)
                    posb.save()
                posb=Position.objects.get(name=b,position=posi)
                dicti1[b]=posb
                posi=posi+1
            bo=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["bowler"]
            runs=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["runs"]["batsman"]
            total=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["runs"]["total"]

            if "extras" in p.keys():
                e=1

                var=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["extras"]
                if "wides" in var.keys():
                    wide=1
                if "legbyes" in var.keys():
                    legbyes=1
                if "byes" in var.keys():
                    bye=1
            pla=Player.objects.filter(name=b)
            if not pla:
                profile=Player(name=b)
                
                profile.save()
            
            pla=Player.objects.get(name=b)
            
            if i<7:
                profile=PowerPlay.objects.filter(name=pla)
                if not profile:
                    pro=PowerPlay(name=pla)
                    pro.save()
                play=PowerPlay.objects.get(name=pla)
                play.ppupdateruns(runs)
            plat=PlayerTeam.objects.filter(name=pla,Team=team2)
            at=AgainstTeam.objects.filter(name=pla,Team=team1)
            cit=City.objects.filter(name=pla, City=city)
            if not plat:
                profileteam=PlayerTeam(name=pla,Team=team2)
                profileteam.save()
            if not at:
                profileteam=AgainstTeam(name=pla,Team=team1)
                profileteam.save()
            if not cit:
                procit=City(name=pla, City=city)
                procit.save()

            prot=PlayerTeam.objects.get(name=pla,Team=team2)
            ot=AgainstTeam.objects.get(name=pla,Team=team1)
            citi=City.objects.get(name=pla, City=city)
            posb=dicti1[b]
            prot.updateruns(runs)
            ot.updateruns(runs)
            prot.setcurrentruns(runs)
            citi.updateruns(runs)
            citi.setcurrentruns(runs)
            ot.setcurrentruns(runs)
            pla.updateruns(runs)
            posb.updateruns(runs)
            pla.setcurrentruns(runs)
            posb.setcurrentruns(runs)
            if wide==0:
                pla.updateballsfaced()
                prot.updateballsfaced()
                posb.updateballsfaced()
                citi.updateballsfaced()
                ot.updateballsfaced()
                if i<7:
                    play.ppupdateballsfaced()
            if runs==6:
                pla.updatesixes()
                prot.updatesixes()
                ot.updatesixes()
            if runs==4:
                pla.updatefours()
                prot.updatefours()
                ot.updatefours()

            pla=Player.objects.filter(name=bo)
            if not pla:
                profile=Player(name=bo)
                profile.save()
            pla=Player.objects.get(name=bo)
            plat=PlayerTeam.objects.filter(name=pla,Team=team1)
            la=AgainstTeam.objects.filter(name=pla,Team=team2)
            citu=City.objects.filter(name=pla, City=city)
            if not plat:
                profileteam=PlayerTeam(name=pla,Team=team1)
                profileteam.save()
            if not la:
                profileteam=AgainstTeam(name=pla,Team=team2)
                profileteam.save()
            if not citu:
                procit=City(name=pla, City=city)
                procit.save()
            prot=PlayerTeam.objects.get(name=pla,Team=team1)
            ro=AgainstTeam.objects.get(name=pla,Team=team2)
            cite=City.objects.get(name=pla, City=city)
            if i<7:
                profile=PowerPlay.objects.filter(name=pla)
                if not profile:
                    pro=PowerPlay(name=pla)
                    pro.save()
                play=PowerPlay.objects.get(name=pla)
                if e==0 or legbyes==1 or bye==1:
                    play.ppupdateballsbowled()
                if legbyes==0:
                    play.ppupdaterunsgiven(total)
            
            if e==0 or legbyes==1 or bye==1:
                pla.updateballsbowled()
                prot.updateballsbowled()
                cite.updateballsfaced()
                ro.updateballsfaced()
            if legbyes==0:
                pla.updaterunsgiven(total)
                prot.updaterunsgiven(total)
                cite.updaterunsgiven(total)
                ro.updaterunsgiven(total)

            if "wicket" in p.keys():
                    wi=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["player_out"]
                    #print(wi,end=":")
                    outupdate=Player.objects.get(name=wi)
                    outupdate.out()
                    outupdate1=PlayerTeam.objects.get(name=wi,Team=team2)
                    outupdate2=City.objects.get(name=wi, City=city)
                    outupdate4=AgainstTeam.objects.get(name=wi,Team=team1)
                    outupdate3=Position.objects.get(name=wi,position=dicti1[wi].position)
                    outupdate2.out()
                    outupdate1.out()
                    outupdate3.out()
                    outupdate4.out()
                    if i<7:
                        playoutupdate=Player.objects.get(name=wi)
                        ppoutupdate=PowerPlay.objects.get(name=playoutupdate)
                        ppoutupdate.ppout()
                    
                        
                    ki=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["kind"]
            
                    x=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]
            
                    if "fielders" in x.keys():
                        c=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["fielders"][0]
                        fiel=Player.objects.filter(name=c)
                        if not fiel:
                            profile=Player(name=c)
                            profile.save()

                        fiel=Player.objects.get(name=c)
                        fiel.updatecatches()
                        pla.updatewickets()
                        prot.updatewickets()
                        cite.updatewickets()
                        ro.updatewickets()
                        if i<7:
                            play.ppupdatewickets()
                        
                    else:
                        if ki!="run out":
                            pla.updatewickets()
                            prot.updatewickets()
                            cite.updatewickets()
                            ro.updatewickets()
                            if i<7:
                                play.ppupdatewickets()

            k=k+1
        res=N.array(batlist)
      

        unique_res=N.unique(res)
        for some in unique_res:
            pin=Player.objects.get(name=some)
            pint=PlayerTeam.objects.get(name=some,Team=team2)
            pin.updateinnings() 
            pint.updateinnings()
            pinto=AgainstTeam.objects.get(name=some,Team=team1)
            pinto.updateinnings() 
            posb=Position.objects.get(name=some,position=dicti1[some].position)
            posb.updateinnings()
            pc=City.objects.get(name=some,City=city)
            pc.updateinnings()
        every=Player.objects.all()
        for i in every:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        every1=PlayerTeam.objects.all()
        for i in every1:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        every3=City.objects.all()
        for i in every3:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        every6=AgainstTeam.objects.all()
        for i in every6:
            i.seteco()
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        every4=Position.objects.all()
        for i in every4:
            i.setaverage()
            i.setsr()
            i.setfiftiesandhundreds()
        ppevery=PowerPlay.objects.all()
        for j in ppevery:
            j.setppeco()
            j.setppsr()
            j.setppaverage()
    return HttpResponse("updated")
def search_players(request):
    query=request.GET.get('q1')
    ls=query.split(' ')
    l=len(ls)
    if query:
        posts = Player.objects.all()
        if l==1:
            results=posts.filter(Q(name__icontains=ls[0]))
        if l==2:
            results=posts.filter(Q(name__icontains=ls[0])|Q(name__icontains=ls[1]))

	
    return render(request, '../templates/html/playerslist.html',context={'players':results})


def matchuprecords(request):
    all=glob.glob("./stats/*.yaml")
    for f in all:
        with open(f,'r') as file:
            every=Player.objects.all()
            
            list_cricket=yaml.full_load(file)
            ls=[]
            
            batlist=[]
            pp=[]
            mid=[]
            death=[]
            team1=list_cricket["innings"][0]["1st innings"]["team"]
            team2=list_cricket["innings"][1]["2nd innings"]["team"]
           
            
            
            
                
            for x in list_cricket["innings"][0]["1st innings"]["deliveries"]:
                k=[key for key,value in x.items()]
                ls.append(k[0])
            
            k=0
            for i in ls:
                wide=0
                legbyes=0
                e=0
                bye=0
                p=(list_cricket["innings"][0]["1st innings"]["deliveries"][k][i])
                b=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["batsman"]
                batlist.append(b)
                bo=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["bowler"]
                runs=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["runs"]["batsman"]
                total=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["runs"]["total"]
                if "extras" in p.keys():
                    e=1
                    var=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["extras"]
                    if "wides" in var.keys():
                        wide=1
                    if "legbyes" in var.keys():
                        legbyes=1
                    if "byes" in var.keys():
                        bye=1
                pla=Player.objects.get(name=b)
                mat=Matchups.objects.filter(name=pla,bowler=bo)
                if not mat:
                    profile=Matchups(name=pla,bowler=bo)
                    profile.save()
                mat=Matchups.objects.get(name=pla, bowler=bo)
                mat.updateruns(runs)
                if wide==0:
                    mat.updateballsfaced()

                play=Player.objects.get(name=bo)
                mats=Matchups.objects.filter(name=play,bowler=b)
                if not mats:
                    profile=Matchups(name=play,bowler=b)
                    profile.save()
                mats=Matchups.objects.get(name=play,bowler=b)
                if e==0 or legbyes==1 or bye==1:
                    mats.updateballsbowled()
                if legbyes==0 :
                    mats.updaterunsgiven(total)

                if "wicket" in p.keys():
                    wi=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["player_out"]
                    #print(wi,end=":")
                    outupdate=Player.objects.get(name=wi)
                    
                    outupdate1=Matchups.objects.get(name=wi,bowler=bo)
                  
                    ki=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["kind"]
           
                    x=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]
           
                    if "fielders" in x.keys():
                        c=list_cricket["innings"][0]["1st innings"]["deliveries"][k][i]["wicket"]["fielders"][0]
                        
                        if ki != "run out":
                            mats.updatewickets()
                            mat.updateouts()
                    else:
                        mats.updatewickets()
                        mat.updateouts()

                k=k+1
            
            every=Matchups.objects.all()
            for i in every:
                i.seteco()
                i.setaverage()
                i.setsr()
            ls1=[]
            for x in list_cricket["innings"][1]["2nd innings"]["deliveries"]:
                k=[key for key,value in x.items()]
                ls1.append(k[0])
            k=0
            for i in ls1:
                wide=0
                legbyes=0
                e=0
                bye=0
                p=(list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i])
                b=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["batsman"]
                batlist.append(b)
                bo=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["bowler"]
                runs=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["runs"]["batsman"]
                total=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["runs"]["total"]
                pla=Player.objects.get(name=b)
                mat=Matchups.objects.filter(name=pla,bowler=bo)
                if not mat:
                    profile=Matchups(name=pla,bowler=bo)
                    profile.save()
                mat=Matchups.objects.get(name=pla, bowler=bo)
                mat.updateruns(runs)
                if wide==0:
                    mat.updateballsfaced()

                play=Player.objects.get(name=bo)
                mats=Matchups.objects.filter(name=play,bowler=b)
                if not mats:
                    profile=Matchups(name=play,bowler=b)
                    profile.save()
                mats=Matchups.objects.get(name=play,bowler=b)
                if e==0 or legbyes==1 or bye==1:
                    mats.updateballsbowled()
                if legbyes==0:
                    mats.updaterunsgiven(total)

                if "wicket" in p.keys():
                    wi=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["player_out"]
                    #print(wi,end=":")
                    outupdate=Player.objects.get(name=wi)
                    
                    outupdate1=Matchups.objects.get(name=wi,bowler=bo)
                  
                    ki=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["kind"]
           
                    x=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]
           
                    if "fielders" in x.keys():
                        c=list_cricket["innings"][1]["2nd innings"]["deliveries"][k][i]["wicket"]["fielders"][0]
                        
                        if ki != "run out":
                            mats.updatewickets()
                            mat.updateouts()
                    else:
                        mats.updatewickets()
                        mat.updateouts()

                k=k+1
            
            every=Matchups.objects.all()
            for i in every:
                i.seteco()
                i.setaverage()
                i.setsr()

        
        return HttpResponse("updated")
                        