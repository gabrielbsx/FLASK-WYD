from flask import redirect, url_for, render_template, request, session, flash, g
from app import app
from app.models.forms import LoginForm
from app.controllers import c_struct
import sys
from io import BytesIO
import ctypes
import os
from app.controllers.config import *

@app.before_request
def before_request():
    g.user = None
    if ('login' in session and session['login'] is not None):
        g.user = session['login']
        with open(DBSRV + 'account/' + getInitial(g.user) + '/' + g.user, 'rb') as acc:
            g.structacc = c_struct.STRUCT_ACCOUNTFILE()
            acc.readinto(g.structacc)
            with open(COMMON + 'ItemList.bin', 'rb') as listitem:
                g.structitem = c_struct.STRUCT_ITEMLISTALL()
                itemlist = c_struct.xor_c(listitem.read())
                listitem.close()
                readitemlist = BytesIO(bytes(itemlist))
                readitemlist.readinto(g.structitem)
                with open(COMMON + 'Guilds.txt', 'r') as guilds:
                    gds = guilds.read()
                    guilds.close()
                    gds = re.sub(' +', ' ', gds).split("\n")
                    g.guilds = {}
                    for gd in gds:
                        if (gd.split(' ')[2] is not ''):
                            g.guilds[int(gd.split(' ')[2])] = {
                                'group': gd.split(' ')[0],
                                'server': gd.split(' ')[1],
                                'guildname': gd.split(' ')[3]
                            }

@app.route('/home')
@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html', page='Início')

@app.route('/dashboard')
def dashboard():
    if 'login' in session and session['login'] is not None:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=["POST", "GET"])
def login():
    if 'login' not in session or session['login'] is None:
        form = LoginForm()
        if request.method == 'POST':
            if 'password' and 'username' in request.form: 
                if form.validate_on_submit():
                    accountFile = DBSRV + 'account/' + getInitial(form.username.data) + '/' + form.username.data
                    if os.path.isfile(accountFile):
                        with open(accountFile, 'rb') as fp:
                            account = c_struct.STRUCT_ACCOUNTFILE()
                            fp.readinto(account)
                            if(account.Info.AccountName.decode().lower() == form.username.data.lower() and account.Info.AccountPass.decode() == form.password.data):
                                session['login'] = account.Info.AccountName.decode().lower()                                
                                flash(f'Login efetuado com sucesso!', 'success')
                                return redirect(url_for('dashboard'))
                            else:
                                flash(f'Não foi possível efetuar o login!', 'danger')
                    else:
                        flash(f'Conta inexistente!', 'danger')
            return render_template('login.html', form=form)
        elif request.method == 'GET':
            return render_template('login.html', page='Login', form=form)
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    if 'login' in session and session['login'] is not None:
        session.clear()
        g.user = None
        g.structitem = None
        g.structacc = None
        flash(f'Logout efetuado com sucesso!', 'success')
    return redirect(url_for('home'))

@app.route('/downloads', methods=['GET'])
def downloads():
    return render_template('downloads.html')

@app.route('/account/<acc>')
def alydoo(acc):
    account = c_struct.STRUCT_ACCOUNTFILE()
    filepath = DBSRV + 'account/' + getInitial(acc) + '/' + acc
    if (os.path.isfile(filepath)):
        with open(filepath, 'rb') as acc:
            binbool = acc.readinto(account)
        return account.Info.AccountName.decode()
    return str(0)

@app.route('/itemlist/<id>', methods=['GET'])
def itemlist(id):
    if (id.isdigit()):
        if (int(id) >= 0 and int(id) < 6500):
            path = 'C:/_SERVIDOR/Common/ItemList.bin'
            with open(path, 'rb') as listitem:
                itemliststruct = c_struct.STRUCT_ITEMLISTALL()
                itemlist = c_struct.xor_c(listitem.read())
                listitem.close()
                readitemlist = BytesIO(bytes(itemlist))
                readitemlist.readinto(itemliststruct)
            return str(itemliststruct.id[int(id)].Name.decode('latin-1'))
        return str(0)
    return str(0)

@app.route('/guildinfo/<id>', methods=['GET'])
def guildinfo(id):
    if (id.isdigit()):
        if (int(id) >= 0 and int(id) < 65536):
            path = 'C:/_SERVIDOR/Common/GuildInfo'
            with open(path, 'rb') as infoguild:
                guildinfostruct = c_struct.STRUCT_GUILDINFOALL()
                infoguild.readinto(guildinfostruct)
            return str(guildinfostruct.GuildInfo[int(id)].Fame)
        return str(0)
    return str(0)

@app.route('/skill/<id>', methods=['GET'])
def spell(id):
    if (id.isdigit()):
        if (int(id) >= 0 and int(id) < 103):
            path = 'C:/_SERVIDOR/Common/SkillData.bin'
            with open(path, 'rb') as dataskill:
                skilldatastruct = c_struct.STRUCT_SPELLALL()
                skilldata = c_struct.xor_c(dataskill.read())
                dataskill.close()
                readskilldata = BytesIO(bytes(skilldata))
                readskilldata.readinto(skilldatastruct)
                return str(skilldatastruct.skill[int(id)].SkillPoint)
        return str(0)
    return str(0)

